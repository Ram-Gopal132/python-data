import pgzrun
from random import randint

HEIGHT=700
WIDTH=500

score=0
player=Actor('character_0000',pos=(WIDTH//2,HEIGHT//2))
item =Actor('character_0008',pos=(50,50))
speed=3

#music.play('bigmusic')

def draw():
    screen.fill('green')
    player.draw()
    item.draw()
    screen.draw.text(f'SCORE:{score}',topleft=(10,500-30))
    
def update():
    global score
   
    # movement control
    if keyboard.left:
        player.x-=speed
    if keyboard.right:
        player.x+=speed
    if keyboard.up:
        player.y-=speed
    if keyboard.down:
        player.y+=speed
        
        #boundry control
        
    if player.x>WIDTH:
        player.x=0
    if player.x<0:
        player.x=WIDTH
    if player.y>HEIGHT:
        player.y=0
    if player.y<0:
        player.y=HEIGHT
        
        
    # collision control
    
    if player.colliderect(item):
        score+=2**2
        item.x=randint(0,WIDTH)
        item.y=randint(0,HEIGHT)
    
        
pgzrun.go()
        
    


