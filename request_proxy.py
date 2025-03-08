import random
import requests

"""
List of Free Proxies:

The proxy_list is a list containing the addresses of free proxy servers.

In the list, you should replace "http://proxy1:port", "http://proxy2:port", and "http://proxy3:port" with actual proxy addresses. Each proxy has an IP address and a port number, and you can get these proxies from free proxy websites like:

https://www.freeproxylists.net/
https://www.sslproxies.org/
https://www.socks-proxy.net/
Example of proxies (replace these with actual ones)

"""

# List of proxies (updated with your proxy list)
proxy_list = [
    "http://85.215.64.49:80", 
    "http://18.223.25.15:80", 
    "http://50.223.246.237:80", 
    "http://50.174.7.159:80",   
    "http://50.202.75.26:80",   
    "http://50.221.74.130:80",  
    "http://190.58.248.86:80",  
    "http://203.115.101.51:82",  
    "http://65.108.203.37:28080",  
    "http://54.67.125.45:3128",  
    "http://184.169.154.119:80",  
    "http://13.56.192.187:80",  
    "http://65.108.195.47:8080"   
]

# Randomly select a proxy
proxy = {"http": random.choice(proxy_list), "https": random.choice(proxy_list)}

# Send request through the proxy
response = requests.get("https://quotes.toscrape.com/", proxies=proxy)

# Print the HTML content of the page
print(response.text)
