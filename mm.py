def mm():
    while True:
        user_in = float(input('mm: '))
        if user_in == 0:
            break
        print("inches: ", user_in / 25.4)


if __name__ == "__main__":
    mm()
