# Logic for executing Car commands.
print("If you are running for first time, type 'help' to see commands")
started=False
stopped=False
while 1:
    command = str.lower(input("> "))
    if command=="start":
        if started==True:
            print("Car already started.")
        else:
            started=True
            stopped=False
            print("Car Started... Enjoy Your Ride...")
    elif command=="stop":
        if stopped==True:
            print("Car already Stopped")
        else:
            stopped=True
            started=False
            print("Car Stopped... Thanks for Riding...")
    elif command=="quit":
        print("Enjoy your day. Bye !!!")
        break
    elif command=="help":
        print("""
        start   - To Start the Car.
        stop    - To Stop the Car.
        quit    - To Exit this program
        """)
    else:
        print("Sorry I didn't get that !")

