import requests
import json

#returns the newest reddit post on a given subreddit, returns response from api in json
def get_random_post(subreddit: str):
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    token_file = json.load(open("oath_token.json", 'r'))
    headers = {
        "Authorization": token_file["token"],
        "User-Agent": json.load(open("secrets.json", 'r'))["USER_AGENT"]
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response = response.json()
            return response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None