from turtle import *

colors=['red']
pensize(21)
for i in range(6):
    pencolor(colors[i%1])
    forward(100)
    left(360/6)
    circle(40)
    
mainloop()