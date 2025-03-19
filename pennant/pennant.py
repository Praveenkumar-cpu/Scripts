import time
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

#############################################################################################
# Prod Config Section
#############################################################################################
BASIC_AUTH_USERNAME = 'Un5GyOvnSbEw9Tf'  # replace with the username while running script
BASIC_AUTH_PSWD = 'eOk0c3Z87WmkujV'  # replace with the password while running script
headers = {'content-type': 'application/json'}
get_plex_workflow = 'https://hercules.creditsaison.in/api/v1/process/resource/{plid}/logs'
get_plex_pending_task = 'https://hercules.creditsaison.in/api/v1/process/{workflowId}/pending'
post_plex_resume = 'https://hercules.creditsaison.in/api/v1/process/{workflowId}/resume'
# Comment above plex resume and uncomment below plex resume when resuming for pony
# post_plex_resume = 'https://pony.creditsaison.in/api/v1/postFinalOffer/{workflowId}/resume'
#############################################################################################

# Put the PLIDs in plid list variable
plid_list = [
"LAI1009748748",
"CASKB250317WMDCZ",
"CASKB250317GNMCM",
"LAI1009750554",
"1000824145",
"1000824126",
"KSF_CRED_PROD_54275220_186448171",
"KSF_CRED_PROD_2341842_186449992",
"KSF_CRED_PROD_10901055_186554984",
"KSF_CRED_PROD_7036185_186628430",
"KSF_CRED_PROD_547274_186685774",
"KSF_CRED_PROD_13327196_186699830",
"BPL0203257493919"
]
failed_plid = []
pending_list = []
failed_to_check_status = []
reason = []
exception_cases = dict()

pennant_task = ['CreateLoanInXmen','CreateLoanInPennant', 'CreateCustomer','UpdateCif','UpdateLoanInPennant','ExposureCalculation','StartDisbursalTrigger','UpdateLoanInPennantUnc']
end_task = ["EndWorkflow", "EndWorkflowAndSendCallback"]

def get_pending_task(plid):
    response_workflow = requests.get(get_plex_workflow.format(plid=plid),
                                     auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD), verify=False)
    if response_workflow.status_code != 200:
        failed_plid.append(plid)
        return
    workflow_response = response_workflow.json()
    workflow_id = workflow_response['workflowId']
    last_task = workflow_response['stateAndLogs'][-1]['taskName']
    if workflow_response['stateAndLogs'][-1]['taskName'] in end_task:
        return
    response_pending = requests.get(get_plex_pending_task.format(workflowId=workflow_id),
                                    auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),verify=False)
    if response_pending.status_code != 200:
        failed_plid.append(plid)
        return
    pending_response = response_pending.json()
    pending_task = pending_response['taskList'][0]['taskName']
    if last_task in pennant_task and pending_task in pennant_task and last_task == pending_task:
        params = {'taskName': pending_task}
        response_resume = requests.post(post_plex_resume.format(workflowId=workflow_id),
                                        auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),verify=False,
                                        params=params, json={}, headers=headers)
        if response_resume.status_code != 200:
            failed_plid.append(plid)
    else:
        failed_plid.append(plid)

def run_script(plid_list):
    for plid in plid_list:
        try:
            print("Working on ", plid)
            get_pending_task(plid)
            time.sleep(0.1)  # Sleep for 0.5 seconds to avoid bombarding the server
        except Exception as e:
            if plid not in failed_plid:
                exception_cases[plid] = repr(e)

    print("Waiting for 30 seconds\n\n")
    time.sleep(30)
    print("Checking Final Status of resumed cases in Plex")

    for plid in plid_list:
        try:
            print("Working on ", plid)
            if plid not in failed_plid and plid not in exception_cases:
                response_get = requests.get(get_plex_workflow.format(plid=plid),
                                            auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),verify=False)
                if response_get.status_code != 200:
                    failed_to_check_status.append(plid)
                else:
                    response_body = response_get.json()
                    if response_body['stateAndLogs'][-1]['taskName'] not in end_task:
                        pending_list.append(plid)
                        reason.append(response_body['stateAndLogs'][-1]['logs'][0]['response']['message'])
            time.sleep(0.1)  # Sleep for 0.5 seconds to avoid bombarding the server
        except Exception as e:
            print("Error occurred for ", plid)
            exception_cases[plid] = repr(e)

    print("Please Check, Failed Plids", failed_plid)
    print("\n==========================================================\n")
    print("Please Check, Resumed but workflow not completed", pending_list)
    print("\n===========================================================\n")
    print("Please Check, Failed to Fetch Workflow Status after resuming", failed_to_check_status)
    print("\n=============================================================\n")
    print("Please Check, These PLID's are in Pending State", exception_cases)
    print("\n\nCreating Files for failed_plid, pending_plid, failed_to_check_status, pending_list, exception_case")

    if (len(failed_plid) == 0 and len(pending_list) == 0 and len(failed_to_check_status) == 0
            and len(exception_cases) == 0):
        print("All cases were resumed successfully")
    else:
        if len(failed_plid) != 0:
            pd.DataFrame({'Failed_Execution_PLID': failed_plid}).to_csv('Failed_Execution_PLID.csv')
        if len(pending_list) != 0:
            pd.DataFrame({'Pending_PLID': pending_list, 'response': reason}).to_csv('Pending_PLID.csv')
        if len(failed_to_check_status) != 0:
            pd.DataFrame({'Failed_to_check_status_PLID': failed_to_check_status}).to_csv('Failed_to_check_status_PLID.csv')
        if len(exception_cases) != 0:
            exception_df = pd.DataFrame(list(exception_cases.items()), columns=['PLID', 'Exception_Message'])
            exception_df.to_csv('Exception_PLID.csv', index=False)
        print("Files have been Created")

def run_resume_hercules(plids):
    run_script(list(set(plids)))

def main():
    run_script(list(set(plid_list)))

if __name__ == "__main__":
    main()


