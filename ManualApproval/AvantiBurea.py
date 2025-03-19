import requests
import json

# Function to get data from the GET API
def get_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for URL {url}: {response.status_code}")
        return None

# Function to post data to the POST API
def post_data(url, headers, payload):
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Data posted successfully.")
        print(response.text)
    else:
        print(f"Failed to post data: {response.status_code}")
        print(response.text)

# GET API URL template and headers
get_url_template = "https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/{}"
get_headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Cookie': 'JSESSIONID=98D751576936C56F9A03F73B8B3D9E6D; JSESSIONID=518FA58588517435759E2AC9C2615923; JSESSIONID=C8D8435BCE2C14B56E8739ED92CB0430'
}

# POST API URL and headers
post_url = "https://cerebro.creditsaison.in/api/v1/bureauFile/upload"
post_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Cookie': 'JSESSIONID=40F04771CFEA4CC18D45A15BC3DB391F'
}

# Example payload template
payload_template = {
    "bureauName": "Crif",
    "bureauFileName": "bureau_report.xml",
    "creditDataPullType": "HARD_PULL",
    "parsingNeededFlag": False
}

# List of partnerLoanIds
partnerLoanIds = [

"AVNKSF55100124694598"
]

# Iterate over each partnerLoanId
for partnerLoanId in partnerLoanIds:
    # Construct the GET URL
    get_url = get_url_template.format(partnerLoanId)

    # Get data from the GET API
    data = get_data(get_url, get_headers)

    if data:
        # Extract necessary fields
        appFormId = data.get('id')
        linked_individual = data.get('linkedIndividuals', [])[0]
        applicantId = linked_individual.get('id')

        # Construct docsUrl
        base_url = "https://s3.ap-south-1.amazonaws.com/unorganizedbucket-production-595588206139-ap-south-1/zipFiles/"
        docsUrl = f"{base_url}{partnerLoanId}.zip"

        # Prepare payload for the POST API using the template
        payload = payload_template.copy()
        payload["appFormId"] = appFormId
        payload["applicantId"] = applicantId
        payload["docsUrl"] = docsUrl

        # Post data to the POST API
        post_data(post_url, post_headers, payload)
