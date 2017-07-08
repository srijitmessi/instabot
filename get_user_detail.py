from const import BASE_URL, APP_ACCESS_TOKEN
import requests
import get_user_id
user_id = get_user_id.get_user_id()
if user_id != 0:
    req_url = BASE_URL + "users/" + user_id + "/?access_token=" + APP_ACCESS_TOKEN
else:
    exit()
print "request: " + req_url
data = requests.get(req_url)
data = data.json()
if data['meta']['code'] == 200:
    if len(data['data'])>0 :
        user_name = data['data']['full_name']
        print "Full Name: %s" % user_name
        user_username = data['data']['username']
        print "Username: @%s" % user_username
        user_bio = data['data']['bio']
        print "Bio: %s" % user_bio
else:
    print "Something Went Wrong. :( "
