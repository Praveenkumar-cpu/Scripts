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
exUrl = [
    'https://unorganizedbucket-production-595588206139-ap-south-1.s3.ap-south-1.amazonaws.com/document-backup/JPL5cf19f59404b474e836b/5727284_selfie_photo.jpg',
    'https://unorganizedbucket-production-595588206139-ap-south-1.s3.ap-south-1.amazonaws.com/document-backup/JPL5cf19f59404b474e836b/5727284_bureau_report.json',
    'https://unorganizedbucket-production-595588206139-ap-south-1.s3.ap-south-1.amazonaws.com/document-backup/JPL5cf19f59404b474e836b/aadhaar_kyc.xml',
    'https://unorganizedbucket-production-595588206139-ap-south-1.s3.ap-south-1.amazonaws.com/document-backup/JPL5cf19f59404b474e836b/aadhaar_kyc.xml'
]
for i in exUrl :
  response = generateURL(i)
  if response.status_code == 200:
    urls.append(response.text)
  else:
    print("failed to get url " , i)

# for url in urls:
#   docsList.append({"type":"photo" , "url":url})



docsList = [
    {
        "type": "photo",
        "url": urls[0]
    },
    {
        "type": "hard_bureau",
        "url": urls[1]
    },
    {
        "type": "aadhaar",
        "url": urls[2]
    },
    {
            "type": "aadhaar_xml",
            "url": urls[3]
    }
]

print(json.dumps(docsList))
















