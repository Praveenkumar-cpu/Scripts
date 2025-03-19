import requests
import json

def send_patch_requests(appFormIds, partnerUtrNumbers):
    url = "https://xmen.creditsaison.in/api/v1/loan"
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg',
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=13FAD97A71D23492F4E31AB33609CAF4'
    }
    for appFormId, partnerUtrNumber in zip(appFormIds, partnerUtrNumbers):
        payload = json.dumps({
            "appFormId": appFormId,
            "partnerUtrNumber": partnerUtrNumber
        })
        response = requests.patch(url, headers=headers, data=payload)
        print(f"Response for appFormId {appFormId} and partnerUtrNumber {partnerUtrNumber}:")
        if response.status_code >= 200 and response.status_code < 300:
            print("Success")
        else:
            print("Failure")
        print()

# Example usage:
appFormIds = [
"975c9d7a-4e0b-4210-87d7-1b119c89cd2a",
"7bbff680-39c2-4387-95b1-f1d7a847e623",
"efbf84c2-7c5d-4278-b550-ba4e08726b44",
"6c5b60ca-d509-4bd7-a819-0ab43f5ad0af",
"49f8056d-1758-40f2-afc5-9c6a8fb768b5",
"25eb1aba-fbf1-46a9-97ff-079cac5929d6",
"be008d79-fbf0-4dd4-8ab4-fb33f5fb1b66",
"3b56fe45-0a04-4693-834f-8a300b23f2c6",
"1f66f1b6-3b95-49da-ba96-dd98449048f7",
"d9a2d153-5947-45c7-9b4f-5e5fb65b6621",
"4c2024a4-20bd-4970-8ff1-8d603981fe6d",
"8d8ec704-88ba-426f-906c-515d60af40fb",
"949157a1-63b6-460a-9b9f-6791ab380059",
"5863b7e3-6456-43c6-a49c-ecfe7ed5073d",
"049211d8-31e6-4ac7-8f1b-04a48a1d9373",
"7daff978-e82e-43e4-8d61-713ce691b1ba",
"b3a33b24-2231-40e6-9ed1-6c18d4a84c02",
"f062e8df-9f1a-4715-b71e-fe55df57e24e"
]
partnerUtrNumbers = [
 "AXISCN0611563554",
             "AXISCN0612581989",
             "AXISCN0612677120",
             "AXISCN0612685733",
             "AXISCN0612685743",
             "AXISCN0612685752",
             "AXISCN0612685804",
             "AXISCN0612685868",
             "AXISCN0612686084",
             "AXISCN0612687400",
             "AXISCN0612687407",
             "AXISCN0612687538",
             "AXISCN0612687577",
             "AXISCN0612688970",
             "CB0047306209",
             "AXISCN0613920216",
             "AXISCN0614035450",
           "AXISCN0617234523"
]

send_patch_requests(appFormIds, partnerUtrNumbers)


verification sttsu -1


import requests
import csv

# Specify the path to your CSV file
csv_file = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/Verification.csv'

# Lists to keep track of results
successes = []
errors_status_minus_one = []
errors_other = []

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
            if status == -1:
                errors_status_minus_one.append((partner_loan_id, app_form_id, status))
            else:
                successes.append((partner_loan_id, app_form_id, status))
            print(f"Partner Loan ID: {partner_loan_id}, App Form ID: {app_form_id}, Status: {status}")
        else:
            errors_other.append((partner_loan_id, app_form_id, response.status_code, response.text))
            print(f"Error for Partner Loan ID {partner_loan_id}, App Form ID {app_form_id}: {response.status_code}, {response.text}")

# Summary of results
print("\n--- Summary ---")
print(f"Successful requests: {len(successes)}")
for loan_id, app_id, status in successes:
    print(f" - Partner Loan ID: {loan_id}, App Form ID: {app_id}, Status: {status}")

print(f"\nRequests with status -1: {len(errors_status_minus_one)}")
for loan_id, app_id, status in errors_status_minus_one:
    print(f" - Partner Loan ID: {loan_id}, App Form ID: {app_id}, Status: {status}")

print(f"\nOther Errors: {len(errors_other)}")
for loan_id, app_id, status_code, message in errors_other:
    print(f" - Partner Loan ID: {loan_id}, App Form ID: {app_id} (Status Code: {status_code}, Message: {message})")



