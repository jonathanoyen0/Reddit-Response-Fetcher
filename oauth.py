import json
import requests
import time

#checks if the currents token is within its life time, to prevent unnecassary retrevial of tokens from API
def check_current_token(token_file):
    if time.time() < token_file["time_created"] + token_file["lifetime"] + 60:
        return True
    else:
        return False

#Uses a file named 'pw.json' and to store the values 
def get_oauth_token():
    #Checking to see if we even need token
    token_file = json.load(open("oath_token.json", 'r+'))
    if (check_current_token(token_file=token_file)):
        return token_file["token"]
    
    #getting token if we need it
    secrets = json.load(open("secrets.json"))
    auth = requests.auth.HTTPBasicAuth(secrets["CLIENT_ID"], secrets["CLIENT_SECRET"])
    data = json.load(open("pw.json", 'r'))
    headers = {"User-agent": secrets["USER_AGENT"]}
    try:
        response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        if(response.status_code == 200):
            print("Got oath token")
            token_file["token"] = response["access_token"]
            token_file["time_created"] = time.time()
            token_file["lifetime"] = response["expires_in"]
            json.dump(token_file, open("oath_token.json", 'w'), indent=4)
            return response.json()
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

