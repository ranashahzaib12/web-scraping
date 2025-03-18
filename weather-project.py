



# import requests

# def get_weather(city):
#     city = city.replace(" ", "+")  # Format city name for URL
#     url = f"https://wttr.in/{city}?format=%C+%t+%h+%w"

#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             # Extract weather details from response text
#             weather_data = response.text.strip().split(" ")

#             # Store data in a dictionary
#             weather_info = {
#                 "City": city.replace("+", " ").title(),
#                 "Condition": weather_data[0],  # Weather condition (e.g., Clear, Rain)
#                 "Temperature": weather_data[1],  # Temperature
#                 "Humidity": weather_data[2],  # Humidity
#                 "Wind Speed": weather_data[3]  # Wind Speed
#             }

#             print(weather_info)  # Print data as JSON-like dictionary
#         else:
#             print("Failed to retrieve weather data.")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# get_weather("Lahore")





import requests
import pandas as pd
import time

# List of world capitals
capitals = [
    "Kabul", "Tirana", "Algiers", "Andorra la Vella", "Luanda", "Buenos Aires", "Yerevan", "Canberra",
    "Vienna", "Baku", "Manama", "Dhaka", "Bridgetown", "Minsk", "Brussels", "Belmopan", "Porto-Novo",
    "Thimphu", "La Paz", "Sarajevo", "Gaborone", "Brasilia", "Sofia", "Ouagadougou", "Gitega", "Phnom Penh",
    "Yaoundé", "Ottawa", "Praia", "Bangui", "N'Djamena", "Santiago", "Beijing", "Bogotá", "Moroni",
    "San José", "Zagreb", "Havana", "Nicosia", "Prague", "Kinshasa", "Copenhagen", "Djibouti", "Roseau",
    "Quito", "Cairo", "San Salvador", "Malabo", "Asmara", "Tallinn", "Mbabane", "Addis Ababa", "Suva",
    "Helsinki", "Paris", "Libreville", "Banjul", "Tbilisi", "Berlin", "Accra", "Athens", "Guatemala City",
    "Conakry", "Bissau", "Georgetown", "Port-au-Prince", "Tegucigalpa", "Budapest", "Reykjavik", "New Delhi",
    "Jakarta", "Tehran", "Baghdad", "Dublin", "Jerusalem", "Rome", "Tokyo", "Amman", "Nur-Sultan", "Nairobi",
    "Tarawa", "Kuwait City", "Bishkek", "Vientiane", "Riga", "Beirut", "Maseru", "Monrovia", "Tripoli",
    "Vilnius", "Luxembourg", "Antananarivo", "Lilongwe", "Kuala Lumpur", "Male", "Bamako", "Valletta",
    "Majuro", "Nouakchott", "Port Louis", "Mexico City", "Palikir", "Chisinau", "Monaco", "Ulaanbaatar",
    "Podgorica", "Rabat", "Maputo", "Naypyidaw", "Windhoek", "Kathmandu", "Amsterdam", "Wellington",
    "Managua", "Niamey", "Abuja", "Pyongyang", "Oslo", "Muscat", "Islamabad", "Panama City", "Port Moresby",
    "Asunción", "Lima", "Manila", "Warsaw", "Lisbon", "Doha", "Bucharest", "Moscow", "Kigali", "Apia",
    "San Marino", "Riyadh", "Dakar", "Belgrade", "Victoria", "Freetown", "Singapore", "Bratislava", "Ljubljana",
    "Honiara", "Mogadishu", "Pretoria", "Seoul", "Juba", "Madrid", "Colombo", "Khartoum", "Paramaribo",
    "Stockholm", "Damascus", "Taipei", "Dushanbe", "Dodoma", "Bangkok", "Lomé", "Tunis", "Ankara", "Ashgabat",
    "Kampala", "Kyiv", "Abu Dhabi", "London", "Washington", "Montevideo", "Tashkent", "Port Vila", "Vatican City",
    "Caracas", "Hanoi", "Sana'a", "Lusaka", "Harare"
]

# Initialize an empty list to store weather data
weather_data = []

# Loop through each capital and scrape data
for city in capitals:
    try:
        url = f"https://wttr.in/{city}?format=%C+%t+%h+%w"  # Fetch weather data in a readable format
        response = requests.get(url)

        if response.status_code == 200:
            data = response.text.strip().split(" ")  # Split the response

            # Append data to the list
            weather_data.append({
                "City": city,
                "Condition": data[0],  # Weather condition (e.g., Clear, Rainy)
                "Temperature": data[1],  # Temperature
                "Humidity": data[2],  # Humidity
                "Wind Speed": data[3]  # Wind Speed
            })
            print(f"Retrieved: {city}")  # Print progress

        else:
            print(f"Failed to retrieve weather for {city}")

    except Exception as e:
        print(f"Error retrieving {city}: {e}")
    time.sleep(1)  # Pause for 1 second to avoid being blocked

# Save to CSV
df = pd.DataFrame(weather_data)
df.to_csv("world_capitals_weather.csv", index=False)

print("✅ Weather data saved to 'world_capitals_weather.csv' successfully!")
