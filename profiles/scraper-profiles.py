from linkedin_api import Linkedin
import csv
import json


# # Authenticate using any Linkedin account credentials
api = Linkedin('***REMOVED***', '***REMOVED***')
# api = Linkedin('***REMOVED***', '***REMOVED***')

# Read the list of profile URLs from the TODO file
with open('profiles_TODO.txt', 'r') as file:
    urls = [line.strip() for line in file]

# Process each profile URL
for url in urls:
    # GET the profile data
    profile_url = url.split('/in/')[1]
    print(profile_url)
    profile = api.get_profile(profile_url)

    # Write the profile data to a JSON file
    with open(profile_url + '.json', 'w') as file:
        json.dump(profile, file, indent=4)

    # Read the existing data from the JSON file
    with open(profile_url + '.json', 'r') as file:
        data = json.load(file)

    # Update the data with contact info
    contact_info = api.get_profile_contact_info(profile_url)
    data.update(contact_info)

    # Write the updated data back to the JSON file
    with open(profile_url + '.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Move the URL from the TODO file to the DONE file
    with open('profiles_TODO.txt', 'r') as todo_file:
        lines = todo_file.readlines()
    with open('profiles_TODO.txt', 'w') as todo_file:
        for line in lines:
            if line.strip() != url:
                todo_file.write(line)
    with open('profiles_DONE.txt', 'a') as done_file:
        done_file.write(url + '\n')