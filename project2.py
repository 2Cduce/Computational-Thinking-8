lawfulgood_points = 0
neutralgood_points = 0
chaoticgood_points = 0
lawfulevil_points = 0

answer1 = input("Do you prefer A, your desk facing the door, B facing away from the door, or C facing away from the door in the center of the room, or D no desk?")
if answer1 == "A":
    lawfulgood_points += 3
elif answer1 == "D":
    neutralgood_points += 2
elif answer1 == "B":
    chaoticgood_points += 1
elif answer1 == "C":
    lawfulevil_points = 3

answer2 = input("If you find a piece of trash on the ground what do you do A ignore it, B kick it out of the way, C Pick it up and throw it at someone, or D throw it away")
if answer2 == "D":
    lawfulgood_points += 3
elif answer2 == "A":
    neutralgood_points += 2
elif answer2 == "B":
    chaoticgood_points += 2
elif answer2 == "C":
    lawfulevil_points = 3

answer3 = input("If you see an elderly person struggling to carry groceries what would you do A Nothing, B Help them, C mock them, D Break their bag")
if answer3 == "A":
    lawfulgood_points += 1
elif answer3 == "B":
    neutralgood_points += 1
elif answer3 == "C":
    chaoticgood_points += 1
elif answer3 == "D":
    lawfulevil_points = 1

answer4 = input("")
if answer4 == "A":
    lawfulgood_points += 1
elif answer4 == "B":
    neutralgood_points += 1
elif answer4 == "B":
    chaoticgood_points += 1
elif answer4 == "C":
    lawfulevil_points = 1

answer5 = input("")
if answer5 == "A":
    lawfulgood_points += 1
elif answer5 == "B":
    neutralgood_points += 1
elif answer5 == "B":
    chaoticgood_points += 1
elif answer5 == "C":
    lawfulevil_points = 1

    if lawfulgood_points >= neutralgood_points and lawfulgood_points >= chaoticgood_points and lawfulgood_points >= lawfulevil_points:
     print("Player 1 wins!")
elif neutralgood_points >= lawfulgood_points and neutralgood_points >= chaoticgood_points and neutralgood_points >= lawfulevil_points:
     print("player 2 wins!")

elif chaoticgood_points >= lawfulgood_points and chaoticgood_points >= neutralgood_points and chaoticgood_points >= lawfulevil_points:
     print("Player 3 wins!")

elif lawfulevil_points >= lawfulgood_points and lawfulevil_points >= neutralgood_points and lawfulevil_points >= chaoticgood_points:
     print("Player 4 wins!")