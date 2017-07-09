from const import BASE_URL, APP_ACCESS_TOKEN
import requests
from get_user_id import get_user_username


def get_user_detail(userid):

    if userid != 0:
        req_url = BASE_URL + "users/" + userid + "/?access_token=" + APP_ACCESS_TOKEN
    else:
        print "User does not exist."
        exit()
    print "request: " + req_url
    data = requests.get(req_url)
    data = data.json()
    if data['meta']['code'] == 200:
        if len(data['data']) > 0:
            user_name = data['data']['full_name']
            print "\n\nFull Name: %s" % user_name
            user_username = data['data']['username']
            print "Username: @%s" % user_username
            user_bio = data['data']['bio']
            print "Bio: %s" % user_bio
            print "\n\n"
    else:
        print "Something Went Wrong. :( "
