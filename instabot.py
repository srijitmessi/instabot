from get_user_id import get_user_id, get_user_username
from get_own_details import get_own_details
from get_user_detail import get_user_detail
from get_recent_media import get_recent_media
from like_post import like_post
from post_comment import post_comment
from get_comments import get_comments
import validate
import requests


print "\n\t\tInstaBot \n\t\tversion 1.0.0\n"
try:
    x = requests.get("https://google.com")
except:
    print "No Network Connection.\n Try Running Windows Network Diagnostics. "
    exit()

while True:
    print "1. Get active account's instagram info.\n2. Get any other's information. \n3. Get recent post. \n4. Like recent post. \n5. Leave comment on recent post. \n6. View comments.\n7. Exit."
    choice = raw_input("What do you want to do? ")
    choice = validate.validate_int(choice)

    if choice == 1:
        get_own_details()
    elif choice == 2:
        user = get_user_username()
        id = get_user_id(user)
        get_user_detail(id)
    elif choice == 3:
        user = get_user_username()
        id = get_user_id(user)
        get_recent_media(id)
    elif choice == 4:
        user = get_user_username()
        like_post(user)
    elif choice == 5:
        user = get_user_username()
        post_comment(user)
    elif choice == 6:
        user = get_user_username()
        get_comments(user)
    else:
        exit()
