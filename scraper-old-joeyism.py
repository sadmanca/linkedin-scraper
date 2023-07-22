from linkedin_scraper import Person, actions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import csv
import json

# driver_loc = 'C:/Users/Sadman/Pictures/Sadman/code/misc/kdit solutions - vfc/linkedin-scraper/chromedriver.exe'

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

email = "***REMOVED***"
password = "***REMOVED***"
actions.login(driver, email, password)

print("LOGGED IN ---------------------------------------------------")

person = Person("https://www.linkedin.com/in/khushi-thakkar-906b56188/", driver=driver, scrape=False)
person.scrape(close_on_complete=False)

print(person)

# Define the headers for the CSV file
headers = ['Name', 'LinkedIn URL', 'Contact Info', 'Latest Experience Position Description', 'Latest Experience Position Title', 'All Other Info']

# Define the data to be written to the CSV file
data = [
    [
        person.name,
        person.linkedin_url,
        person.contacts,
        person.experiences[0].description,
        person.experiences[0].position_title,
        json.dumps(person.__dict__)
    ]
]

# Write the data to the CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)