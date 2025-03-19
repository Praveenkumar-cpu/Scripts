import requests
import csv

def hit_dedupe_api(appForm):
    url = f'https://vision.creditsaison.in/api/v1/appForm/{appForm}/dedupe/detailed'
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Cookie': 'JSESSIONID=C6783D184A2B2B698291FD74453C1495; JSESSIONID=7F4EADE38814B54F803F2F7FA011D404'
    }

    response = requests.get(url, headers=headers, verify = False)
    return response

def hit_applicant_dedupe_api(applicant_id):
    url = f'https://vision.creditsaison.in/api/v1/applicant/{applicant_id}/dedupe'
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Cookie': 'JSESSIONID=9D2F7592E18DF9AC0E5232388CE7DD00; JSESSIONID=9D2F7592E18DF9AC0E5232388CE7DD00'
    }

    response = requests.post(url, headers=headers, verify = False)
    return response

# Specify the path to your CSV file
csv_file = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/appForm.csv'

# Read the CSV file and iterate through each row
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if it exists
    for row in reader:
        appForm = row[0]

        # Hit the Dedupe API for the current appForm
        dedupe_response = hit_dedupe_api(appForm)
        dedupe_json = dedupe_response.json()

        print(f"AppForm: {appForm}")
        print("Dedupe API Status Code:", dedupe_response.status_code)
        print("Dedupe API Response JSON:", dedupe_json)
        print("\n" + "="*30 + "\n")  # Separate each API request for better visibility

        # Check if dedupeStatus is "0" (indicating success)
        if 'detailedApplicantDedupeList' in dedupe_json and dedupe_json['detailedApplicantDedupeList']:
            detailed_applicant = dedupe_json['detailedApplicantDedupeList'][0]

            # Check if dedupeStatus is "0" for the first detailedApplicantDedupeList it will take applicant id
            if 'dedupeStatus' in detailed_applicant and detailed_applicant['dedupeStatus'] == "0":
                applicant_id = detailed_applicant.get('id')

                # Hit the Applicant Dedupe API with the extracted "id"
                applicant_dedupe_response = hit_applicant_dedupe_api(applicant_id)

                print(f"Applicant ID: {applicant_id}")
                print("Applicant Dedupe API Status Code:", applicant_dedupe_response.status_code)
                print("Applicant Dedupe API Response Text:", applicant_dedupe_response.text)
                print("\n" + "="*30 + "\n")  # Separate each API request for better visibility
            else:
                print("Dedupe status is not 0. Skipping Applicant Dedupe API request.")
                print("\n" + "="*30 + "\n")
        else:
            print("No detailedApplicantDedupeList found in the Dedupe API response.")
            print("\n" + "="*30 + "\n")
