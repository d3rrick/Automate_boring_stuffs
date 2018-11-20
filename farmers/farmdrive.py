import requests
from requests.auth import HTTPBasicAuth
import json
from requests.auth import HTTPBasicAuth

headers = {'content-type': 'application/json'}

auth = HTTPBasicAuth('john', '674g27BZQaLgvVc5')

def whitelist_f(data,loc):
    pass_data = {
            "location_code": loc,
            "phone_numbers": data
        }
    data = json.dumps(pass_data)
    req = requests.post("https://staging.df.farmdrive.co.ke/farmers/whitelist",data=data, headers=headers,auth=auth)
    return req.text
def verify_f(num):
    req = requests.get(f"https://staging.df.farmdrive.co.ke/farmers/whitelist/{num}", headers=headers,auth=auth)
    return req.text
