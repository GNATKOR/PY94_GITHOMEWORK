from getters import get_email, get_password


def validator(users):
    while True:
        validator_result = check_account_in_users(users, get_email(), get_password())
        if validator_result:
            print("Hello user!")
            break
        else:
            print("Try again!, or type exit to quit")


def check_account_in_users(users, user_email, user_password):
    for i in users:
        if i['email'] == user_email and i['password'] == user_password:
            return True
    return False
