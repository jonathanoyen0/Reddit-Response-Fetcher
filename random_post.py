import requests
import json

#returns the newest reddit post on a given subreddit, returns response from api in json
def get_random_post():
    headers = {
        "Authorization": json.load(open("oath_token.json", 'r'))["token"],
        "User-Agent": json.load(open("secrets.json", 'r'))["USER_AGENT"]
    }
    try:
        response = requests.get(f"https://www.reddit.com/r/all/new.json", headers=headers)
        if response.status_code == 200:
            response = response.json()
            return response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

#gets a post with the post id 
def get_id_post(id: str):
    headers = {
        "Authorization": json.load(open("oath_token.json", 'r'))["token"],
        "User-Agent": json.load(open("secrets.json", 'r'))["USER_AGENT"]
    }
    try:
        requests.post(f"https://www.reddit.com/")
    except:
        return
    return None