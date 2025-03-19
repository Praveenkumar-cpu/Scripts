import requests
from requests.auth import HTTPBasicAuth

#############################################################################################
# Prod Config Section
#############################################################################################
BASIC_AUTH_USERNAME = 'Un5GyOvnSbEw9Tf'  # replace with the username while running script
BASIC_AUTH_PSWD = 'eOk0c3Z87WmkujV'  # replace with the password while running script
update_status_url = 'https://shield.creditsaison.in/api/v1/appForm/{0}/stageStatus'
fetch_appform_url = 'https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/{0}'
#############################################################################################


update_status_payload = {'stage': 'disbursalstage', 'status': 'DISBURSAL_COMPLETE'}
headers = {'Content-Type': 'application/json'}

plid_list = [



]

not_15_status_plid = list()
execution_completed = list()
execution_failed = list()
failed_to_fetch_appForm_id = list()
for i in plid_list:
    response_get = requests.get(fetch_appform_url.format(i), auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD))
    json_response = response_get.json()
    if response_get.status_code == 200:
        if 'id' in json_response and json_response['id'] is not None:
            appform_id = json_response['id']
            if 'appFormStatus' in json_response and json_response['appFormStatus'] == '15' and json_response['stage'] != 'creditstage':
                response_put = requests.put(update_status_url.format(appform_id),
                                            auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),
                                            json=update_status_payload, headers=headers)
                print(i, "Response :", response_put.json())
                if response_get.status_code == 200:
                    execution_completed.append(i)
                else:
                    execution_failed.append(i)
            else:
                not_15_status_plid.append(i)
        else:
            failed_to_fetch_appForm_id.append(i)
    else:
        failed_to_fetch_appForm_id.append(i)

print("======================================================")
print("Status updated for PLIDs \n", execution_completed)
print("======================================================")
print("Status update gave not 200 response for PLIDs \n", execution_failed)
print("=======================================================")
print("Status is not 15 for the PLIDs \n", not_15_status_plid)
print("========================================================")
print("Failed to fetch appForm Id from shield for PLIDs \n", failed_to_fetch_appForm_id)
