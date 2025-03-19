# Use this athena query to fetch the csv from athen and paster in pennant folder with name bank-details.csv
# Replace partnerLoanId1 etc with partnerloanIds
# Remove # when using query
# -- Athena Query for fetching appformId, partnerloanId, applicantId and BankAccount from mrBurns and shield
# WITH LatestTimestamps AS (
#     SELECT partner_loan_id,
#            MAX(time_stamp) AS latest_timestamp
#     FROM "partitioned_datalake_production_ap_south_1"."mrburns_withdrawal"
#     WHERE partner_loan_id IN (
#         'partnerLoanId1',
#         'partnerLoanId2'
#     )
#     GROUP BY partner_loan_id
# ),
# LatestApplicantData AS (
#     SELECT yt.app_form_id,
#            yt.partner_loan_id,
#            yt.bank_account,
#            MAX(sa.id) AS applicantId  -- Ensure only one id is selected
#     FROM "partitioned_datalake_production_ap_south_1"."mrburns_withdrawal" AS yt
#     JOIN LatestTimestamps AS lt
#     ON yt.partner_loan_id = lt.partner_loan_id
#     AND yt.time_stamp = lt.latest_timestamp
#     INNER JOIN "partitioned_datalake_production_ap_south_1"."shield_applicant" AS sa
#     ON sa.app_form_id = yt.app_form_id
#     GROUP BY yt.app_form_id, yt.partner_loan_id, yt.bank_account
# )
# SELECT app_form_id AS appFormId,
#        applicantId AS applicantId,
#        partner_loan_id AS partnerLoanId,
#        bank_account AS bankAccount
# FROM LatestApplicantData;

import pandas as pd
import requests
import json

from requests.auth import HTTPBasicAuth

shield_patch_url = ("https://shield.creditsaison.in/api/v1/appForm/{"
                    "appFormId}?validationRequired=false&reRunCpcChecks=false")
BASIC_AUTH_USERNAME = 'produsername'  # replace with the username while running script
BASIC_AUTH_PSWD = 'prodpassword'  # replace with the password while running script
headers = {'content-type': 'application/json', 'requestingSub': 'akg'}

df = pd.read_csv("bank-details.csv")
plids = []
failed_patch = []


# Please don't run for same plid multiple times as multiple bank accounts will get created
def main():
    for index, row in df.iterrows():
        payload = """{{
          "editRequests": [
            {{
              "resourcePath": "linkedIndividuals/[id={applicantId}]",
              "editData": {{
                "bankAccounts": [
                  {{
                    "type": "{type}",
                    "accountNumber": "{account}",
                    "holderName": "{holder_name}",
                    "bankName": "{bank_name}",
                    "ifscCode": "{ifsc_code}"
                  }}
                ]
              }}
            }}
          ]
        }}"""
        bank_account = json.loads(row['bankAccount'])
        print(bank_account)
        updated_payload = payload.format(applicantId=row['applicantId'], type=bank_account['type'],
                                         account=bank_account['accountNumber'], holder_name=bank_account['holderName'],
                                         bank_name=bank_account['bankName'], ifsc_code=bank_account['ifscCode'])
        url = shield_patch_url.format(appFormId=row['appFormId'])
        print(url)
        print(updated_payload)
        response = requests.request("PATCH", url, headers=headers,
                                    data=updated_payload,
                                    auth=HTTPBasicAuth(BASIC_AUTH_USERNAME, BASIC_AUTH_PSWD))
        if response.status_code != 200:
            print("Failed to Patch ", row['partnerLoanId'])
            failed_patch.append(row['partnerLoanId'])
        else:
            print("Success Patch ", row['partnerLoanId'])
            plids.append(row['partnerLoanId'])

    if len(plids) > 0:
        print("Patch Success for ", plids)
        print("Patch failed for ", failed_patch)
    else:
        print("No cases to resume since all Patch failed")
        print("Patch Success for ", plids)
        print("Patch failed for ", failed_patch)


if __name__ == "__main__":
    main()


