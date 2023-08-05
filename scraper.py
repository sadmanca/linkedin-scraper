from linkedin_api import Linkedin
import csv
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Authenticate using any Linkedin account credentials
api = Linkedin(os.environ.get('LINKEDIN_EMAIL'), os.environ.get('LINKEDIN_PASSWORD'))
# api = Linkedin(os.environ.get('LINKEDIN_EMAIL_ALTERNATIVE'), os.environ.get('LINKEDIN_PASSWORD_ALTERNATIVE'))

# GET a profile
# profile = api.get_profile('khushi-thakkar-906b56188')
link = 'https://ca.linkedin.com/in/gerry-vandenham-pmp-ibm-tivoli-maximo-7-8304936'
profile_url = link.split('/in/')[1]
profile = api.get_profile(profile_url)

# # print(profile)
# with open('profile.txt', 'w') as file:
#     file.write(str(profile))

# Read the contents of the text file into a string variable
# with open('profile.txt', 'r') as file:
#     profile_str = file.read()

# # Convert the string back to a dictionary using eval()
# profile = eval(profile_str)

# print(profile)
with open(profile_url + '.json', 'w') as file:
    json.dump(profile, file, indent=4)

# Get the column headers by finding all unique keys in the dictionary
# column_headers = set()
# for key, value in profile.items():
#     if not key == "experience":
#         print(f"key: {key}")
#         print(f"value: {value}")
#     if key == "experience":
#         print(f"key: {key}")
#         print(f"EXPERIENCE LIST LENGTH: {len(value)}")
#         print(f"value keys: {value[0].keys()}")
#         column_headers.update(value[0].keys())
#         break

# # Write the data to the CSV file
# with open('profile.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(list(column_headers))
#     for key, value in profile.items():
#         row_data = []
#         for column_header in column_headers:
#             row_data.append(value.get(column_header, ''))
#         writer.writerow(row_data)

# GET a profiles contact info
# contact_info = api.get_profile_contact_info('khushi-thakkar-906b56188')

# print(contact_info)
# with open('contact_info.txt', 'w') as file:
#     file.write(str(contact_info))

# # Get the column headers by finding all unique keys in the dictionary
# column_headers = set()
# for key, value in contact_info.items():
#     column_headers.update(value.keys())

# # Write the data to the CSV file
# with open('contact_info.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(list(column_headers))
#     for key, value in contact_info.items():
#         row_data = []
#         for column_header in column_headers:
#             row_data.append(value.get(column_header, ''))
#         writer.writerow(row_data)