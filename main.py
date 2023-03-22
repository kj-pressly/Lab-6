from encoder import encoder


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
            encoder()
        if user_input == 2:
            pass
        if user_input == 3:
            break

