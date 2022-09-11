from turtle import *
speed('fastest')
colors=['red','green','silver']
pensize(7)
for i in range(50,0,-1):
    pencolor(colors[i%3])
    forward(100)
    left(360/12)
    dot(i*100)
    
mainloop()