import requests
import json

#returns the newest reddit post on a given subreddit, returns response from api in json
def get_random_post(id = None):
    headers = {
        "Authorization": json.load(open("oath_token.json", 'r'))["token"],
        "User-Agent": json.load(open("secrets.json", 'r'))["USER_AGENT"]
    }
    try:
        if id:
            response = requests.get(f"https://oauth.reddit.com/r/all/new.json?after={id}", headers=headers)
        else:
            response = requests.get("https://oauth.reddit.com/r/all/new.json", headers=headers)
        if response.status_code == 200:
            print("got post")
            return response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

