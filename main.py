from random_post import get_random_post
from oauth import get_oauth_token
import random
import json

get_oauth_token()
post = get_random_post().json()
id = post["data"]["after"]

for i in range(1):
    post = get_random_post(id=id).json()
    id = post["data"]["after"]

