import requests
import json

headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Content-Type': 'application/json',
}

def send_callback(payload):
    url = "https://thor.creditsaison.in/api/v1/notification/preProcessor/send"
    return requests.request("POST", url, headers=headers, data=payload)

def get_data_from_api(partner_loan_id):
    url = f"https://chronos.creditsaison.in/api/v1/events?partnerLoanId={partner_loan_id}"
    return requests.request("GET", url, headers=headers)

def create_payload(data):
    result = data.get("result", [])

    if not result:
        print("No withdrawal instructions found in the API response.")
        return None

    # Assuming only the first withdrawal instruction is relevant
    withdrawal_instruction = result[0]

    entity_id = withdrawal_instruction.get("entityId")
    withdrawal_id = withdrawal_instruction["data"].get("withdrawalId")

    if entity_id is None or withdrawal_id is None:
        print("Failed to find entityId or withdrawalId in the withdrawal instruction.")
        return None

    payload = {
        "entityId": entity_id,
        "partnerId": withdrawal_instruction.get("partnerId", ""),
        "partnerLoanId": withdrawal_instruction.get("partnerLoanId", ""),
        "lpc": "ESC",
        "scenarioName": "withdrawalInstruction",
        "entityType": "application",
        "notificationType": "instant",
        "recipientName": "Partner",
        "isTemplate": False,
        "message": {
            "content": withdrawal_instruction.get("description", ""),
            "subject": "withdrawalInstruction",
            "target": {
                "CALLBACK": []
            }
        },
        "data": {
            "withdrawalId": withdrawal_id,
            "status": withdrawal_instruction.get("status", "")
        },
        "attachments": [],
        "scheduledTime": []
    }
    return json.dumps(payload)

def process_partner_loan_id(partner_loan_id):
    response = get_data_from_api(partner_loan_id)
    if response.status_code == 200:
        data = response.json()
        payload = create_payload(data)
        if payload:
            response_post = send_callback(payload)
            if response_post.status_code == 200:
                print(f"Callback sent successfully for partnerLoanId: {partner_loan_id}")
            else:
                print(f"Failed to send callback for partnerLoanId: {partner_loan_id}, Status code: {response_post.status_code}")
        else:
            print(f"Failed to create payload for partnerLoanId: {partner_loan_id}")
    else:
        print(f"Failed to fetch data for partnerLoanId: {partner_loan_id}, Status code: {response.status_code}")

partner_loan_ids = [


]

for partner_loan_id in partner_loan_ids:
    process_partner_loan_id(partner_loan_id)
