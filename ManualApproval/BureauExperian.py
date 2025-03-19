import csv
import requests

# Set to store processed appForm and applicant pairs
processed_requests = set()

def hit_credit_data_api(appForm, applicant):
    # Check if the pair has already been processed
    if (appForm, applicant) in processed_requests:
        print(f"Already processed - Skipping request for AppForm: {appForm}, Applicant: {applicant}")
        print("="*30 + "\n")
        return

    url = f'https://cerebro.creditsaison.in/api/v1/appForm/{appForm}/applicant/{applicant}/creditData'
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=DDC794C1470B98B72F249699B4A02D67; JSESSIONID=1380CAFCF2B36B0C5DD3737275C76039; JSESSIONID=5C763F2C3E12F692FA64D953F895AFAA'
    }
    payload = {
        'bureauName': 'Experian'
    }

    response = requests.post(url, headers=headers, json=payload,verify = False)

    print(f"AppForm: {appForm}, Applicant: {applicant}")
    print("API Status Code:", response.status_code)
    print("API Response Text:", response.text)
    print("="*30 + "\n")

    # Add the processed pair to the set
    processed_requests.add((appForm, applicant))

# Specify the path to your CSV file
csv_file = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/bureau.csv'

# Read the CSV file and iterate through each row
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if it exists
    for row in reader:
        # Check if the row has the expected number of values
        if len(row) != 2:
            print(f"Skipping row {row} as it doesn't have the expected number of values.")
            continue

        appForm, applicant = row
        hit_credit_data_api(appForm, applicant)
