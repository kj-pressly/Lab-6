# KJ Pressly 76143268

def user_menu():
    print("Menu")
    print("-------------")
    print("1.Encode")
    print("2.Decode")
    print("3.Quit")
    return


encoder = True

while encoder:
    user_menu()
    user_input = int(input("Please enter an option:"))
    if user_input == 1:
        password_input = (input("Please enter your password to encode:"))
        encoded_password = ''
        for i in password_input:
            if int(i) >= 7:
                encoded_password += str(int(i) - 7)
            else:
                encoded_password += str(int(i) + 3)
        print("Your password has been encoded and stored!")
    if user_input == 2:
        decoded_password = ''
        for i in encoded_password:
            if int(i) < 3:
                decoded_password += str(int(i) + 7)
            else:
                decoded_password += str(int(i) - 3)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
    if user_input == 3:
        break

