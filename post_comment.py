#
#   This function will comment on the selected post.
#   The likes/comments will be done on behalf of @yogesh_biebz
#

from const import BASE_URL, APP_ACCESS_TOKEN
from get_user_id import get_user_id, get_user_username
from get_recent_media import get_recent_media
import requests


def post_comment(username):
    id = get_user_id(username)
    if id != 0:
        pass
    else:
        exit()

    print "Which Post you want to like?"
    post_id = get_recent_media(id)
    text = raw_input("Type in your comment. \n")
    request_url = (BASE_URL + 'media/%s/comments') % (post_id)
    payload = {
        "access_token": APP_ACCESS_TOKEN,
        "text" : text
    }
    print 'POST request url : %s' % request_url
    comment = requests.post(request_url, payload).json()

    if comment['meta']['code'] == 200:
        print 'You commented on post'
    else:
        print 'Something went wrong.'
