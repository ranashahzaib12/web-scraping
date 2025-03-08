from bs4 import BeautifulSoup
import requests
import sys
import json 

# Set encoding to UTF-8 to avoid Unicode errors
sys.stdout.reconfigure(encoding='utf-8')

# Walmart product URL
url = "https://www.walmart.com/ip/Gawfolk-34-Inch-Curved-Gaming-Monitor-165hz-Ultrawide-WQHD-3440x1440-Screen-PC-Computer-1500R-21-9/5239346994?classType=VARIANT&athbdg=L1600&adsRedirect=true"

# Sometimes the data may not load there could be a reason of it 
# website could be Dynamic ,or website may not allow to fetch it 
# Right click and Inspect the Site clearly for TAGs

# SOlution to above is >> inspect site >> Network >> Copy the beloww requirements which we didd below



HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the script tag containing product data
    script_tag = soup.find("script", id="__NEXT_DATA__")

    if script_tag:
        try:
            # Load JSON data from script tag
            data = json.loads(script_tag.string)

            # Navigate to product details
            product_info = data.get("props", {}).get("pageProps", {}).get("initialData", {}).get("data", {}).get("product", {})

            # Extract details safely
            title = product_info.get("name", "N/A")
            brand = product_info.get("brand", "N/A")  # Ensure brand is extracted safely
            if isinstance(brand, dict):  # If brand is a dictionary, get its "name" field
                brand = brand.get("name", "N/A")

            price = product_info.get("priceInfo", {}).get("currentPrice", "N/A")
            rating = product_info.get("rating", {}).get("averageRating", "N/A")
            reviews_count = product_info.get("rating", {}).get("count", "N/A")
            availability = product_info.get("availabilityStatus", "N/A")

            # Display extracted details
            print(f"🛒 Product Name: {title}")
            print(f"🏷 Brand: {brand}")
            print(f"💰 Price: ${price}")
            print(f"⭐ Rating: {rating} / 5")
            print(f"📝 Reviews: {reviews_count}")
            print(f"📦 Availability: {availability}")

        except (KeyError, TypeError, json.JSONDecodeError) as e:
            print(f"❌ Error: Unable to extract product details. JSON structure may have changed.\nError: {e}")
    else:
        print("❌ Error: '__NEXT_DATA__' script tag not found.")
else:
    print(f"❌ Error: Failed to fetch page (Status Code: {response.status_code})")
