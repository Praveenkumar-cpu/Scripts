import requests
import json

# List of partner loan IDs to query
partner_loan_ids = [

]

# API URL with a placeholder for the loan ID
url_template = "https://xmen.creditsaison.in/api/v1/loan/partnerLoanIds?partnerLoanId={}"

# Headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Cookie': 'JSESSIONID=55A4D8F135E39581A0F52FB46D7D7381; JSESSIONID=256812AEFB177129E8BFBA6C3A282E1D'
}

# Dictionary to store responses
responses = {}

# Loop through each partner loan ID
for loan_id in partner_loan_ids:
    # Format the URL with the current loan ID
    url = url_template.format(loan_id)

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Attempt to parse the response as JSON
    try:
        response_data = response.json()
    except json.JSONDecodeError:
        response_data = None

    # Store the response text in the dictionary
    responses[loan_id] = response_data

# Print all responses
print("All responses:")
for loan_id, response_data in responses.items():
    print(f"Response for loan ID {loan_id}:")
    print(json.dumps(response_data, indent=4))
    print()

# Determine which responses are NULL or empty
null_or_empty_responses = [loan_id for loan_id, response_data in responses.items() if response_data is None or response_data == {}]

# Print out the partner loan IDs with NULL or empty responses
print("Partner Loan IDs with NULL or empty responses:")
for loan_id in null_or_empty_responses:
    print(loan_id)

