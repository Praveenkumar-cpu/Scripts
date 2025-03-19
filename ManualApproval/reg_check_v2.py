import requests
import json
import string

BASIC_AUTH_USERNAME = 'Un5GyOvnSbEw9Tf'
BASIC_AUTH_PASSWORD = 'eOk0c3Z87WmkujV'

HEADERS = {'content-type': 'application/json'}

def call_service(app_form_id):
    url = 'https://deadpool.creditsaison.in/api/v2/regulatoryCheck'
    body = {
    "appFormId":app_form_id
    }
    response = requests.post(auth=(BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD), url=url, headers=HEADERS,data=json.dumps(body),verify=False)
    if response.status_code == 200:
        print(response.text)
    else:
        print("failed")
        print(response.text)
        print(response)

def retry_cibil():
    filename = "/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/input_reg_check.csv"
    file1 = open(filename, "r")
    records = file1.readlines()
    data_list = []
    for i, record in enumerate(records):
        arr = record.split(",")
        app_form_id = arr[0].replace("\n","")
        call_service(app_form_id)


if __name__ == '__main__':
    retry_cibil()
