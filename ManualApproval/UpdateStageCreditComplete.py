import requests
def update_stage(application_form_ids):
    url_template = 'https://shield.creditsaison.in/api/v1/appForm/{}/stageStatus'
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=2C7429A3191DA45A752984202DA1E6D7; JSESSIONID=C6783D184A2B2B698291FD74453C1495; JSESSIONID=292991B7ECDC394E12DB972B7D0A8111'
    }
    payload = {
    "stage": "creditstage",
   "status": "CREDIT_COMPLETE"

  #    "stage": "disbursalstage",
  #   "status": "DISBURSAL_COMPLETE"
    }

    for app_form_id in application_form_ids:
        url = url_template.format(app_form_id)
        response = requests.put(url, headers=headers, json=payload,verify=False)

        if response.status_code == 200:
            print(f"Stage updated successfully for application form ID {app_form_id}.")
        else:
            print(f"Failed to update stage for application form ID {app_form_id}. Status code:", response.status_code)

if __name__ == "__main__":
    application_form_ids = [
"ab419502-ec03-465d-97dc-c18b2ddedaff",
"ef3185fe-f502-4ecd-a522-03d19c14040a",
"0b80c4fc-3c82-4a2c-aedf-7b5b6c2bf766",
"5520f631-4a33-4c2b-894c-ae7c53426737",
"1b91d380-6e5e-43e7-8578-dda3d757630d",
"28792c9c-b018-4e2a-be74-c0ee2b67f701",
"e9f2353a-9bf8-4bdf-8744-468a9ce64247",
"a86f4d27-1486-4e74-bf17-bf0b9ff88d7a",
"87c83bc6-2164-4d4a-967d-477392e85a18",
"76c20159-e3df-44a2-aa99-9ba30fe2ac4f",
"58d6a4a2-6ae7-4960-9162-c6faea420f91",
"c4fabb5d-7d64-4f00-aaa3-29750c3e4946",
"aaa8071c-e172-4b2b-b1dc-24e245fb5d4a",
"4bc3fc97-5c9a-49e7-b500-ee69d1641337",
"e8e88431-9b25-4042-a917-d4560faa3474",
"05edfb02-bcb7-447e-b938-f106f4b1d024",
"5d556ab8-6641-4205-ac61-8d0c3ea21027",
"42e75cb5-11fb-4d54-b806-b31856ae484b",
"a5e30105-296e-410b-b4d4-152bdeb17e10",
"451ebf5a-0368-4c31-a3bd-e8d2067a8774",
"68cec107-cb27-48e7-bf62-e62bc42f89a8",
"ce8703a2-83ac-452e-99d6-892516c3c084",
"a2b1f3e8-7f8b-4111-9740-9feaf106f0e6",
"90002ec5-5b35-4988-845f-b64280d12a3a",
"be4bf198-5a5e-4666-a06c-fd5ede5a3c03",
"4f22af5d-1956-47d1-a966-e718a208c328",
"c7ddcc85-574f-4d72-aa57-ee4dd3728756",
"9699a862-ed62-4e22-99df-0ed3b403cdde",
"7932d7f7-ed51-4c2f-bc17-8f6c889dfb4d",
"901d134f-3797-422e-8c97-4ffb45dde1b7",
"c4ebbba6-d787-4dfc-9e62-6bf9e89b48c1",
"39a95ea9-c045-4fdf-912c-34584c77d391",
"f270cf88-91d5-4dae-bd4d-c21e69702d16",
"334e652a-ce04-4887-b314-b1e9d7d2c1ea",
"26d93243-686b-4c88-9d80-a0ea23879d59",
"646b496d-53a1-49d8-857e-23f4ef28373d",
"05d84ed5-f26c-498d-8675-5661e654a2bc",
"ace5b41f-5210-4161-bf4f-63b01df32ab8",
"9445b5f7-c28d-4586-b69f-9979336d4e48",
"6fb04c91-cfdb-47ad-9646-cc19a0596b33",
"0e018c42-9937-466b-bf4e-de4656f91eab",
"17ff00b7-b2ee-4256-b865-d920e117f054",
"9435876b-08fe-47f0-a1f1-22bf087c2a9b",
"3585c4c0-a349-4c86-b227-bbb63bca1d07",
"76db0090-de46-48ef-8519-c8bb16cbb304",
"a18ad77c-65a0-44f6-888c-5f40e9308a5f",
"c74b76a8-5ac4-4a08-966d-e3da0099b0ce",
"84998654-0b49-45ab-8713-d3177091194b",
"2995708b-aa32-4edb-bdc5-2e67b6b51385"
]
    update_stage(application_form_ids)
