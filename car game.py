command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if not started:
            started = True
            print("car started")
        else:
            print("car already started!")
    elif command == "stop":
        if started:
            started = False
            print("car stopped")
        else:
            print("car already stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("i dont understand that")
