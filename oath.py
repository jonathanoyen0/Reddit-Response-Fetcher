import json
import requests

#Uses a file named 'pw.json' and to store the values 
def get_oath_token():
    secrets = json.load(open("secrets.json"))
    auth = requests.auth.HTTPBasicAuth(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
    data = json.load(open("pw.json", 'r'))
    headers = {"User-agent": secrets["USER_AGENT"]}
    try:
        response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        if(response.status_code == 200):
            print("Got oath token")
            response = response.json()
            return response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None
