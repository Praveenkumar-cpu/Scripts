import requests
import json

headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Content-Type': 'application/json'  # Set Content-Type to JSON
}

def post_karza(applicant_id):
    url = f"https://hulk.creditsaison.in/api/v1/applicant/{applicant_id}/verify"
    try:
        # Sending an empty JSON object
        response = requests.post(url, headers=headers, data=json.dumps({}), verify=False)
        return response
    except Exception as e:
        print(f"Error while posting for Applicant ID {applicant_id}: {e}")
        return None

def start_post_karza(applicant_ids):
    successful_ids = []
    failed_ids = []

    for applicant_id in applicant_ids:
        res = post_karza(applicant_id)
        if res is None:
            print(f"Request failed for Applicant Id: {applicant_id} due to an exception.")
            failed_ids.append(applicant_id)
            continue
        if res.status_code == 200:
            try:
                res_data = res.json()  # Parse JSON response
                tpResponse = res_data['kycList'][0]['tpResponse']
                print(f'Successfully Posted | Applicant Id: {applicant_id} | tpResponse: {tpResponse}')
                successful_ids.append(applicant_id)
            except (KeyError, IndexError) as e:
                print(f"Unexpected response format for Applicant Id: {applicant_id}. Error: {e}")
                failed_ids.append(applicant_id)
        else:
            print(f"Failed to post Karza | Applicant Id: {applicant_id} | Status Code: {res.status_code} | Response: {res.text}")
            failed_ids.append(applicant_id)

    print("\nSuccessful Applicant IDs:")
    print(successful_ids)
    print("\nFailed Applicant IDs:")
    print(failed_ids)

if __name__ == '__main__':
    applicantIds = [
"12487694"

]
    start_post_karza(applicantIds)
