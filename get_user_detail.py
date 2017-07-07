from const import BASE_URL, APP_ACCESS_TOKEN
import requests
import get_user_id
userid = get_user_id()
req_url = BASE_URL + "users/" + userid + "/?access_token=" + APP_ACCESS_TOKEN
print req_url
data = requests.get(req_url)
print len(data['data'])
data = data.json()
print len(data['data'])

if data['meta']['code'] == 200:
    user_name = data['data']['full_name']
    print "Full Name: %s" % user_name
    user_username = data['data']['username']
    print "Username: @%s" % user_username
    user_bio = data['data']['bio']
    print "Bio: %s" % user_bio
else:
    print "Something Went Wrong. :( "
