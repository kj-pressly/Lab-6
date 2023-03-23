
def decoder(password):
    decoded = ''
    for i in range(0, len(password)):
        if int(password[i]) < 3:
            decoded += str((int(password[i]) + 7))
        else:
            decoded += str((int(password[i]) - 3))
    print("The encoded password is " + password + ", and the original password is " + decoded + ".\n")
    return decoded
