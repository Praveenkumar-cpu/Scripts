import requests
import json
import pandas as pd

PLID_LIST = [
"PSEKSF11095548"
]

shield_get_url = "https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/{plid}"
guardian_url = "https://guardian.creditsaison.in/api/v1/creditPolicyCheck/appForm/{appFormId}"

headers = {
  'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=0A96353F701EDA53C84FCA0C3D8F0E0B'
}

for plid in PLID_LIST:
    shield_response = requests.request("GET", shield_get_url.format(plid=plid), headers=headers)
    if shield_response.status_code != 200:
        print("Shield Get Appform Failed for {}".format(plid))
    else:
        shield_response_json = shield_response.json()
        apid = shield_response_json['id']
        guardian_response = requests.request("POST", guardian_url.format(appFormId=apid), headers=headers, data=json.dumps(shield_response_json))
        if guardian_response.status_code != 200:
            print("Shield Guardian Failed for {}".format(plid))
        else:

           print("Success for {}".format(plid))


