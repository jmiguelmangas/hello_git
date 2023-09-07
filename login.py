import sys

userdata = [
    {"username": "pepito", "password": "123456"},
    {"username": "juanito", "password": "665544"},
]


def ask_username_password():
    username = input("Username: ").lower()
    password = input("Password: ").lower()
    return (username, password)


def check_user_password(login):
    username, password = login
    for user in userdata:
        if user["username"] == username:
            if user["password"] == password:
                return True
            else:
                sys.exit("Incorrect Password")
    sys.exit("Incorrect User")


def main():
    print("Login V3")
    login = ask_username_password()
    if check_user_password(login):
        print(f"Hello {login[0].capitalize()} welcome to the system")


if __name__ == "__main__":
    main()
