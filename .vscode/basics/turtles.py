from turtle import *

bgcolor('black')
speed(64)
hideturtle()
for i in range(140):
    color('green')
    circle(i)

    
    color('orange')
    color('blue')
    begin_fill()
    circle(40,80)
    end_fill()
    color('yellow')
    #circle(i*0.8)
    right(45)
    #left(5)
    color('red')
    begin_fill()
    forward(55)
    end_fill()
    
done()    
    