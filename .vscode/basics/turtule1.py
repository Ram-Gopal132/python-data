import turtle
s=turtle.Turtle()
s.getscreen().bgcolor("black")

s.penup()
s.goto(-200,100)
s.pendown()
s.color("red")
s.pensize(2.5)

s.speed(45)
def star(turtle,size):
    if size<=20:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
         turtle.forward(size)
         star(turtle,size/3)
         turtle.left(111)
         turtle.end_fill()
star(s,360)
turtle.done()
