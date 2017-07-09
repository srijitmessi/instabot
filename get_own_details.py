from const import BASE_URL, APP_ACCESS_TOKEN
import requests
def get_own_details():
    req_url = BASE_URL + "users/self/?access_token=" + APP_ACCESS_TOKEN
    print "requesting..."
    data = requests.get(req_url)
    data = data.json()
    if data['meta']['code'] == 200:
        user_name = data['data']['full_name']
        print "\n\nFull Name: %s" % user_name
        user_username = data['data']['username']
        print "Username: @%s" % user_username
        user_bio = data['data']['bio']
        print "Bio: %s" % user_bio
        print "\nHe says Hi! And thanks for checking out this application.\n\n"
    else:
        print "Something Went Wrong. :( "
