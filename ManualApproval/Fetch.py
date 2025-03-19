import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Suppress the SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASIC_AUTH_USERNAME = 'Un5GyOvnSbEw9Tf'
BASIC_AUTH_PSWD = 'eOk0c3Z87WmkujV'
fetch_appform_url = 'https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/{0}'

plid_list = [
"KSF_CRED_PROD_43271415",
"KSF_CRED_PROD_36844998",
"KSF_CRED_PROD_3950651",
"KSF_CRED_PROD_13237313",
"KSF_CRED_PROD_27308054",
"KSF_CRED_PROD_18547210",
"KSF_CRED_PROD_5842603",
"KSF_CRED_PROD_43345148",
"KSF_CRED_PROD_39736442",
"KSF_CRED_PROD_47448016",
"KSF_CRED_PROD_5603046",
"KSF_CRED_PROD_7702288",
"KSF_CRED_PROD_9705242",
"KSF_CRED_PROD_4515873",
"KSF_CRED_PROD_28578988",
"KSF_CRED_PROD_2447103",
"KSF_CRED_PROD_34347235",
"KSF_CRED_PROD_20449395",
"KSF_CRED_PROD_3711385",
"KSF_CRED_PROD_16582438",
"KSF_CRED_PROD_3303908",
"KSF_CRED_PROD_41854315",
"KSF_CRED_PROD_34707738",
"KSF_CRED_PROD_11247776",
"KSF_CRED_PROD_4200134",
"KSF_CRED_PROD_17315467",
"KSF_CRED_PROD_24380750",
"KSF_CRED_PROD_18892783",
"KSF_CRED_PROD_2263799",
"KSF_CRED_PROD_21109331",
"KSF_CRED_PROD_3407672",
"KSF_CRED_PROD_51821979",
"KSF_CRED_PROD_38430396",
"KSF_CRED_PROD_17840792",
"KSF_CRED_PROD_13755356",
"KSF_CRED_PROD_24819609",
"KSF_CRED_PROD_39423898",
"KSF_CRED_PROD_17578680",
"KSF_CRED_PROD_26860252",
"KSF_CRED_PROD_32486441",
"KSF_CRED_PROD_26603245",
"KSF_CRED_PROD_31768035",
"KSF_CRED_PROD_6211690",
"KSF_CRED_PROD_4308058",
"KSF_CRED_PROD_45195976",
"KSF_CRED_PROD_41986026",
"KSF_CRED_PROD_13859430",
"KSF_CRED_PROD_38537337",
"KSF_CRED_PROD_12636041"
]

for i in plid_list:
    response_get = requests.get(fetch_appform_url.format(i),
                                auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),
                                verify=False)  # Disable SSL verification
    json_response = response_get.json()

    # Extracting values
    app_id = str(json_response.get('id', ''))  # Convert app_id to string, default to empty string if None
    linked_individuals = json_response.get('linkedIndividuals', [])

    # Prepare a list to store linked individual IDs
    linked_individual_ids = []

    # Collect linkedIndividuals IDs
    for individual in linked_individuals:
        linked_individual_id = str(individual.get('id', None))  # Convert ID to string
        linked_individual_ids.append(linked_individual_id)

    # Print the appform id and applicant id
    print(f"Appform ID: {app_id}, Applicant IDs: {', '.join(linked_individual_ids)}")
