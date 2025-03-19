import requests

def call_api_with_multiple_ids(applicant_ids, appform_ids):
    base_url = "https://hulk.creditsaison.in/api/v1/applicant/{}/verify/?appFormId={}"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=A396EAAE8983BE16F0199B0CEDB64CB9; JSESSIONID=E888C64614185E585C387BCFB9CF961A',
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
    }

    for applicant_id, appform_id in zip(applicant_ids, appform_ids):
        url = base_url.format(applicant_id, appform_id)
        response = requests.post(url, headers=headers)
        print("Response for Applicant ID:", applicant_id)
        if response.status_code == 200:
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)
        else:
            print("Skipping. Status Code:", response.status_code)
        print("---------------------------")

# Example applicant IDs and appFormIDs
applicant_ids = [
"9196514",
"9312528",
"9317174",
"9322815",
"9322810",
"9322799",
"9322791",
"9322787",
"9322370",
"9328464",
"9329465",
"9330107",
"9330631",
"9330635",
"1064864"


]
appform_ids = [
"744b58de-7759-4b0d-83ef-a9bbef0de172",
"a87a50fd-d3e7-4498-b2be-d7875af5f9bc",
"05ff499c-227f-4aa9-958d-2dd4ad38a69e",
"d7ee19a4-e2c9-4217-b025-e8f765c72703",
"9f419f2d-5ae2-4767-ad76-bb22635fbbd2",
"ed8de144-3149-416e-a6eb-b22937ad3134",
"94c1cf21-b665-4ec6-ab49-0e2c4035139b",
"2ed7fdb7-d972-4866-a854-594fee62509f",
"04564185-4e0a-471e-988b-3999f02334d8",
"5afcb8df-680e-4a07-bc50-aca341875d78",
"ec6c23e5-d6cd-4edc-a750-5cbb5e2040ba",
"112f116f-9bba-413f-bce2-caff4c05c108",
"e211d0a4-5105-440f-8242-b7314c153863",
"c61d3e2b-f686-4c9e-b3bf-287028494939",
"0ebbd57a-7b6d-4baf-99f0-3c0c8b07f152"



]

call_api_with_multiple_ids(applicant_ids, appform_ids)
