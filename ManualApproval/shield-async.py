import requests
import json
import asyncio
import aiohttp

pids = []

with open('./pid.txt', 'r') as f:
    for line in f.readlines():
        pids.append(line.strip())


async def findByPartnerLoanId(session, pid):
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
  }
  url = "https://shield.creditsaison.in/api/v1/appForm/findByPartnerLoanId/" + pid
  await asyncio.sleep(0.1)
  async with session.get(url, headers= headers) as response:
        return await response.json()

async def lastTarsTask(session, wid):
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
  }
  url = "https://tars.creditsaison.in/api/v1/processHistory/" + wid
  await asyncio.sleep(0.1)
  async with session.get(url, headers= headers) as response:
        return await response.json()

async def fetch_appform_details(pids):
    connector = aiohttp.TCPConnector(verify_ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        appformTasks = []
        for pid in pids:
            appformTasks.append(findByPartnerLoanId(session, pid))
        appforms = await asyncio.gather(*appformTasks)
        historyTasks = []
        completed = []
        pendings = []
        for appform in appforms:
            if appform.get('appFormStatus') == '15':
                completed.append(appform)
            else:
              pendings.append(appform)

        for case in completed:
            print(case.get('partnerLoanId'))
        print("15 status", len(completed))
        for pending in pendings:
            if (pending.get('workflowId') != None):  
              historyTasks.append(lastTarsTask(session, pending.get('workflowId')))
        histories = await asyncio.gather(*historyTasks)
        resultList = []
        for i in range(len(pendings)):
            result = {}
            try:
              result['appformId'] = pendings[i].get('id')
              result['partnerLoanId'] = pendings[i].get('partnerLoanId')
              result['workflowId'] = pendings[i].get('workflowId')
              result['appformStatus'] = pendings[i].get('appFormStatus')
              result['applicantId'] = pendings[i]['linkedIndividuals'][0].get('id')
              result['stage'] = pendings[i].get('stage')
              
              result['lastTask']  = 'NA'
              if(len(histories[i].get('execution')) > 0):
                result['lastTask'] = histories[i].get('execution')[-1].get('activityName')
                # result['processInstanceId'] = histories[i].get('execution')[-1].get('processInstanceId')
              resultList.append(result)
            except Exception as e :
                print(e);
        return resultList

# Main entry point for the script
if __name__ == "__main__":
    # Run the asyncio event loop
    result = asyncio.run(fetch_appform_details(pids))
    with open('/Users/aadarshpanwar/Downloads/kbl-pending-gc.json', 'w', encoding='utf-8') as f:
      json.dump(result, f, ensure_ascii=False, indent=4)
    # f = open("lastTaskName.csv", "w")
    # f.write("workflowId, name, type\n")

    # for appform in appforms:
    #   if(len(appform.get('execution')) > 0):
    #     row = appform.get('execution')[-1].get('processInstanceId') + "," + appform.get('execution')[-1].get('activityName') + "," + appform.get('execution')[-1].get('activityType')+"\n"
    #     f.write(row)
    # f.close()