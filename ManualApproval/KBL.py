import subprocess
import time
from Quartz import CGEventCreate, kCGEventMouseMoved, CGEventPost, kCGHIDEventTap

def prevent_sleep():
    while True:
        # Move the mouse cursor to keep the system awake
        event = CGEventCreate(None)
        CGEventPost(kCGHIDEventTap, event)
        time.sleep(60)  # Move the cursor every 60 seconds

# Start the prevent_sleep function in a separate thread
import threading
threading.Thread(target=prevent_sleep, daemon=True).start()

# Your existing script code here
import requests
import json

# Function to get processId and entityId
def get_process_and_entity_id(partner_loan_id):
    url = f"https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/{partner_loan_id}"
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Cookie': 'JSESSIONID=98D751576936C56F9A03F73B8B3D9E6D; JSESSIONID=6F509A64FE83F7C804F707B924D12E81; JSESSIONID=A9AE3AF2E6DBF2259AA90C55AC14F0D8'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        process_id = data.get("workflowId")
        entity_id = None
        if "linkedIndividuals" in data and len(data["linkedIndividuals"]) > 0:
            entity_id = data["linkedIndividuals"][0].get("id")
        return process_id, entity_id
    else:
        print(f"Failed to get process and entity ID for partner loan ID {partner_loan_id}")
        return None, None

# Function to make the POST request
def post_resume(process_id, entity_id):
    url = f"https://tars.creditsaison.in/api/v1/process/{process_id}/resume?entity={entity_id}&taskName=resumeAppFormEntityMatching"
    payload = json.dumps({
        "variables": [
            {
                "name": "aadhaarXmlType",
                "value": "UIDAI"
            }
        ]
    })
    headers = {
        'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg==',
        'Cookie': 'JSESSIONID=95EDDDFBB904DBABCDD44BEB68F4FCC2; JSESSIONID=01F0B4BA982A9FDF8F798F30CA47E201; JSESSIONID=8A5E8EC21358FC28A072F26394919660; JSESSIONID=CC1EAF622F304B29637F308966C3F181',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    print(f"Response for process ID {process_id} and entity ID {entity_id}: {response.text}")

# List of partner loan IDs
partner_loan_ids = [
"CASKB240709WAKYA",
"CASKB240710HUGFL",
"CASKB240709ESWNP",
"CASKB240710EJZKM",
"CASKB240711VBZLU",
"CASKB240629GHKGY",
"CASKB240713LMEFS",
"CASKB240713LHORR",
"CASKB240717XCMGB",
"CASKB240717UAZVC",
"CASKB240717BBWCZ",
"CASKB240717YJJJD",
"CASKB240717NLPCY",
"CASKB240717BAXIN",
"CASKB240717CCNDP",
"CASKB240717SUHEG",
"CASKB240717QNUHW",
"CASKB240717WDEQP",
"CASKB240717JAQSY",
"CASKB240717ERPHD",
"CASKB240717XZUZO",
"CASKB240717KKJIB",
"CASKB240717HZLJV",
"CASKB240717YBECE",
"CASKB240717JAOAV",
"CASKB240717KNVNL",
"CASKB240717JNKYQ",
"CASKB240717WWLWB",
"CASKB240717SHXAG",
"CASKB240717GINFG",
"CASKB240715FVCUA",
"CASKB240717EHGLJ",
"CASKB240717VFYQP",
"CASKB240717MBWZG",
"CASKB240717JVJKS",
"CASKB240717MHENK",
"CASKB240717KNABH",
"CASKB240717VWERG",
"CASKB240717YJIGM",
"CASKB240717XCWJJ",
"CASKB240717EMJAA",
"CASKB240717OEPSE",
"CASKB240717UPJBE",
"CASKB240717BXPBW",
"CASKB240717CLEJV",
"CASKB240717EQEPV",
"CASKB240717SHFOL",
"CASKB240717PPKHW",
"CASKB240717SETIA",
"CASKB240717AHLVD",
"CASKB240717MKVXQ",
"CASKB240717CJMSI",
"CASKB240717BFIIK",
"CASKB240717PKJTW",
"CASKB240717ZUFSO",
"CASKB240717VGXAN",
"CASKB240717VONFU",
"CASKB240717TJIID",
"CASKB240717MYUPJ",
"CASKB240717OJBLP",
"CASKB240717FYTSQ",
"CASKB240717VJGIR",
"CASKB240717GXXGD",
"CASKB240717UNQOQ",
"CASKB240717MYFRK",
"CASKB240717IBEKT",
"CASKB240717IVQGG",
"CASKB240717DUEPE",
"CASKB240717XXHWR",
"CASKB240717YXNDP",
"CASKB240717LLPQH",
"CASKB240717UYSOG",
"CASKB240717VVBDR",
"CASKB240717YODBI",
"CASKB240704MHLDR",
"CASKB240717TKVUU",
"CASKB240717TKBAV",
"CASKB240717TFTYW",
"CASKB240717RROIF",
"CASKB240717GXMWZ",
"CASKB240717DBHVK",
"CASKB240717EANXV",
"CASKB240717CWFKL",
"CASKB240717SMNQW",
"CASKB240717LAWKA",
"CASKB240717WQUML",
"CASKB240717SUWGW",
"CASKB240717KAMDD",
"CASKB240717PXMEG",
"CASKB240717BGELJ",
"CASKB240717XSRXU",
"CASKB240717JGKPX",
"CASKB240717HDXFF",
"CASKB240717XMPAP",
"CASKB240717JPUEZ",
"CASKB240717MOWGS",
"CASKB240717WGGLJ",
"CASKB240717AWBFD",
"CASKB240717LWJFV",
"CASKB240717NVVLH",
"CASKB240717VQTJR",
"CASKB240717DAACY",
"CASKB240717YLAYY",
"CASKB240717ZULKT",
"CASKB240717SBJFJ",
"CASKB240717DLQZU",
"CASKB240717BQTAY",
"CASKB240717REXLR",
"CASKB240717CPNBG",
"CASKB240717BHSUI",
"CASKB240717EKJQH",
"CASKB240717BEPIE",
"CASKB240717BRRTN",
"CASKB240717QZETG",
"CASKB240717DXPVO",
"CASKB240718VDQMS",
"CASKB240717GVLGU",
"CASKB240717RGGCN",
"CASKB240718CAOZB",
"CASKB240718DESDL",
"CASKB240718NVBOD",
"CASKB240718QIZQZ",
"CASKB240718UTILQ",
"CASKB240718HOCZA",
"CASKB240718IFSSQ",
"CASKB240718KPBFZ",
"CASKB240718HSMKD",
"CASKB240718GMCEY",
"CASKB240718GGOWU",
"CASKB240718LDUXR",
"CASKB240718HEOTO",
"CASKB240718ZFLBD",
"CASKB240718OSCFM",
"CASKB240718VRQTE",
"CASKB240718BQGPK",
"CASKB240718JWPSO",
"CASKB240718GAXZN",
"CASKB240718PGIMV",
"CASKB240718JRVGS",
"CASKB240718SEUUZ",
"CASKB240718YTFVM",
"CASKB240718PKUCD",
"CASKB240718CSAWO",
"CASKB240718XVPFC",
"CASKB240718UGGOV",
"CASKB240718LLMKB"

]

# Loop through each partner loan ID and process
for partner_loan_id in partner_loan_ids:
    # Get process ID and entity ID
    process_id, entity_id = get_process_and_entity_id(partner_loan_id)

    # If both IDs are found, make the POST request
    if process_id and entity_id:
        post_resume(process_id, entity_id)
