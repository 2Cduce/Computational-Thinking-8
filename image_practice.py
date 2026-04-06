# Section 1 - Your code
from utils import *
set_background("house fire")

s1 = create_sprite("Elmo1", 300, 100)
s2 = create_sprite("bat", -100, 100)
s2 = create_sprite("flower", -100, -210)
s2 = create_sprite("cardinal", 100, -100)
s2 = create_sprite("mario", 150, -100)

message1 = create_sprite("alien",-100,288)
message1.color("pink")
message1.write("ciao",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()