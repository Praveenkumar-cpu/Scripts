import requests
import json

# List of appForm IDs
app_form_ids = [
   "d21aece1-7ce7-4b22-9652-48169d36f591",
   "a283bc42-60ab-4ea8-bd09-2885fa3a6e95",
   "9c27a3c6-7782-42fa-9711-b1980e45bc7f",
   "a7e51d3d-96b4-4fed-92d0-335f1ac1ba14",
   "7406c449-1b5d-482d-ac0f-76198f2109d2",
   "d4b7fff4-3f42-4c94-8dbe-457e57bce95a",
   "c4fcdf0b-b0fd-4400-b917-b4061b92c22e",
   "aec873d6-f4e8-4442-a5ab-528fb3896816",
   "03de5f9e-d363-4a42-b68d-a9ef2eb5b4c1",
   "8376edea-ecf0-4836-8322-149c7d396350",
   "356f95ca-359d-4732-b810-bda3b229ae96",
   "dc34c408-9a26-4bc8-89a5-662fe4f1b67e",
   "b715d718-e383-46a4-8961-2c5e8fde0eb3",
   "c236a8e3-86a9-478e-8853-503dd5399bb5",
   "16f593f3-bc1f-4f8c-8098-adb38c877b21",
   "7fd11236-4916-4b0d-8038-a513f17880e7",
   "3f36ab6d-025f-484f-8356-f297c6c39efa",
   "bd887441-1bc6-4263-94ed-56d4821ecb0f",
   "be787559-ae06-4aa9-b73f-336b818e7cfb",
   "e55fba22-30ac-435d-be99-36e8bbb9a966",
   "7419b95d-ee0a-4c29-a41a-94cc71d50400",
   "44dfa57c-17fd-41b0-8468-6c22424f7051",
   "580655dd-fed1-4943-8d90-09fb8972ab14",
   "beef5599-d30a-4a22-9412-497c804624ca",
   "ff1c476b-b53c-4a15-9e6a-ffce7f302337",
   "cdc6cec7-6ca5-4142-baf3-c88b7024bbc4",
   "7dea837b-05ac-494d-bc91-63cfb35eac57",
   "b3ee796d-c42b-4504-b065-e4292e799402",
   "a2c5598c-5d1e-4b9b-b933-803b84f3511f",
   "33a9c972-ce4b-4b51-b93a-14edfa6879ad",
   "e637fa5e-17e0-48d1-844b-aa79da0ed9c3",
   "9d76bd38-f8b6-4efc-aa4f-db0f8a17fd93",
   "25c91324-663b-4595-b760-5181f877996c",
   "9fa26285-3d01-4083-a641-27eaae76dfa7",
   "454c0df9-6475-433f-8f6f-e6178ffc55ea",
   "c9e20ed9-cb27-439d-932f-64ea90ed8929",
   "89582340-0029-4257-a4d7-b3a3caea1a96",
   "392ee3ae-fcdb-4c2b-9794-a96bb546aa6b",
   "a3044fe8-2544-4515-98f7-e7f88068fc43",
   "2aabf5e7-b3aa-4559-bc99-116ab44913b0",
   "1d8d7c0a-e68e-4a6f-931b-93313f553629",
   "a7f0238b-6902-474e-87f1-82ee2c4672ae",
   "c322a413-01eb-4507-9fb7-5bf61ecb3791",
   "5c13f1c4-1d1e-41cb-ba87-f42f4faaeee4",
   "06669d94-f464-4f7a-a1f9-778ea659f971",
   "4221b98b-38f6-42d5-a945-d9d4c7eef229",
   "8252c5e4-5136-4580-9064-af66f963e79a",
   "4ffc87a4-82b8-446c-ab3c-8f26052b321a",
   "350604de-e4c7-45ed-a727-c93673e212ba",
   "818cd277-f10e-4cfd-8e4c-89c72ed83008",
   "989a5aaf-bc0f-4ee2-b563-96155d9ea130",
   "46a26a3e-e1be-4ee4-bdec-e977d45bec9f",
   "5165cebd-0be0-4581-bfb9-14a2ef312f7f",
   "79d6d08b-86d3-4a0e-ae38-158c116ab968",
   "727c8764-a872-4b7e-93bf-6b8ae6cbda35",
   "5feb5447-9cd4-475c-b2eb-0ef4458d27d8",
   "6089af33-f4d8-425e-8cca-38c8bd8b64fb",
   "3cf40af7-4923-437f-9d70-e12269db21be",
   "e80f50b6-ee14-4f5e-bd87-d1a8fdaba76d",
   "723c4f1b-2ebc-4f3d-8373-f981dcfefb0b",
   "24e4c412-7aa1-4a50-a3e0-6c264469d328",
   "b0daf326-cfce-48e9-9de5-b897086d0239",
   "faea2fe2-9f0c-48ab-8b50-0a41c1f64bed",
   "9d6fe6ee-6c81-4558-9a47-6ad7fa3251e5",
   "e132f224-526b-4c2d-8334-4f7306765b22",
   "cbd178a3-7ce1-43f7-87bb-ca36ce8785dd",
   "92f8c59b-41c6-4e13-8877-1667d2d6ea51",
   "e2dfec9d-ee5b-4453-aa35-94cce69a3dbb",
   "7fde4232-4ae5-4db0-bc7c-34753f5ce03c",
   "6a69ce73-c06c-4724-b8e9-1eed9c1be7ee",
   "a43bad83-0fb5-4ceb-8929-d1a51cbf309b",
   "d02761b6-4c96-4f5b-9eab-bbea57eab3af",
   "88169a72-0012-441d-bad2-d6a9125b18c3",
   "f4b9c689-1660-451f-9bee-4080ee959594",
   "f54fb2cf-9474-4172-b515-5f4bf4b4862b",
   "88a88036-b5f0-4337-989c-ecea2539bb8c",
   "b3d29ece-ae98-4d7e-a3c7-78536d9aa807",
   "8dfea53a-dde8-4b85-a109-fe95c59883a1",
   "71e6378d-12ec-4752-97c1-15c80477fe2f",
   "91af777e-1009-4486-9daf-cfbd6785c9d7",
   "ac7b4efa-e7b1-4949-b291-8a7bc4ddf714",
   "5571031e-43b5-4e95-bbf6-487b3f20e45a",
   "d05a8a4d-e7aa-4964-b941-19e59d11faf7",
   "a5352552-e69c-4dd1-a7c1-87d49acdc035",
   "9f9fddc1-73e7-463a-b487-8388229e7708",
   "63d2f5e7-4c39-403e-8adb-2308bc9f56a6",
   "6a2e8daa-ff41-4a44-90f0-a5c4063f3c95",
   "37993891-5981-45f7-bf74-261eb8740ba6",
   "45c564dc-072d-43f8-929f-c8e5a0095b0c",
   "0b6ba70c-bef9-44cc-a1ae-b838d958c7fb",
   "bbe51b59-a4ed-400d-a881-1e51d0210f7b",
   "e49fdcb3-a515-4a2d-8ee9-77b382f16704",
   "fb797a5c-ffaa-4262-8e30-8a3d1da4c25a",
   "67455951-6f3c-4cc0-8c6e-b0b9dce33878",
   "1a4e31a7-8726-4a6c-8ab6-a6165b2c2d40",
   "430a170a-43ec-4d3a-a767-8ab919976478",
   "4af72001-944d-4554-82b4-aaae147bf8fb",
   "ab3a9d33-1376-43c4-9113-9aea60c9f8cf",
   "09b3e784-c039-4407-ac02-414532cc46b1",
   "7e8ea147-b92c-4eb1-96f6-1d9941c47cd0",
   "47ff5103-ae37-4809-9720-20d107628ae9",
   "28f8e2ff-adb3-4304-8996-7428e6d4240f",
   "02efa770-facf-4840-9b00-e904b93ba137",
   "3071f862-c56c-4c03-88e7-59319964e7e2",
   "4f3fc05b-e90d-445c-bc2a-341360a86be8",
   "e84f4b45-5c64-4915-aade-cfcf00677947"
]

# Base URL
base_url = "https://shield.creditsaison.in/api/v1/appForm/"

# Headers
headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
    'Content-Type': 'application/json',
    'Cookie': 'JSESSIONID=A396EAAE8983BE16F0199B0CEDB64CB9'
}

# Initialize a list to store partnerLoanIds
partner_loan_ids = []

# Iterate through appForm IDs and make requests
for app_form_id in app_form_ids:
    url = f"{base_url}{app_form_id}"
    response = requests.get(url, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()

        # Extract partnerLoanId (modify according to the actual structure of the response)
        if 'partnerLoanId' in data:
            partner_loan_ids.append(data['partnerLoanId'])
        else:
            print(f"No partnerLoanId found for appForm ID {app_form_id}")
    else:
        print(f"Error {response.status_code} for appForm ID {app_form_id}: {response.text}")

# Print the list of partnerLoanIds in a clear format
print("List of partnerLoanIds:")
print(json.dumps(partner_loan_ids, indent=2))
