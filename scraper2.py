from linkedin_api import Linkedin
import csv
import json

# Authenticate using any Linkedin account credentials
api = Linkedin('***REMOVED***', '***REMOVED***')

link = 'https://ca.linkedin.com/in/gerry-vandenham-pmp-ibm-tivoli-maximo-7-8304936'
profile_url = link.split('/in/')[1]

# Read the existing data from the JSON file
with open(profile_url + '.json', 'r') as file:
    data = json.load(file)

contact_info = api.get_profile_contact_info(profile_url)
data.update(contact_info)

# Write the updated data back to the JSON file
with open(profile_url + '.json', 'w') as file:
    json.dump(data, file, indent=4)