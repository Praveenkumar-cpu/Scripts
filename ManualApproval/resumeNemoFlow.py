import requests
import json

headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
}

def groot_custom_config(lpc):
    url = f"https://groot.creditsaison.in/api/v1/loanProduct/productCode/{lpc}"
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        json_res = res.json()
        return json.dumps({
            "customConfig": json.dumps(json_res.get('customConfig', {}))
        })
    except requests.RequestException as e:
        print(f"Error fetching custom config: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response for custom config")
    return None

def get_real_time_wf_history(partner_loan_id):
    url = f"https://nemo.creditsaison.in/api/v1/process/resource/{partner_loan_id}/history?onlyTasks=true"
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(f"Error fetching workflow history for {partner_loan_id}: {e}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON response for {partner_loan_id}")
    return None

def resume_task(process_id, task_name, payload):
    url = f"https://nemo.creditsaison.in/api/v1/process/{process_id}/resume?taskName={task_name}"
    try:
        res = requests.post(url, headers=headers, data=payload)
        res.raise_for_status()
        return res
    except requests.RequestException as e:
        print(f"Error resuming task for process {process_id}: {e}")
    return None

already_completed_partner_loan_id = []
pending_partner_loan_id = []
resumed_partner_loan_id = []
failed_resumed_partner_loan_id = []
other_status_partner_loan_id = []
invalid_resume_task_partner_loan_id = []

def resume_hercules_task(partner_loan_ids, lpc):
    custom_config = groot_custom_config(lpc)
    if custom_config:
        print(f'Fetched custom Config for LPC: {lpc}')
        for partner_loan_id in partner_loan_ids:
            history_data = get_real_time_wf_history(partner_loan_id)
            if history_data:
                print(f"Response Data for Partner Loan Id {partner_loan_id}: {history_data}")
                task_list = history_data.get('taskList', [])
                if task_list:
                    last_executed_task = task_list[-1].get('taskName', 'Unknown')
                    workflow_id = str(history_data.get('workflowId', 'Unknown'))
                    print(f'\nPartner Loan Id: {partner_loan_id} | Last Executed Task: {last_executed_task}')
                    if history_data.get('status') == 'f' and last_executed_task == 'UploadExternalBureau':
                        res = resume_task(workflow_id, 'UploadExternalBureau', custom_config)
                        if res and res.status_code == 200:
                            print(f'Partner Loan Id: {partner_loan_id} | Resumed Successfully')
                            resumed_partner_loan_id.append(partner_loan_id)
                        else:
                            print(f'Partner Loan Id: {partner_loan_id} | Failed to Resume Task')
                            failed_resumed_partner_loan_id.append(partner_loan_id)
                    elif last_executed_task in ['EndWorkflow', 'EndWorkflowAndSendCallback']:
                        already_completed_partner_loan_id.append(partner_loan_id)
                    else:
                        other_status_partner_loan_id.append(partner_loan_id)
                else:
                    print(f"No tasks found for Partner Loan Id: {partner_loan_id}")
                    other_status_partner_loan_id.append(partner_loan_id)
            else:
                pending_partner_loan_id.append(partner_loan_id)
                print(f"Failed to get history for Partner Loan Id: {partner_loan_id}")
    else:
        print(f'Failed to fetch custom config for LPC: {lpc}')

