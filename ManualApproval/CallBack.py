import csv
import json
import boto3
from datetime import datetime

sqs_queue_url = 'https://sqs.ap-south-1.amazonaws.com/595588206139/events-ap-south-1.fifo'
sqs = boto3.client('sqs', region_name='ap-south-1')

def get_current_timestamp():
    return datetime.utcnow().isoformat() + 'Z'

def construct_message_body(app_form_id, partner_loan_id):
    json_data = {
        "type": "applicationStatus",
        "priority": "1",
        "entityType": "application",
        "entityId": app_form_id,
        "batchId": "",
        "partnerLoanId": partner_loan_id,
        "partnerId": "AV",
        "customerId": "",
        "workflowId": "354403987",
        "status": "15",
        "description": "appform update status",
        "timeStamp": get_current_timestamp(),
        "meta": {
            "origin": "tars-production"
        },
        "data": None,
        "userId": "",
        "reason": "Loan application has been approved.",
        "stage": ""
    }
    return json.dumps(json_data)

def insert_message_to_sqs(queue_url, csv_file_path):
    try:
        with open(csv_file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                app_form_id = row['app_form_id']
                partner_loan_id = row['partner_loan_id']

                message_body = construct_message_body(app_form_id, partner_loan_id)

                response = sqs.send_message(
                    QueueUrl=queue_url,
                    MessageBody=message_body,
                    MessageGroupId='defaultGroup',
                )

                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print(f"{app_form_id} : Message inserted successfully.")
                else:
                    print(f"{app_form_id} : Failed to insert message.")
                    print(response)

    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    insert_message_to_sqs(sqs_queue_url, 'avanti.csv')
