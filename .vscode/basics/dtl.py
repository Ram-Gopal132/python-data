from turtle import*
speed(0)
#turtle.pos(50,1110)
color('red','yellow')
begin_fill()
while True:
    forward(290)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()