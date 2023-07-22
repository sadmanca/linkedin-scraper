import csv
import json
import os

# Read the headers from a text file
with open('headers.txt', 'r') as file:
    headers = [line.strip() for line in file]

# Open the output CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the headers to the CSV file
    writer.writerow(headers)

    # Loop through each JSON file in the directory
    for filename in os.listdir('.'):
        if filename.endswith('.json'):
            # Load the JSON data from the file
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)

            # Extract the relevant data from the JSON object
            row = []
            for header in headers:
                if header == 'titles':
                    # Extract the value of the 'title' key from each item in the 'experience' list
                    titles = [
                        f"{item.get('title', '')} at {item.get('companyName', '')}" +
                        (f" ({item.get('locationName', '')})" if item.get('locationName', '') else '')
                        for item in data.get('experience', [])
                    ]
                    if titles:
                        row.append(', '.join(titles))
                    else:
                        row.append('')
                        
                elif header == 'job descriptions':
                    descriptions = [f"{item.get('description', 'NO_DESCRIPTION')} at {item.get('companyName', '')}" for item in data.get('experience', [])]
                    if descriptions:
                        row.append(', '.join(descriptions))
                    else:
                        row.append('')    
                                    
                elif header == 'name':
                    # Concatenate the values of the 'firstName' and 'lastName' keys with a space separator
                    row.append(data.get('firstName', '') + ' ' + data.get('lastName', ''))
                    
                elif header == 'public_id':
                    # Append 'https://www.linkedin.com/in/' followed by the value of the 'public_id' key to the 'row' list
                    row.append('https://www.linkedin.com/in/' + data.get(header, ''))
                    
                else:
                    # Use the value of the header as-is
                    row.append(data.get(header, ''))

            # Write the data to the CSV file
            writer.writerow(row)