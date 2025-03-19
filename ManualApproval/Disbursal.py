import requests
import json

headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
}


def get_real_time_wf_history(partner_loan_id):
    url = "https://hercules.creditsaison.in/api/v1/process/resource/" + partner_loan_id + "/history?onlyTasks=true"
    response = requests.request("GET", url, headers=headers, data=None)
    return response


def get_app_form(partner_loan_id):
    url = "https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/" + partner_loan_id
    response = requests.request("GET", url, headers=headers, data=None)
    return response


def resume_task(process_id):
    url = "https://hercules.creditsaison.in/api/v1/process/" + process_id + "/resume?taskName=StartDisbursalTrigger"
    response = requests.request("POST", url, headers=headers, data=json.dumps({}))
    return response


already_disbursal_completed_partner_loan_id = list()
pending_pre_approved_partner_loan_id = list()
resumed_partner_loan_id = list()
failed_resumed_partner_loan_id = list()
other_status_partner_loan_id = list()


def resume_hercules_task(partner_loan_ids):
    for partnerLoanId in partner_loan_ids:
        res = get_real_time_wf_history(partnerLoanId)
        if res.status_code == 200:
            res_data = json.loads(res.content)
            last_executed_task = res_data['taskList'][-1]['taskName']
            workflowId = str(res_data['workflowId'])
            print('\nPartner Loan Id: ' + partnerLoanId + ' | Last Executed task: ' + last_executed_task)
            if res_data['status'] == 'f' and last_executed_task == 'StartDisbursalTrigger':
                res2 = resume_task(workflowId)
                if res2.status_code == 200:
                    print('Partner Loan Id: ' + partnerLoanId + ' | Resumed Successfully')
                    resumed_partner_loan_id.append(partnerLoanId)
                else:
                    print('Partner Loan Id: ' + partnerLoanId + ' | Failed to resume')
                    failed_resumed_partner_loan_id.append(partnerLoanId)
            elif last_executed_task == 'EndWorkflow':
                already_disbursal_completed_partner_loan_id.append(partnerLoanId)
            else:
                other_status_partner_loan_id.append(partnerLoanId)
        else:
            pending_pre_approved_partner_loan_id.append(partnerLoanId)
            print("Failed to get History | partner Loan Id: " + partnerLoanId)


partnerLoanIds = ['MV114967345787']

resume_hercules_task(partnerLoanIds)

print('\n\nDisbursal Already Completed Partner Loan Ids: ' + str(already_disbursal_completed_partner_loan_id))
print('Disbursal Resumed Partner Loan Ids: ' + str(resumed_partner_loan_id))
print('Disbursal Failed Partner Loan Ids: ' + str(failed_resumed_partner_loan_id))
print('Disbursal Other Status Partner Loan Ids: ' + str(other_status_partner_loan_id))
