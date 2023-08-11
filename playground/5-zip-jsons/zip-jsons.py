import os
import zipfile

# Define the name of the zip file to create
zip_filename = 'json_files.zip'

# Define the path to the folder containing the JSON files
folder_path = r'C:\Users\Sadman\Pictures\Sadman\code\misc\kdit solutions - vfc\linkedin-scraper\linkedin-scraper\json'

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