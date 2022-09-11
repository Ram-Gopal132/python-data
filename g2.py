

import pgzrun

HEIGHT=500
WIDTH=800

box=rect((50,50),(100,100))
def draw():
    screen.fill('white')
    screen.draw.rect(box,'red')

def update():
    box.x+=3
    if box.x<WIDTH:
        box2.x-=3
        if box2.x<HEIGHT:
            box2.x-=4
pgzrun.go()
