from turtle import *
color('red','blue')
speed(0)
#begin_fill()
ht()
for i in range(8):
    #up()
    forward(100)
    left(360/8)
    for i in range(8):
        #down()
        forward(60)
        left(360/8)
#end_fill()

mainloop()