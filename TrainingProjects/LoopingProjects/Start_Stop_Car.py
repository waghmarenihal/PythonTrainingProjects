# Logic for executing Car commands.
while 1:
    command = str.lower(input("> "))
    if command=="start":
        print("Car Started... Enjoy Your Ride...")
    elif command=="stop":
        print("Car Stoped... Thanks for Riding...")
    elif command=="quit":
        print("Enjoy your day. Bye !!!")
        break
    else:
        print("Sorry I didn't get that !")

