import csv
import requests
import json

# Define the base URL and other constants
base_url = "https://cerebro.creditsaison.in/api/v1/appForm/{appForm}/applicant/{applicant}/creditData?scope=plex"
payload = json.dumps({
    "bureauName": "Cibil"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Cookie': 'JSESSIONID=8CE9FEF3AA64A774ABA1224B8CDF0869; JSESSIONID=A50DE51FF1BDE5A8E679620D55732746'
}

# Path to the CSV file
csv_file_path = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/bureau.csv'

# Read the CSV and make API calls
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        appForm = row['appForm']
        applicant = row['applicant']

        # Format the URL with the values from the CSV
        url = base_url.format(appForm=appForm, applicant=applicant)

        try:
            # Make the API call
            response = requests.post(url, headers=headers, data=payload, verify=False)

            # Print the response for each request
            print(f"Response for appForm: {appForm}, applicant: {applicant}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            print(f"An error occurred for appForm: {appForm}, applicant: {applicant}")
            print(e)

# Note: The 'verify=False' disables SSL verification. Use this only in development or trusted environments.
# In production, ensure proper SSL certificates are configured and remove 'verify=False'.
