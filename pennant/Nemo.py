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
get_plex_workflow = 'https://nemo.creditsaison.in/api/v1/process/resource/{plid}/logs'
get_plex_pending_task = 'https://nemo.creditsaison.in/api/v1/process/{workflowId}/pending'
post_plex_resume = 'https://nemo.creditsaison.in/api/v1/process/{workflowId}/resume'
# Comment above plex resume and uncomment below plex resume when resuming for pony
# post_plex_resume = 'https://pony.creditsaison.in/api/v1/postFinalOffer/{workflowId}/resume'
#############################################################################################

# Put the PLIDs in plid list variable
plid_list = [
"CASKB250302PFSAR",
"CASKB250227AFSWG",
"CASKB250205KZTKN",
"CASKB250304JOOAA",
"CASKB250304XXHSF",
"CASKB250205YBDRN",
"CASKB250205KZTKN",
"CASKB250317HZSAF",
"CASKB240710OSTAA",
"CASKB250317QKNWP",
"CASKB250205YBDRN",
"CASKB250303YYXLU",
"CASKB240710OSTAA",
"CASKB250312JAPDI",
"CASKB240710OSTAA",
"CASKB250205YBDRN",
"CASKB250205KZTKN",
"CASKB250205YBDRN",
"CASKB250205KZTKN",
"CASKB250311GAPIB",
"CASKB250310KUJOO",
"CASKB250311QSTGL",
"CASKB250311GAPIB",
"CASKB250311QSTGL",
"CASKB250313KCGPK",
"CASKB250313YDNWW",
"CASKB250317HZSAF",
"MV246367930047",
"1450081251",
"1450081251",
"CASKB250316ELPAM",
"CASKB250309IDQQT",
"CASKB250309BPRZT",
"CASKB250309GYJGE",
"CASKB250309QCJTO",
"CASKB250309YOGBP",
"CASKB250309ARPGH",
"CASKB250309SHJFC",
"CASKB250309YPQME",
"CASKB250313BQQQL",
"CASKB250313JMWSY",
"CASKB250313WIGKJ",
"CASKB250316WUTMA",
"CASKB250313LAXYQ",
"CASKB250313ZAFVX",
"CASKB250317QKNWP",
"CASKB250313ZAFVX",
"CASKB250316LANZW",
"CASKB250313YCPJB",
"CASKB250313EOEHO",
"CASKB250313NTZOO",
"MV255249368544",
"CASKB250313ZAFVX",
"CASKB250313LAXYQ",
"CASKB250313YDNWW",
"CASKB250313SHKWD",
"CASKB250313NHBYG",
"CASKB250313NGWCS",
"CASKB250313ASNXJ",
"CASKB250313KQIBP",
"CASKB250313MDBPA",
"CASKB250313FHWEE",
"CASKB250316TXTYY",
"PRP0846085906",
"CASKB250313RIMTW",
"CASKB250313BTYNR",
"CASKB250313PQOXF",
"CASKB250312QLJFH",
"CASKB250313CMZVL",
"CASKB250313EEEFF",
"CASKB250313TBQTC",
"CASKB250313ZRYVS",
"CASKB250313GPXGT",
"CASKB250313VGSMQ",
"CASKB250313SOIJS",
"CASKB250309ZSLRQ",
"CASKB250305ZREUS",
"CASKB250305ODUGN",
"CASKB250227AFSWG",
"CASKB250205YBDRN",
"CASKB250205KZTKN",
"CASKB250227AFSWG",
"CASKB250205YBDRN",
"CASKB250205KZTKN",
"CASKB250314LSLWS",
"CASKB250314LSLWS",
"CASKB250302PFSAR",
"CASKB250302PFSAR",
"CASKB250314IMZFK",
"CASKB250303YYXLU",
"CASKB250303YYXLU",
"JPLd7833ba6a6c0482c9b59",
"CASKB250304JOOAA",
"CASKB250304JOOAA",
"CASKB250304XXHSF",
"CASKB250304XXHSF",
"CASKB250315UZBSW",
"1462452909",
"JPLd7833ba6a6c0482c9b59"
]

failed_plid = []
pending_list = []
failed_to_check_status = []
reason = []
exception_cases = dict()


def get_pending_task(plid):
    response_workflow = requests.get(
        get_plex_workflow.format(plid=plid),
        auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),
        verify=False
    )
    if response_workflow.status_code != 200:
        failed_plid.append(plid)
        return
    workflow_response = response_workflow.json()
    workflow_id = workflow_response['workflowId']
    last_task = workflow_response['stateAndLogs'][-1]['taskName']

    response_pending = requests.get(
        get_plex_pending_task.format(workflowId=workflow_id),
        auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),
        verify=False
    )
    if response_pending.status_code != 200:
        failed_plid.append(plid)
        return
    pending_response = response_pending.json()
    if pending_response['taskList']:
        pending_task = pending_response['taskList'][0]['taskName']
        # Resume the pending task
        params = {'taskName': pending_task}
        response_resume = requests.post(
            post_plex_resume.format(workflowId=workflow_id),
            auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),
            params=params, json={}, headers=headers, verify=False
        )
        if response_resume.status_code != 200:
            failed_plid.append(plid)
    else:
        # No pending tasks found, but the PLID might need to be reviewed.
        failed_plid.append(plid)


def run_script(plid_list):
    for plid in plid_list:
        try:
            print("Working on ", plid)
            get_pending_task(plid)
        except Exception as e:
            if plid not in failed_plid:
                exception_cases[plid] = repr(e)

    print("Waiting for 30 seconds\n\n")
    time.sleep(30)
    print("Checking Final Status of resumed cases in Plex")

    for plid in plid_list:
        try:
            if plid not in failed_plid and plid not in exception_cases:
                response_get = requests.get(
                    get_plex_workflow.format(plid=plid),
                    auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD),
                    verify=False
                )
                if response_get.status_code != 200:
                    failed_to_check_status.append(plid)
                else:
                    response_body = response_get.json()
                    # Check if workflow is not completed
                    if response_body['stateAndLogs'][-1]['taskName'] not in ["EndWorkflow", "EndWorkflowAndSendCallback"]:
                        pending_list.append(plid)
                        reason.append(response_body['stateAndLogs'][-1]['logs'][0]['response']['message'])
                    else:
                        reason.append('')  # Ensure reason list has an entry even if no pending task is found
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
            # Ensure that the 'reason' list is of the same length as 'pending_list'
            if len(pending_list) > len(reason):
                reason.extend([''] * (len(pending_list) - len(reason)))
            pd.DataFrame({'Pending_PLID': pending_list, 'response': reason}).to_csv('Pending_PLID.csv')
        if len(failed_to_check_status) != 0:
            pd.DataFrame({'Failed_to_check_status_PLID': failed_to_check_status}).to_csv('Failed_to_check_status_PLID.csv')
        if len(exception_cases) != 0:
            pd.DataFrame.from_dict(exception_cases, orient='index', columns=['Exception']).to_csv('Exception_PLID.csv')

        print("Files have been Created")


def run_resume_hercules(plids):
    run_script(list(set(plids)))


def main():
    run_script(list(set(plid_list)))


if __name__ == "__main__":
    main()
