import csv
import requests
import time

# Specify the path to your CSV file
csv_file = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/appForm.csv'

# Read the CSV file and iterate through each row
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        app_form_id = row['appForm']

        # First, update the status to CREDIT_COMPLETE (status code '12' for this)
        url = f'https://shield.creditsaison.in/api/v1/appForm/{app_form_id}/status'

        headers = {
            'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=22BC06F4C6BD9B57296528F195BFDD5D'
        }

        data = {
            'status': '15'  # Assuming '12' is CREDIT_COMPLETE
        }

        try:
            response = requests.post(url, headers=headers, json=data, verify=False)

            # Check the response status code
            if response.status_code == 200:
                print(f"Status updated to CREDIT_COMPLETE for App Form ID {app_form_id}")
                # Now call the callback URL for processing the change
                callback_url = f"https://thor.creditsaison.in/api/v2/callback?partnerId=ES&partnerLoanId={app_form_id}"

                callback_headers = {
                    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
                    'Content-Type': 'application/json',
                    'Cookie': 'JSESSIONID=22BC06F4C6BD9B57296528F195BFDD5D'
                }

                callback_response = requests.get(callback_url, headers=callback_headers, verify=False)

                # Check if the callback was successful
                if callback_response.status_code == 200:
                    print(f"Callback sent successfully for App Form ID {app_form_id}")
                else:
                    print(f"Error sending callback for App Form ID {app_form_id}: {callback_response.status_code} {callback_response.text}")

            else:
                print(f"Error updating status for App Form ID {app_form_id}: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request error for App Form ID {app_form_id}: {e}")

        # Optional: Add a delay between requests to avoid hitting rate limits
        time.sleep(1)
