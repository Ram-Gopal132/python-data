import pgzrun

HEIGHT=500
WIDTH=500

alienb=Actor('character_0001',pos=(200,200))
alieng=Actor('character_0012',topleft=(50,50))

def draw():
    screen.fill('white')
    alienb.draw()
    alieng.draw()
def update():
    alienb.y+=1
    if alienb.y>HEIGHT:
        alienb.y=0
pgzrun.go()