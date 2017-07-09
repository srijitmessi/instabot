from get_user_id import get_user_id, get_user_username
from get_own_details import get_own_details
from get_user_detail import get_user_detail
from get_recent_media import get_recent_media
import validate

print "\n\t\tInstaBot \n\t\tversion 1.0.0\n"

while True:
    print "1. Get developer's instagram info.\n2. Get any other's information. \n3. Get recent post. \n4. Like recent post. \n5. Leave comment on recent post. \n6. Exit."
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
    else:
        exit()
