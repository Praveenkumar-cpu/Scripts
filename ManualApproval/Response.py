import requests

# List of partner loan IDs
partner_loan_ids = [
    "1444702821",
    "1448612828",
    "1429683288",
    "1437189624"
]

# Base URL for the API
base_url = "https://thor.creditsaison.in/api/v2/callback?partnerId=ES&partnerLoanId={}"

# Headers for the request
headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Content-Type': 'application/json',
    'Cookie': 'JSESSIONID=A396EAAE8983BE16F0199B0CEDB64CB9; JSESSIONID=BEAF7F723D1D537AC0CB5E0FF02DDAAB; JSESSIONID=7B8C5F19243DFDC80E1A9B00B00A73ED'
}

# Function to fetch data for a given partner loan ID
def fetch_data(partner_loan_id):
    url = base_url.format(partner_loan_id)
    response = requests.get(url, headers=headers, verify=False)  # Added verify=False here
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Open the output file to write data
with open("response_data.txt", "w") as file:
    # Loop through each partner loan ID and fetch the data
    for partner_loan_id in partner_loan_ids:
        data = fetch_data(partner_loan_id)
        # Write the response data to the file
        file.write(f"Data for Partner Loan ID {partner_loan_id}:\n")
        file.write(f"{data}\n\n")  # Add two newlines for better readability

print("Response data has been written to 'response_data.txt'.")
