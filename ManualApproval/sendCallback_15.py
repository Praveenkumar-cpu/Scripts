import requests
import json
import subprocess

# Start caffeinate to prevent sleep
caffeinate_process = subprocess.Popen(['caffeinate', '-i'])

headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Content-Type': 'application/json',
}

def send_call_back(payload):
    url = "https://thor.creditsaison.in/api/v1/notification/preProcessor/send"
    return requests.post(url, headers=headers, data=payload, verify = False)

def get_shield_app_form(partner_loan_id):
    url = f"https://shield.creditsaison.in/api/v1/partnerLoanId/{partner_loan_id}/selective?details=appFormBasic"
    return requests.get(url, headers=headers,verify = False)

def get_payload(shield_res):
    return json.dumps({
        "entityId": shield_res["id"],
        "partnerId": shield_res["partnerId"],
        "partnerLoanId": shield_res["partnerLoanId"],
        "lpc": shield_res["loanProduct"],
        "scenarioName": "applicationStatus",
        "entityType": "application",
        "notificationType": "instant",
        "recipientName": "Partner",
        "isTemplate": False,
        "message": {
            "content": "Loan application has been approved.",
            "subject": "applicationStatus",
            "target": {
                "CALLBACK": []
            }
        },
        "data": {
            "status": "15"
        },
        "attachments": [],
        "scheduledTime": []
    })

def start_sending_callback(partner_loan_id):
    response = get_shield_app_form(partner_loan_id)
    if response.status_code == 200:
        payload = get_payload(response.json())
        response = send_call_back(payload)
        if response.status_code == 200:
            print(f"Callback Sent | partnerLoanId: {partner_loan_id}")
        else:
            print(f"Failed to Send Callback | partnerLoanId: {partner_loan_id}")
    else:
        print(f"Failed to get appForm | partnerLoanId: {partner_loan_id}")

partner_loan_ids = [
"1462489517"

]
for partner_loan_id in partner_loan_ids:
    start_sending_callback(partner_loan_id)

# Stop caffeinate when done
caffeinate_process.terminate()
