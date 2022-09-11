import pgzrun
HEIGHT=500
WIDTH=500

alienb=Actor('character_0002',pos=(300,50))
alieng=Actor('character_0001',topleft=(0,0))
speed=3
def draw():
    screen.fill("white")
    alieng.draw()
    alienb.draw()
    
def update():
    alieng.x+=1
    if alieng.x>WIDTH:
        alieng.x=0
    if keyboard.left:
        alienb.x-=speed
    if keyboard.left:
        alienb.x+=speed
    if keyboard.left:
        alienb.y-=speed
    if keyboard.left:
        alienb.y+=speed
#    if alienb.colliderect(alieng):
#        sounds.sound1.play()
pgzrun.go()