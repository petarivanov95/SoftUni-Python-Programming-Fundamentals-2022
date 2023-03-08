messages = int(input())


for x in range(messages):
    enter = int(input())

    if enter == 88:
        print("Hello")
    elif enter == 86:
        print("How are you?")
    elif enter < 88 and enter != 86:
        print("GREAT!")
    elif enter > 88:
        print("Bye.")
