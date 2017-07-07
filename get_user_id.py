from const import BASE_URL, APP_ACCESS_TOKEN
import requests
q = raw_input("Search user by name: ")
req_url = BASE_URL + "users/search?q=" + q + "&access_token=" + APP_ACCESS_TOKEN
print req_url
def get_user_id():
    user = requests.get(req_url).json()
    user_username = user['data'][0]['username']
    print user_username
    return user['data'][0]['id']
