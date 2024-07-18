message = input("Hello World ! This is a test. Give me a message that you would like to share...   ")

print("Here is your message: " + message)

print("Now lets play Rock-Paper-Scissors")

play=True
while play==True:
    from random import randint

    print ("hello! and welcome")
    player=input("rock(r), paper(p), or scissors(s)? ")
    print(player, "vs")

    chosen=randint(1,3)

    if chosen==1:
        computer='r'
    elif chosen==2:
        computer='p'
    else:
        computer='s'
    print(computer)

    if player==computer:
        print("Draw")
    elif player=='r' and computer=='s' or player=='s' and computer=='p' or player=='p' and computer=='r':
        print("Player Wins")
    else:
        print("Computer Wins")
    playagain=input("Do you want to play again yes/no? :")
    if playagain=="yes":
        play=True
    elif playagain=="no":
        play=False
    else:
        play=False
