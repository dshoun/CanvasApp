def get_username():
    print("Username:")
    username = input()        # Set to your username.
    return username


def get_password(username):
    print("Password:")
    password = input()        # Set to your username.

    if username == "canvas-shound":
        import base64
        encoded_password = str(base64.b64encode(password.encode("utf-8")))
        return encoded_password[2:-1]
    else:
        return password


def main_menu():
    print("What would you like to do?")
    print("1. Search Course")
    print("2. Search Person")
    print("666. Quit")
    user_input = input()
    return user_input


def course_sub_menu():
    print("What would you like to do?")
    print("1. Make myself a teacher.")
    print("666. Start over.")
    user_input = input()
    return user_input