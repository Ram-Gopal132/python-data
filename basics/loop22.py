from turtle import *
#speed(2)
sides=7
distance=120
fillcolor('pink')
begin_fill()
for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()
mainloop()