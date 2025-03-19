import requests
import json

headers = {
    'Authorization': 'Basic VW41R3lPdm5TYkV3OVRmOmVPazBjM1o4N1dta3VqVg=='
  }

def generateURL(url):

  url = f"https://drstrange.creditsaison.in/api/v1/urlGenerator?validity=12000000&url={url}"
  payload = ""
  return requests.request("GET", url, headers=headers, data=payload , verify=False)



urls = []
exUrl = ['https://unorganizedbucket-production-595588206139-ap-south-1.s3.amazonaws.com/propelld/PRP3612382602/PRP3612382602_selfie.png',
         'https://unorganizedbucket-production-595588206139-ap-south-1.s3.amazonaws.com/propelld/PRP3612382602/PRP3612382602_loanAgreement.pdf',
         'https://unorganizedbucket-production-595588206139-ap-south-1.s3.amazonaws.com/propelld/PRP3612382602/PRP3612382602_vkycReport.pdf',
         'https://unorganizedbucket-production-595588206139-ap-south-1.s3.amazonaws.com/propelld/PRP3612382602/PRP3612382602_vkycVideo.mp4',
         'https://unorganizedbucket-production-595588206139-ap-south-1.s3.amazonaws.com/propelld/PRP3612382602/PRP3612382602_poa.png']
for i in exUrl :
  response = generateURL(i)
  if response.status_code == 200:
    urls.append(response.text)
  else:
    print("failed to get url " , i) 
     
# for url in urls:
#   docsList.append({"type":"photo" , "url":url})



docsList =  [
                {
                    "type": "photo",
                    "url": urls[0]
                },
                {
                    "type": "loanAgreement",
                    "url": urls[1]
                },
                {
                    "type": "vkycReport",
                    "url": urls[2]
                },
                {
                    "type": "vkycVideo",
                    "url": urls[3]
                },
                {
                    "type": "poa",
                    "url": urls[4]
                }

            ]

print(json.dumps(docsList))

