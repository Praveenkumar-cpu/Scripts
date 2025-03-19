import requests
import csv

# Specify the path to your CSV file
csv_file = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/Verification.csv'
# Read the CSV file and iterate through each row
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        partner_loan_id = row['partner_loan_id']
        app_form_id = row['app_form_id']

        url = f'https://hulk.creditsaison.in/api/v1/appForm/{app_form_id}/verify'

        headers = {
            'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
            'Cookie': 'JSESSIONID=C6783D184A2B2B698291FD74453C1495; JSESSIONID=57527A94D095CA1B6B1AC6FA61D08DD0'
        }

        response = requests.get(url, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            app_form_data = response.json()
            status = app_form_data.get('status', None)
            print(f"Partner Loan ID: {partner_loan_id}, App Form ID: {app_form_id}, Status: {status}")
        else:
            print(f"Error for Partner Loan ID {partner_loan_id}, App Form ID {app_form_id}:", response.status_code, response.text)