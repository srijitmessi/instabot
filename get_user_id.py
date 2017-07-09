#
#   Two functions in this file will fetch user's id and username after searching.
#

from const import BASE_URL, APP_ACCESS_TOKEN
from validate import validate_char
import requests


def get_user_username():

    q = raw_input("Search user by name: ")
    q = validate_char(q)
    req_url = BASE_URL + "users/search?q=" + q + "&access_token=" + APP_ACCESS_TOKEN

    user = requests.get(req_url).json()
    if not user['data']:
        print "No users found."
    else:
        user_username = user['data'][0]['username']
        print user_username
        return user_username
    return 0


def get_user_id(username):
    if username == 0:
        exit()

    req_url = BASE_URL + "users/search?q=" + username + "&access_token=" + APP_ACCESS_TOKEN

    user = requests.get(req_url).json()
    if not user['data']:
        print "No users found."
    else:
        print user['data'][0]['id']
        return user['data'][0]['id']
    return 0
