import yagooglesearch
from linkedin_api import Linkedin
import json
from dotenv import load_dotenv
import os
from datetime import datetime
from tqdm import tqdm
import zipfile

load_dotenv()

# query = "site:linkedin.com/in \"manager\" \"asset management\" \"ibm maximo\""

# query = "site:linkedin.com/in manager asset management \"ibm maximo\""

# client = yagooglesearch.SearchClient(
#     query,
#     # tbs="li:1", # verbatim search
#     max_search_result_urls_to_return=1000,
#     http_429_cool_off_time_in_minutes=5,
#     http_429_cool_off_factor=1.5,
#     minimum_delay_between_paged_results_in_seconds=1,
#     # proxy="socks5h://127.0.0.1:9050",
#     verbosity=5, # 6 turns off all terminal output
#     verbose_output=False,  # False (only URLs) or True (rank, title, description, and URL),
#     google_exemption = os.environ.get("GOOGLE_ABUSE_EXEMPTION_COOKIE"),
# )
# client.assign_random_user_agent()

# urls = client.search()

# # Get the current date and time
# now = datetime.now()

# # Format the date as an ISO string
# date_str = now.date().isoformat()

# # Create the filename with the ISO date and "-urls" suffix
# filename_TODO = f"{date_str}-linkedin-urls.txt"

# # Write the URLs to the file
# with open(filename_TODO, 'w') as f:
#     for url in urls:
#         f.write(url + '\n')

# ---------------------------------------------------------------

filename_TODO = r"linkedin-scraper\2023-08-09-linkedin-urls.txt"
filename_DONE = r"linkedin-scraper\DONE-2023-08-09-linkedin-urls.txt"

# Authenticate using any Linkedin account credentials
api = Linkedin(os.environ.get('LINKEDIN_EMAIL'), os.environ.get('LINKEDIN_PASSWORD'))

# Read the list of profile URLs from the TODO file
with open(filename_TODO, 'r') as file:
    urls = [line.strip() for line in file]

# Create the folder with the current timestamp
# now = datetime.now()
# timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
# folder_name = f'json_{timestamp}'
folder_name = 'json'
os.mkdir(folder_name)

i = 0    
# Process each profile URL
for url in tqdm(urls, total=len(urls)):
    if i == 3:
        break
    
    # GET the profile data
    profile_url = url.split('/in/')[1]
    profile = api.get_profile(profile_url)

    # Write the profile data to a JSON file in the folder
    filename = '{:03d} - {:s}.json'.format(i+1, profile_url)
    with open(os.path.join(folder_name, filename), 'w') as file:
        json.dump(profile, file, indent=4)

    # Read the existing data from the JSON file
    with open(os.path.join(folder_name, filename), 'r') as file:
        data = json.load(file)

    # Update the data with contact info
    contact_info = api.get_profile_contact_info(profile_url)
    data.update(contact_info)

    # Write the updated data back to the JSON file
    with open(os.path.join(folder_name, filename), 'w') as file:
        json.dump(data, file, indent=4)

    # Move the URL from the TODO file to the DONE file
    with open(filename_TODO, 'r') as todo_file:
        lines = todo_file.readlines()
    with open(filename_TODO, 'w') as todo_file:
        for line in lines:
            if line.strip() != url:
                todo_file.write(line)
    with open(filename_DONE, 'a') as done_file:
        done_file.write(url + '\n')
        
    i = i + 1
    
# Define the name of the zip file to create
zip_filename = 'json_files.zip'

# Define the path to the folder containing the JSON files
folder_path = r'json'

# Create a new zip file
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    # Loop over all the files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Add the file to the zip archive
            zip_file.write(os.path.join(folder_path, filename), filename)

# Print a message indicating that the zip file was created
print(f'Zip file created: {zip_filename}')