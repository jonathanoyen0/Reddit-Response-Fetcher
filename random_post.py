import requests
import json

#returns the newest reddit post on a given subreddit, returns response from api in json
def get_random_post(id = "None"):
    headers = {
        "Authorization": json.load(open("oath_token.json", 'r'))["token"],
        "User-Agent": json.load(open("secrets.json", 'r'))["USER_AGENT"]
    }
    try:
        if id != "None":
            response = requests.get(f"https://www.reddit.com/r/all/new.json?afer={id}", headers=headers)
        else:
            response = requests.get("https://www.reddit.com/all/new.josn", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

