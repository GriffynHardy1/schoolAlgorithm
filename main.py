# it asks for a inputed letter from the user
decision = input("Do you go to school today? (Y/N) ")
#it now checks what you put as the input
if decision == "Y":
    fperiod = input("Do you go to first period? (Y/N) ")
    if fperiod == "Y":
        felt = input("How did it go? (good/bad) ")
        if felt == "good":
            print("Glad to hear it went well!")
            Rschool = input("Do you go to the rest of school? (Y/N) ")
            if Rschool == "Y":
                print("You have a good day at school.")
            elif Rschool == "N":
                print("You go home early.")
        elif felt == "bad":
            home = input("Sorry to hear that. Do you want to go home? (Y/N) ")
            if home == "Y":
                print("You go home.")
            elif home == "N":
                print("You go to the rest of school.")
    elif fperiod == "N":
        Rclass = input("Which class do you go to: (english, math, or science) ")
        #this checks if it is any one of the 3 choices you couldve made
        if Rclass == "english" or "math" or "science":
            print("You go to", Rclass)
        else:
            #this checks if it is even a choice
            print("Invalid class. Please choose between english, math, or science.")
else:
    #this checks whether the first decision was a N
    decision2 = input("Do you sleep or play games? (games/sleep) ")
    if decision2 == "sleep":
        print("You sleep.")
        wake = input("You wake up later. What do you want to do? (sleep/sleepMore/eat) ")
        #this checks if it is any of the sleeps that you chose
        if wake == "sleepMore" or "sleep":
            print("You sleep more.")
        elif wake == "eat":
            decision3 = input("You eat. Now what? (sleep/game) ")
            if decision3 == "sleep":
                print("You sleep.")
            elif decision3 == "game":
                print("You game.")
    elif decision2 == "games":
        game = input("What game do you play? ")
        print("You play", game)
