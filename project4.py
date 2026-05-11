from utils import *

# Section 1 - setup
set_background("Pixlebackround")


#the goal of my game was to make a clicker game and you give bread until you have 15 bread (thats the starter amount) then you can buy fish, then once you have 50 bread you can buy ducks then once you have 100 bread you can buy geese and if by some chance you get 100 geese the backroumd and text would change telling you a goose army destroyed the world: but i never had time for that but I thought it was a pretty cool idea

Bread = 0
cost = 15
Goose = 0
cost = 0

# Section 2 - controls

def get_Bread():
    global Bread 
    Bread += 1
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    create_sprite("Bread",x,y)

def get_Goose():
    global Bread 
    Bread += 1
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    create_sprite("Goose",x,y)

window.onkeypress(get_Bread,"space")
window.onkeypress(get_Goose,"d")

# OPTIONAL: use this invisible alien to say a message
m1=create_sprite("alien",-200,200)
m1.hideturtle()
# Section 3 - game loop
window.listen()
for i in range(1000000000):
    m1.clear()
    m1.write(f"bread: {Bread}\nCost: {cost}\nGoose: {Goose}",font=("Arial",30, "normal")) 

    Bread += Goose

    time.sleep(0.01)
    window.update()