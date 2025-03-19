# this script will help when operation team say docs not reflecting add partner id here and run
# docs will reflect in jarvis

import requests

def hit_partner_loan_api(partner_loan_id):
    url = f'https://drstrange.creditsaison.in/api/v1/partnerLoan/{partner_loan_id}/dms/tagging'
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Cookie': 'JSESSIONID=51A083167344F533419FD517BD2FA2B7; JSESSIONID=30699E97ECADA4216C023E6D666D8416; JSESSIONID=194E00E429D6762B81510A67CA483C7D'
    }

    response = requests.post(url, headers=headers,verify = False)

    return response

# List of partner loan IDs
partner_loan_ids = [
"KSF_CRED_PROD_4533544",
"KSF_CRED_PROD_3424725",
"KSF_CRED_PROD_5019407",
"KSF_CRED_PROD_29425455",
"KSF_CRED_PROD_16825465",
"KSF_CRED_PROD_46275392",
"KSF_CRED_PROD_16095909",
"KSF_CRED_PROD_11989761",
"KSF_CRED_PROD_44420394",
"KSF_CRED_PROD_13020363"
]
# Lists to store successful and unsuccessful partner loan requests
successful_requests = []
unsuccessful_requests = []

# Iterate through the partner loan IDs and hit the Partner Loan API for each ID
for partner_loan_id in partner_loan_ids:
    partner_loan_response = hit_partner_loan_api(partner_loan_id)

    # Print the response for each partner loan ID
    print(f"Partner Loan ID: {partner_loan_id}")
    print("Partner Loan API Status Code:", partner_loan_response.status_code)
    print("Partner Loan API Response Text:", partner_loan_response.text)
    print("\n" + "="*30 + "\n")  # Separate each API request for better visibility

    # Check success and update the lists
    if partner_loan_response.status_code == 200:
        successful_requests.append(partner_loan_id)
    else:
        unsuccessful_requests.append(partner_loan_id)

# Print lists of successful and unsuccessful partner loan requests
print("\n\nSuccessful Partner Loan Requests:")
for partner_loan_id in successful_requests:
    print(f"Partner Loan ID: {partner_loan_id}")

print("\nUnsuccessful Partner Loan Requests:")
for partner_loan_id in unsuccessful_requests:
    print(f"Partner Loan ID: {partner_loan_id}")