if __name__ == '__main__':
    partner_loan_ids = [
"CASKB240727EBWSE",
"CASKB240727LVMIJ",
"CASKB240727YUTDT",
"CASKB240727QAYRT",
"CASKB240729KXTQK",
"CASKB240727NYQEI",
"CASKB240727DFELR",
"CASKB240729YRONT",
"CASKB240729KHMNG",
"CASKB240729DUWEB",
"CASKB240729DRPEP",
"CASKB240726NWQTU",
"CASKB240726SVAWS",
"CASKB240726VGOAK",
"CASKB240727FKFOS",
"CASKB240729TJTGR",
"CASKB240727YVFTL",
"CASKB240729RHWXG",
"CASKB240727DZBIO",
"CASKB240807WIRQY",
"CASKB240729JRRIE",
"CASKB240727HNSMM",
"CASKB240727GAWMM",
"CASKB240729GKAFY",
"CASKB240727WBWNV",
"CASKB240730HRMYO",
"CASKB240729YHKDN",
"CASKB240807OICNY",
"CASKB240727VFRJB",
"CASKB240729ZITQB",
"CASKB240729IZDXD",
"CASKB240727CGLIH",
"CASKB240729HFDKT",
"CASKB240729IFQWC",
"CASKB240727DPNMV",
"CASKB240727MYWVD",
"CASKB240729DLGMT",
"CASKB240727MUMYD",
"CASKB240807TBJHA",
"CASKB240730PWEBG",
"CASKB240730ROGEX",
"CASKB240729WCCXE",
"CASKB240727ZZFXB",
"CASKB240727GZLBN",
"CASKB240727BGGUH",
"CASKB240729AUGAU",
"CASKB240727LGMWL",
"CASKB240730JRGVY",
"CASKB240727YCPTF",
"CASKB240729DIPRU",
"CASKB240727UQDRU",
"CASKB240729VXZKP",
"CASKB240727QDASU",
"CASKB240730HBMGM",
"CASKB240727FQDJO",
"CASKB240727FWWVK",
"CASKB240727VLVZH",
"CASKB240729NNUEK",
"CASKB240727BTJTY",
"CASKB240730MZCKE",
"CASKB240730BDEBR",
"CASKB240727XCEZL",
"CASKB240730HXEWJ",
"CASKB240727OZWDE",
"CASKB240807PPYOE",
"CASKB240730OFBIB",
"CASKB240727UMRRN",
"CASKB240729WMMTY",
"CASKB240807TIVZP",
"CASKB240730VSBUM",
"CASKB240729JKGRN",
"CASKB240730SXILZ",
"CASKB240730HBHBG",
"CASKB240729ALPMG",
"CASKB240729BKJDF",
"CASKB240729MNVNU",
"CASKB240730TGMJQ",
"CASKB240730SOMWD",
"CASKB240729YIOID",
"CASKB240729BCVCC",
"CASKB240730CHDJK",
"CASKB240729NBHCU",
"CASKB240730EZKYS",
"CASKB240729OUKTE",
"CASKB240730UBNJV",
"CASKB240730YGKGP",
"CASKB240730EGCAU",
"CASKB240730ZMGEM",
"CASKB240731JHBTD",
"CASKB240731PQZHS",
"CASKB240731HSFLC",
"CASKB240731XBOYS",
"CASKB240727XKBSD",
"CASKB240727VNJDZ",
"CASKB240727SMDWR",
"CASKB240727IVHSQ",
"CASKB240727ZXPHI",
"CASKB240727TRMYW",
"CASKB240731UAWPO",
"CASKB240730NNPWF",
"CASKB240727HTKCO",
"CASKB240727JZEDX",
"CASKB240727JYNOU",
"CASKB240727VGAIT",
"CASKB240729SMRPS",
"CASKB240729RRVEB",
"CASKB240727BFIQE",
"CASKB240731KEUYS",
"CASKB240727NCYCY",
"CASKB240729TGUHS",
"CASKB240729HARSH",
"CASKB240727UYOVR",
"CASKB240727XLAED",
"CASKB240727UTFNF",
"CASKB240729SFOPW",
"CASKB240729SSATF",
"CASKB240729GRPDN",
"CASKB240729ORCVH",
"CASKB240729DQMXG",
"CASKB240729XVRNP",
"CASKB240729QADTS",
"CASKB240729UFJBB",
"CASKB240729JYEMS",
"CASKB240729PSVBZ",
"CASKB240729JOBVV",
"CASKB240727BBMNZ",
"CASKB240727KIMYQ",
"CASKB240727XAHBT",
"CASKB240729XUDHN",
"CASKB240729NJNXS",
"CASKB240727FHHWH",
"CASKB240727CAHDN",
"CASKB240727YETSP",
"CASKB240729YRSZD",
"CASKB240729TBOXJ",
"CASKB240729JBBQQ",
"CASKB240729URPJZ",
"CASKB240729SLRHV",
"CASKB240727ZPVAR",
"CASKB240730EOSMW",
"CASKB240729RBKYP",
"CASKB240729TOIIW",
"CASKB240729GITPC",
"CASKB240730QLDQG",
"CASKB240730TBIXR",
"CASKB240730SBXUA",
"CASKB240727OFOYT",
"CASKB240727CMLGT",
"CASKB240727FGJBL",
"CASKB240727XCMHE",
"CASKB240727WMULS",
"CASKB240727COZCN",
"CASKB240730VXTSQ",
"CASKB240729WZXJK",
"CASKB240729BDAAJ",
"CASKB240730DXAVT",
"CASKB240729JDMAP",
"CASKB240727HLICC",
"CASKB240729TLUEF",
"CASKB240730IFHVX",
"CASKB240727FAAWD",
"CASKB240730HCAAT",
"CASKB240730AWKOV",
"CASKB240729EWFWX",
"CASKB240729ZTIBH",
"CASKB240727GNCAL",
"CASKB240729WYJAO",
"CASKB240729RFVKJ",
"CASKB240727PAQQJ",
"CASKB240729XBCZB",
"CASKB240730YZQBQ",
"CASKB240727VUUOB",
"CASKB240727CVCFO",
"CASKB240727FYWYB",
"CASKB240727KSQDJ",
"CASKB240727QAHCI",
"CASKB240727HQXLR",
"CASKB240727MOOIR",
"CASKB240727VAKBD",
"CASKB240729LYSXF",
"CASKB240727IHWRU",
"CASKB240727BKDOH",
"CASKB240727QIFUR",
"CASKB240727XVIAT",
"CASKB240727JUKZK",
"CASKB240727DBKIH",
"CASKB240727ADKGQ",
"CASKB240727DGDYJ",
"CASKB240729YEGMZ",
"CASKB240729NFNHM",
"CASKB240727DOBGF",
"CASKB240727EUCMK",
"CASKB240727UECLM",
"CASKB240727DICHY",
"CASKB240727TSXSY",
"CASKB240727IDRQO",
"CASKB240727RSGLS",
"CASKB240727VUODG",
"CASKB240727XCNNI",
"CASKB240727DAPRG",
"CASKB240727YKAJY",
"CASKB240727THLNP",
"CASKB240727JRATQ",
"CASKB240727QQBZS",
"CASKB240727WOKRH",
"CASKB240729EUYPP",
"CASKB240727NQLNN",
"CASKB240727HXLDS",
"CASKB240727GAGHB",
"CASKB240727VLWTD",
"CASKB240729TEMHJ",
"CASKB240727TTEJN",
"CASKB240727KCDEV",
"CASKB240729PDCZN",
"CASKB240729FIXDT",
"CASKB240729EYTSS",
"CASKB240727RKIDH",
"CASKB240727TVBYJ",
"CASKB240727FJDPD",
"CASKB240727NGDQM",
"CASKB240727ICKOD",
"CASKB240727PPSHW",
"CASKB240727THBZT",
"CASKB240727QUYNT",
"CASKB240727EVAQI",
"CASKB240727BORML",
"CASKB240727POJAI",
"CASKB240807JESNI",
"CASKB240807GDMNH",
"CASKB240807TDLGJ"
    ]

    resume_hercules_task(partner_loan_ids, "KBL")

    print('\n\nDisbursal Already Completed Partner Loan Ids:', already_completed_partner_loan_id)
    print('Disbursal Resumed Partner Loan Ids:', resumed_partner_loan_id)
    print('Disbursal Failed Partner Loan Ids:', failed_resumed_partner_loan_id)
    print('Disbursal Other Status Partner Loan Ids:', other_status_partner_loan_id)
    print('Invalid Resume Task Partner Loan Ids:', invalid_resume_task_partner_loan_id)
