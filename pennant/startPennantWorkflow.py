import csv
import json
import requests
import time

hercules_url = "https://hercules.qa2.creditsaison.xyz/api/v1"
headers = {'content-type': 'application/json', 'Authorization': 'Basic TOKEN'}

def callHercules(json_data, partner_loan_id):
    req_body = json.dumps(json_data)
    print("Calling hercules for partnerLoanId : " + partner_loan_id)
    hercules_resp = requests.post(
        hercules_url + "/partner/pennantWorkflow/start-process",
        data=req_body, headers=headers, verify=False)
    # auth=(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD))
    if hercules_resp.status_code == 200:
        print("for partner loan id : " + partner_loan_id + " hercules response  is:" + str(hercules_resp.json()))
        return True
    else:
        print("for partner loan id : " + partner_loan_id + " , hercules response:" + str(hercules_resp.content))

def create_msg_payload(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            # Read appFormID and partnerLoanId from CSV row
            app_form_id = row['app_form_id']
            utr_number = row['partner_utr_number']
            partner_loan_id = row["partner_loan_id"]
            loan_product = "KBL"

            json_data = {
                "utrNumber": utr_number,
                "appFormId": app_form_id,
                "partnerLoanId": partner_loan_id,
                "loanProduct": loan_product
            }

            print("================== Sending for partnerLoanId " +  partner_loan_id + " ================")
            callHercules(json_data, partner_loan_id)
            time.sleep(0.25)


if __name__ == '__main__':
    create_msg_payload('second10k.csv')
    print("##########")
