# KJ Pressly 76143268

def encoder(password_input):
    encoded_password = ''
    for i in password_input:
        if int(i) >= 7:
            encoded_password += str(int(i) - 7)
        else:
            encoded_password += str(int(i) + 3)
    return encoded_password


