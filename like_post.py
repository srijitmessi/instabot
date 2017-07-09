#
#   This function will like the selected post.
#   The likes/comments will be done on behalf of @yogesh_biebz
#

from const import BASE_URL, APP_ACCESS_TOKEN
from get_user_id import get_user_id, get_user_username
from get_recent_media import get_recent_media
import requests


def like_post(username):
    id = get_user_id(username)
    if id != 0:
        pass
    else:
        exit()

    print "Which Post you want to like?"
    post_id = get_recent_media(id)
    request_url = (BASE_URL + 'media/%s/likes') % (post_id)
    payload = {
        "access_token": APP_ACCESS_TOKEN
    }
    print 'POST request url : %s' % request_url
    like = requests.post(request_url, payload).json()

    if like['meta']['code'] == 200:
        print 'Post liked. <3'
    else:
        print 'Cannot like post due to some error.'
