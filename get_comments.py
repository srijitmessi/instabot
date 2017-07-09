#
#   This function will fetch comments on a post.
#   And will display on the screen.
#

from const import BASE_URL, APP_ACCESS_TOKEN
from get_user_id import get_user_id, get_user_username
from get_recent_media import get_recent_media
import requests


def get_comments(username):
    id = get_user_id(username)
    if id != 0:
        pass
    else:
        exit()


    post_id = get_recent_media(id)
    print "Fetching data..."
    req_url = BASE_URL + "media/" + post_id + "/comments/?access_token=" + APP_ACCESS_TOKEN

    comments = requests.get(req_url).json()

    if not comments['data'][0]:
        print "No comments found."
    else:
        query = raw_input("Search for comments having certain keyword? (Leave empty if all comments):  \n")

        if not query:
            for temp in comments['data']:
                print temp['from']['username'] + ": " + temp['text']
        else:
            for temp in comments['data']:
                if temp['data']['text'].find(query) > 0:
                    print temp['from']['username'] + ": " + temp['text']
                else:
                    pass