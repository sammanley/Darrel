import re
import requests
from urllib.parse import urlparse

def extract_phone_numbers(text):
    return re.findall(r'\b(\+?1[.-]?)?(\([2-9][0-8][0-9]\)|[2-9][0-8][0-9])[-.]?([0-9]{3})[-.]?([0-9]{4})\b', text)

def extract_emails(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

def print_divider():
    print("-" * 29)

def save_to_file(file, url, unique_phone_numbers, unique_emails):
    file.write("-" * 29 + '\n')
    file.write(f"Site: {url}\n")
    file.write("-" * 29 + '\n')

    if unique_phone_numbers:
        file.write("Phone Numbers:\n")
        for number in unique_phone_numbers:
            file.write(number + '\n')
        file.write("-" * 29 + '\n')

    if unique_emails:
        file.write("Emails:\n")
        for email in unique_emails:
            file.write(email + '\n')
        file.write("-" * 29 + '\n')

def scrape_and_print_info(url):
    response = requests.get(url)
    phone_numbers = extract_phone_numbers(response.text)
    emails = extract_emails(response.text)

    unique_phone_numbers = set(''.join(number) for number in phone_numbers)
    unique_emails = set(emails)

    print_divider()
    print(f"Site: {url}")
    print_divider()

    if unique_phone_numbers:
        print("Phone Numbers:")
        for number in unique_phone_numbers:
            print(number)
        print_divider()

    if unique_emails:
        print("Emails:")
        for email in unique_emails:
            print(email)
        print_divider()

    return unique_phone_numbers, unique_emails

if __name__ == "__main__":
    # Prompt for multiple URLs
    urls = input("Enter one or more URLs separated by spaces: ").split()

    # Prompt for the filename
    filename = input("Enter the filename: ")

    with open(filename, 'w') as file:
        for url in urls:
            # Parse the domain URL to extract the domain name
            parsed_url = urlparse(url)
            domain = parsed_url.netloc

            # Check if the domain URL has a schema
            if not parsed_url.scheme:
                url = "http://" + url

            # Scraping and printing information
            unique_phone_numbers, unique_emails = scrape_and_print_info(url)

            # Save the phone numbers and emails to the specified file
            save_to_file(file, url, unique_phone_numbers, unique_emails)

            print(f"Phone numbers and emails scraped from {domain} have been saved to {filename}\n")
