from encoder import encoder
from decoder import decoder


def user_menu():
    print("Menu")
    print("-------------")
    print("1.Encode")
    print("2.Decode")
    print("3.Quit")
    return


for __name__ in "__main__":
    user_play = True
    while user_play:
        user_menu()
        user_input = int(input("Please enter an option:"))
        if user_input == 1:
            password = (input("Please enter your password to encode:"))
            password = encoder(password)
            print("Your password has been encoded and stored!")
        if user_input == 2:
            password = decoder(password)
        if user_input == 3:
            break
