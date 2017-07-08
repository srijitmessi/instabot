import requests
import urllib
from get_user_id import get_user_id
from const import BASE_URL, APP_ACCESS_TOKEN

user_id = get_user_id()

if user_id != 0:
    req_url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + APP_ACCESS_TOKEN
else:
    exit()


data = requests.get(req_url).json()
print data['data'][0]['id']
img_url = data['data'][0]['images']['standard_resolution']['url']

#   Downloading the image.
urllib.urlretrieve(img_url, 'hey.jpg')


