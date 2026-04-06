import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 270
x2 = -300
y2 = 100
x3 = -300
y3 = 0
x4 = -300
y4 = -100

# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("moon")
t1 = create_sprite("turtle2",x1,y1)
t2 = create_sprite("soccerball",x2,y2)
t3 = create_sprite("turtle2",x3,y3)
t4 = create_sprite("turtle2",x4,y4)



# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower

# Each sprite is random to add more randomness to who wins I find sprite 2 or 3 wins
for i in range(55):
     x1 += random.randint(10,20)
     x2 +=random.randint(3,26)
     x3 +=random.randint(6,23)
     x4 +=random.randint(7,24)

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     s5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
     s5.write("player 2 wins!")

elif x3 >= x1 and x3 >= x2 and x3 >= x4:
     s5.write("Player 3 wins!")

elif x4 >= x1 and x4 >= x2 and x4 >= x3:
     s5.write("Player 4 wins!")

turtle.exitonclick()