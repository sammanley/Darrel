#!/bin/bash

# Prompt for the domain
echo "Enter the domain: "
read domain

# Prompt for the filename
echo "Enter the filename: "
read filename

# Execute the curl command and save the output to a temporary file
curl -s "$domain" | grep -Eo '\b(\+?1[.-]?)?(\([2-9][0-8][0-9]\)|[2-9][0-8][0-9])[-.]?[0-9]{3}[-.]?[0-9]{4}\b' > "$filename.tmp"

# Remove redundant phone numbers and save the cleaned output to the final file
sort "$filename.tmp" | uniq > "$filename"

# Remove the temporary file
rm "$filename.tmp"

echo "Phone numbers scraped from $domain have been saved to $filename"

# Created by Samuel Manley aka ImmaFish
