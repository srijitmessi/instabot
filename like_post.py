from const import BASE_URL, APP_ACCESS_TOKEN
import requests


def like_post(username):
    q = raw_input("Search user by name: ")
    req_url = BASE_URL + "users/search?q=" + q + "&access_token=" + APP_ACCESS_TOKEN

    user = requests.get(req_url).json()
    if not user['data']:
        print "No users found."
        exit()
    else:
        user_username = user['data'][0]['username']
        print user_username

    if user_username != 0:
        req_url = BASE_URL + "users/" + user_username + "/?access_token=" + APP_ACCESS_TOKEN
    else:
        exit()

