import requests
from oath import get_oath_token
import json

def get_random_post(subreddit: str):
    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    headers = {
        "Authorization": get_oath_token()["access_token"],
        "User-Agent": json.load(open("secrets.json", 'r'))["USER_AGENT"]
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("We did it")
            response = response.json()
            print(response)
            return response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None