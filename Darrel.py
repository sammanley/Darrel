import re
import requests

# Prompt for the domain
domain = input("Enter the domain: ")

# Prompt for the filename
filename = input("Enter the filename: ")

# Send a GET request to the specified domain
response = requests.get(domain)

# Extract phone numbers using regular expressions
phone_numbers = re.findall(r'\b(\+?1[.-]?)?(\([2-9][0-8][0-9]\)|[2-9][0-8][0-9])[-.]?[0-9]{3}[-.]?[0-9]{4}\b', response.text)

# Remove redundant phone numbers
unique_phone_numbers = list(set(phone_numbers))

# Save the phone numbers to the specified file
with open(filename, 'w') as file:
    for number in unique_phone_numbers:
        file.write(number + '\n')

print(f"Phone numbers scraped from {domain} have been saved to {filename}")

# Created by Samuel Manley aka ImmaFish
