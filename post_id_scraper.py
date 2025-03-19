import requests
import pandas as pd
import random

#This script will randomly select a sample,size 100, of the public subreddits in 'subreddits_public.csv'


#function that will return the newest post on a particular subreddit in JSON format
def get_post(subreddit: str):
    url = "https://www.reddit.com/r/nsfw/new.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("got one")
            return response
        else:
            print("Error: ", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None

df = pd.read_csv("subreddits_public.csv", names=["base10_id","base36_reddit_id","creation_epoch","subreddit_name","subscribers_count"])

all_subs = df["subreddit_name"]



get_post(all_subs[0])