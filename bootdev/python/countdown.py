def countdown_to_start():
    time = 10
    while time > 0:
        timeprint = f"{time}..."
        print(timeprint)
        time = time - 1
    else:
        print("Fight!")

# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()