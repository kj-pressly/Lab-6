# KJ Pressly 76143268


def encoder():
    password_input = (input("Please enter your password to encode:"))
    encoded_password = ''
    for i in password_input:
        if int(i) >= 7:
            encoded_password += str(int(i) - 7)
        else:
            encoded_password += str(int(i) + 3)
    print("Your password has been encoded and stored!")
    return encoded_password


