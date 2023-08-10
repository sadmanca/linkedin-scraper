import csv
import json
import os

# Read the headers from a text file
with open('table-headers.txt', 'r') as file:
    headers = [line.strip() for line in file]

# Open the output CSV file for writing
with open('sample_lead_profiles.csv', 'w', newline='') as csvfile:
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
                        "{}. COMPANY: {}\nJOB TITLE: {}\nLOCATION: {}\n".format(
                            i + 1,
                            item.get('companyName', ''),
                            item.get('title', '').replace('\n', ' '),
                            item.get('locationName', 'N/A') if item.get('locationName', '') else 'N/A'
                        )
                        for i, item in enumerate(data.get('experience', []))
                    ]
                    if titles:
                        row.append('\n'.join(titles))
                    else:
                        row.append('')
                        
                elif header == 'job descriptions':
                    descriptions = [
                        "{}. COMPANY: {}\nJOB TITLE: {}\nLOCATION: {}\nDESCRIPTION: {}\n".format(
                            i + 1,
                            item.get('companyName', ''),
                            item.get('title', '').replace('\n', ' '),
                            item.get('locationName', 'N/A') if item.get('locationName', '') else 'N/A',
                            item.get('description', 'N/A')
                        )
                        for i, item in enumerate(data.get('experience', []))
                    ]
                    if descriptions:
                        row.append('\n'.join(descriptions))
                    else:
                        row.append('')
                        
                elif header == 'name':
                    # Concatenate the values of the 'firstName' and 'lastName' keys with a space separator
                    row.append(data.get('firstName', '') + ' ' + data.get('lastName', ''))
                    
                elif header == 'public_id':
                    # Append 'https://www.linkedin.com/in/' followed by the value of the 'public_id' key to the 'row' list
                    row.append('https://www.linkedin.com/in/' + data.get(header, ''))
                
                elif header == 'twitter':
                    if isinstance(data.get(header), list) and len(data.get(header)) == 1:
                        row.append('https://twitter.com/' + data.get(header)[0].get('name', ''))
                        
                elif header == 'websites':
                    # Extract the URLs from the 'websites' list and join them with commas
                    urls = [item.get('url', '') for item in data.get(header, [])]
                    if urls:
                        row.append(',\n'.join(urls))
                    else:
                        row.append('')
                        
                elif header == 'locationName':
                    location = data.get('locationName', '')
                    geo_location = data.get('geoLocationName', '')
                    row.append(geo_location + ', ' + location)
                    
                else:
                    # Use the value of the header as-is
                    if header:
                        value = data.get(header)
                        if isinstance(value, list) and not value:
                            row.append('')
                        else:
                            row.append(value)
                    else:
                        row.append('')

            # Write the data to the CSV file
            writer.writerow(row)