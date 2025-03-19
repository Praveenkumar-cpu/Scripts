import requests

# List of app form IDs
app_form_ids = [
"cad8286e-d25f-4e64-9c38-a8cd626ef4e0",
"91f79661-a09b-4546-9972-759b4c93ec95",
"e2168770-765e-40c5-9be5-8a60d641ecd4",
"573fe6a5-b0b1-46a3-b129-015dfbd7691e",
"9bf5fa71-3b8c-44bf-8df5-3de9e9e642cd",
"5a91e3fd-f130-440b-b7d6-be74676363eb",
"0ddcafed-0dfa-4a00-aa81-6aeff531a0ba",
"430b3a19-2523-497d-b57f-8dd0dec29eea",
"3eaa9f7c-7227-422f-af2a-592e6a635a9a",
"3693173d-0f26-4f85-9fef-2dc2b51efe9c",
"aa4304ae-c1c3-4dfb-b6fa-bb039177894a",
"d7a04be0-83c7-4719-96a3-12e0947d4c87",
"d70a63d0-9119-4bdd-a875-f98af07020b2",
"c23630ba-6e20-4dca-bb0f-52f3fc49dd04",
"f056a5ab-102c-4568-bcc0-16e5df8cc18a",
"cea9b87e-529b-4a25-b688-5b861bbf826d",
"9a470f65-276f-459c-84ff-3176e7a6e6c8",
"0f464786-1dc8-4590-bded-32e5c996b1cf",
"f5a29f9b-f0e2-4ee7-81a3-ecd343cc4487",
"ed91fdb5-0464-4863-bf4a-692c2e754591",
"7a18520e-0364-4cd1-aeab-89727f2ad870",
"b8a496b7-b7a8-491b-99f1-a65803dfceb4",
"f1fa0eab-e3ca-4537-98ee-c7c461095982",
"2016746e-1456-450c-9642-361bff781792",
"fcdc37e1-9371-479f-833e-aef5e407d75d",
"a4fe75c8-d079-424d-9778-742c9cceb480",
"72738cb4-674f-4f56-ab0e-42239652ba06",
"62bc4b03-0c92-4f76-95db-426644523357",
"8125fd19-9db4-4965-a88d-f01e979d1952",
"f2a04777-3252-4d5d-89a1-ea7228fedd3e",
"ab4eb545-9c52-453a-9f8c-a401ccd4310f",
"9a1ab48e-763f-4882-bf09-687d6210e7e6",
"de5c4987-66d7-41a0-a1b9-0a2d1bf04a5f",
"57dc957c-1c6d-490c-88c0-d493c181a0b9",
"0cba8b42-65e3-4b9f-811e-3227ab0e8791",
"11c3ab71-6a6e-4b12-8f63-7290936ef1a3",
"5310b1fa-797f-4a6d-b62a-82709aff11fd",
"479e8f06-0320-4234-9421-192f5ab1e4fd",
"0b4b11f9-e41e-43e8-aff5-4b012d7af338",
"b1647a3f-1759-4d9a-984f-429d1ca7d481",
"74242856-a501-4943-b207-a4d27426440f",
"bfe7865c-0b85-4a46-a27b-b96547fd18cd",
"34d528a6-1bf7-42eb-81a9-fb15ebcd4131",
"cab9765f-b257-4e85-87d8-9401c0abbb0e",
"5719ffba-8fc8-4290-ac9b-fe17d0968179",
"53bc7596-9075-4f3f-be18-8eed876f8e54"


]

url_template = "https://drstrange.creditsaison.in/api/v1/appForm/{}/dms/complete?loanProductCode=ESC"

headers = {
    'Content-Type': 'application/json',
    'Cookie': 'JSESSIONID=A396EAAE8983BE16F0199B0CEDB64CB9; JSESSIONID=E888C64614185E585C387BCFB9CF961A; JSESSIONID=7A00F3ACA9B70511E2FD2B34AC803E62',
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
}

# Lists to keep track of successes and failures
successes = []
failures = []

# Loop through each app form ID and make a POST request
for app_form_id in app_form_ids:
    url = url_template.format(app_form_id)
    payload = {}  # You can update this with the actual payload if needed

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            successes.append(app_form_id)
            print(f"Success for {app_form_id}: {response.text}")
        else:
            failures.append((app_form_id, response.status_code, response.text))
            print(f"Failure for {app_form_id}: {response.status_code} - {response.text}")
    except Exception as e:
        failures.append((app_form_id, 'Exception', str(e)))
        print(f"Error processing {app_form_id}: {e}")

# Summary of results
print("\n--- Summary ---")
print(f"Successful requests: {len(successes)}")
for app_form_id in successes:
    print(f" - {app_form_id}")

print(f"\nFailed requests: {len(failures)}")
for app_form_id, status, message in failures:
    print(f" - {app_form_id} (Status: {status}, Message: {message})")
