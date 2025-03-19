import requests
import json

# API headers
headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Cookie': 'JSESSIONID=98D751576936C56F9A03F73B8B3D9E6D; JSESSIONID=6F509A64FE83F7C804F707B924D12E81'
}

# List of partner loan IDs to check
partner_loan_ids = [


]

# Initialize an empty list to store partner loan IDs with appFormStatus != 15
filtered_loan_ids = []

# Loop through each partner loan ID and fetch the response
for loan_id in partner_loan_ids:
    try:
        url = f"https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/{loan_id}"
        response = requests.get(url, headers=headers,verify=False)

        # Check if the request was successful
        if response.status_code == 200:
            parsed_res = response.json()  # Parse the JSON response

            # Check if 'appFormStatus' exists and if it's not 15
            if 'appFormStatus' in parsed_res and parsed_res['appFormStatus'] != 15:
                filtered_loan_ids.append(loan_id)
        else:
            print(f"Failed to fetch loan ID {loan_id}: Status Code {response.status_code}")

    except Exception as e:
        print(f"Error fetching loan ID {loan_id}: {e}")

# Print the list of partner loan IDs where appFormStatus is not 15
print("Partner Loan IDs with appFormStatus != 15:", filtered_loan_ids)
