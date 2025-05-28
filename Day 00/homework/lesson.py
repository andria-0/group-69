
from turtle import *


# we want to paint a house

# step 1: draw a square

width(5)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

# end of square

# drawing a door

forward(80)
left(90)
color("yellow")
begin_fill()
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

# end of door

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
left(180)
left(30)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()

# end a roof

# draw a window

penup()
goto(20,100)
pendown()

color("green")
begin_fill()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

penup()
goto(180,100)
pendown()

begin_fill()
left(180)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

# end of window

exitonclick()