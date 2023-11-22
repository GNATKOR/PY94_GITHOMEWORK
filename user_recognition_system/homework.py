import json
from getters import get_email, get_password
from validators import validator


def registered_users():
    with open('users.json', 'r') as read_file:
        users = json.load(read_file)
    return users


def app():
    while True:
        ans = input("SIGN UP or LOG IN?: ").lower()
        if ans == 'exit':
            quit()
        elif ans == 'log in':
            validator(registered_users())
            break
        elif ans == 'sign up':
            new_user_creation(registered_users())
            break
        else:
            print("Incorrect answer, type log in or sign up, or exit to quit.")


def check_name(users, new_email):
    for i in users:
        if i['email'] == new_email:
            return True
    return False


def new_user_creation(users):
    while True:
        new_email = get_email()
        if check_name(users, new_email):
            print('This username already exist, choose another!')
        else:
            break
    while True:
        password_1 = get_password()
        print('Repeat password')
        password_2 = get_password()
        if password_1 != password_2:
            print('Passwords dont match, try again...')
        else:
            break
    new_user = {'email': new_email, 'password': password_1}
    with open('users.json', 'r') as file:
        users_list = json.load(file)
        users_list.append(new_user)
    with open('users.json', 'w') as json_file:
        json.dump(users_list, json_file)


app()
