import requests
import json

pids = [
"1451098628",
"1445604173",
"1449717089",
"1443387728",
"1244424000",
"1133882842",
"1430595434",
"1452003595"
]

def checkCallback(pid):
    url = "https://thor.creditsaison.in/api/v2/callback/status"
    payload = json.dumps({
        "partnerLoanIds": [pid]
    })
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response_data = response.json()

        # Check if the response is a list and has elements
        if isinstance(response_data, list) and len(response_data) > 0:
            if 'message' in response_data[0]:
                return -1  # Return -1 if there is an error message
            return response_data[0]['callbacks'][-1]['value']
        else:
            print(f"Unexpected response format for PID {pid}: {response_data}")
            return None

    except json.JSONDecodeError:
        print(f"Failed to decode JSON response for PID {pid}: {response.text}")
        return None
    except Exception as e:
        print(f"Error processing PID {pid}: {str(e)}")
        return None

for pid in pids:
    result = checkCallback(pid)
    print(pid, result)
