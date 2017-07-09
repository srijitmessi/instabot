#
#   VALIDATING INPUT VALUES PROVIDED BY USER.
#   Validate(verb) - Verification that something is correct or conforms to a certain standard.
#
#   In Instabot we need these two validations only.
#   Integer Validation - No float/character allowed.
#   Character Validation -  No whitespaces allowed.
#


def validate_int(value):
    while not str.isdigit(value):
        value = raw_input("Please enter a number.")
    return int(value)


def validate_char(value):
    while len(value)==0:
        value = raw_input("Please enter something.")
    while value.isspace():
        value = raw_input("No whitespaces allowed.")
    return value
