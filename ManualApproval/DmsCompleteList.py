import requests

# List of appForm IDs
app_form_ids = [
"91fecc4c-b81f-4fc3-bbc6-3761730dd28f",
"5a0a047d-6e9e-4471-97ae-fd949b3905b9",
"d88ba7b7-54c2-48d1-929d-49e55f3de69a",
"32f1c2b1-0567-46f6-8879-21fb63111f18",
"1f54282f-1567-4a17-9ca0-c80db62371a2",
"a4c6c5b2-b60c-404a-ba29-0752936a9706",
"7fcea69c-38c1-4ab0-8ef7-caa6e5cab838",
"06d36f9a-a2e5-4a8d-8791-6b992d7fefe1",
"c07c5bd3-58f7-42b6-bcb3-922b576dc4af",
"00cf447f-4250-4566-a333-96b37de59afc",
"2446fd49-3b31-4a1d-a8a1-07652d0f61d3",
"11c3a4f4-1258-4786-8479-b3c9e9acc761",
"2bc89319-1506-4db1-a423-4581c23a48b5",
"b47ff373-67dc-4631-8cce-22208424f9b3",
"6e307730-a281-42c6-b51f-de45927dd0f2",
"3ac837ce-77b4-49ca-9d56-0a39dadd3268",
"1cbd74ee-3427-4a63-8432-13cb16316c9f",
"49db70c8-83f0-4133-a6f0-809d23c7195b",
"fb3cf07b-2e8b-4f6c-a94a-29bff3f0f5b1",
"2c561169-e161-4a05-b6ae-68e9fa97b377",
"38c52095-cc18-4e3f-a980-6dda3e072f3e",
"267a76ba-2211-4fc3-aa22-f3c9b7e1c224",
"8fa9f7be-c8bb-4800-87a0-301b5af9995f",
"291115c3-bc6a-4357-ba72-2bc81fe91b52",
"76695a32-bd6a-42e8-9ef5-187cf7fc80ca",
"5b1da58d-663d-42a3-a00e-40cd5cc88a78",
"be1254e0-9396-416e-9105-0d7aa3b9dd7c",
"498f8965-0233-4fdc-a599-d34d729cab3c",
"52aea8de-57b5-4323-a2ec-3cb4f04c1d8f",
"06a7db30-ed5c-4b3c-9714-284efda400c0",
"18dc5675-ca42-4266-91d8-28d79bf0675c",
"43a15af4-0094-4933-9e38-5e977846b2b9",
"b38cbade-7e0e-42fe-a788-fb7ed5f4e0f8",
"ec4a8135-9302-4b27-ba3b-d2c0a8616ad6",
"9850dfc8-0513-4f9a-963d-56107f89a22a",
"e50a2331-03f7-4562-a277-818df6755d77",
"866fa65a-45c8-439b-8630-572462616ee6",
"6bc33ca1-d924-4d8b-a6d4-ddc52acb113e",
"6131ec26-6b6e-474e-b957-c6eb7dd2d480",
"e291c7a1-58d6-48a7-9e66-4f0621d47976",
"d1f17626-9f99-4410-8fde-f18c1696a69e",
"6752c8db-6f7c-452a-8129-678211baa345",
"69c61c9a-93a3-4d57-a4b4-0704efe22087",
"a062d329-c731-4f12-acd8-1d5f5c3646ad",
"00fe803e-3d49-47ff-80c8-0a6cc55be8ff",
"722b088c-c949-4ce0-b1a9-8317b7aabcf3",
"fe4baca0-228b-4835-88e3-d56be1206d8b",
"049e65cb-3949-4add-b3f8-a7dbabb95439",
"b417c432-8a58-4e8e-a624-cc0e9012aae0",
"fa188924-80de-4a07-91ca-0c19fc29067b",
"fc01984c-5592-4b48-9177-ac5c54c3c9a1",
"34518efc-a7ad-49aa-bb32-cc0750f5f963"
]

url_template = "https://drstrange.creditsaison.in/api/v1/appForm/{}/docsBySection?loanProductCode=KBL"
headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Cookie': 'JSESSIONID=98D751576936C56F9A03F73B8B3D9E6D; JSESSIONID=F6CF096264C9FF3BA0961B63321157C9; JSESSIONID=9BE5B75501EEBB1E9AF9A612456B9240; JSESSIONID=3CA1CF0B409B06032DA098DE794EC7C9'
}

complete_ids = []
incomplete_ids = []

print("Fetching details, please wait...")

for index, app_form_id in enumerate(app_form_ids):
    url = url_template.format(app_form_id)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("dmsComplete") == True:
            complete_ids.append(app_form_id)
        else:
            incomplete_ids.append(app_form_id)
    else:
        print(f"Failed to fetch data for appForm ID: {app_form_id}, status code: {response.status_code}")

    # Display progress
    print(f"Processed {index + 1}/{len(app_form_ids)}")

print("\nIDs with dmsComplete true:")
for complete_id in complete_ids:
    print(complete_id)

print("\nIDs with dmsComplete false:")
for incomplete_id in incomplete_ids:
    print(incomplete_id)
