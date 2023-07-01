import re
import requests
from urllib.parse import urlparse

# Prompt for the domain URL
domain_url = input("Enter the domain URL: ")

# Parse the domain URL to extract the domain name
parsed_url = urlparse(domain_url)
domain = parsed_url.netloc

# Check if the domain URL has a schema
if not parsed_url.scheme:
    domain_url = "http://" + domain_url

# Prompt for the filename
filename = input("Enter the filename: ")

# Send a GET request to the specified domain
response = requests.get(domain_url)

# Extract phone numbers using regular expressions
phone_numbers = re.findall(r'\b(\+?1[.-]?)?(\([2-9][0-8][0-9]\)|[2-9][0-8][0-9])[-.]?([0-9]{3})[-.]?([0-9]{4})\b', response.text)

# Remove redundant phone numbers
unique_phone_numbers = set(''.join(number) for number in phone_numbers)

# Save the phone numbers to the specified file
with open(filename, 'w') as file:
    for number in unique_phone_numbers:
        file.write(number + '\n')

print(f"Phone numbers scraped from {domain} have been saved to {filename}")

# Darrel is a Web Scraper created by Samuel Manley AKA ImmaFish
