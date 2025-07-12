from pygame import *
init()
from random import *

screen = display.set_mode((800, 600))

display.set_caption("PING PONG")

running = True

field = image.load("поле.jpg") 
field = transform.scale(field, (800, 600))

player =  image.load("игрок.png")  
player = transform.scale(player, (60, 100))

enemy = image.load("враг.png")  
enemy = transform.scale(enemy, (60, 100))

ball = image.load("image.png") 
ball = transform.scale(ball, (60, 60))



class Ball():
    
    def __init__(self,x,y):
        self.hitbox = ball.get_rect(center=(x, y))
        self.speed = 3
        self.speedx = 1
        self.speedy = 1
        self.pause = False
    def moving(self):
        self.hitbox.x += self.speedx * self.speed
        self.hitbox.y += self.speedy * self.speed
        if self.hitbox.right > 800:
            self.pause = True
            self.speedx = -self.speed
            self.speedy = self.speedy *choice([-1,1])
            playerchik.score += 1
            playerchik.hitbox.centery =  300
            enemymchik.hitbox.centery =  300
            self.hitbox.center = (400, 300)

        if self.hitbox.left < 0:
            self.pause =  True
            self.speedx = self.speed
            self.speedy = self.speedy * choice([-1,1])
            enemymchik.score += 1

            self.hitbox.center = (400, 300)
            playerchik.hitbox.centery =  300
            enemymchik.hitbox.centery =  300
        if self.hitbox.bottom > 600:
            self.speedy = -self.speed
        if self.hitbox.top < 0:
            self.speedy = self.speed


        
ballchik = Ball(400,300)
class PLayer():

    
    def __init__(self,x,y,image,speed):
        self.hitbox = image.get_rect(center = (x , y))
        self.speed = speed
        self.score = 0 
    def moving(self):
        key_list = key.get_pressed()
        if key_list[K_DOWN]:
            self.hitbox.y += self.speed
            if self.hitbox.bottom > 600:
                self.hitbox.bottom= 600
        if key_list[K_UP]:
            self.hitbox.y -= self.speed
            if self.hitbox.top < 0:
    
                self.hitbox.top = 0
    def autopilot(self):
        if self.hitbox.centery < ballchik.hitbox.centery:
            self.hitbox.y += self.speed
        elif self.hitbox.centery > ballchik.hitbox.centery:
            self.hitbox.y -= self.speed



    def collide(self):
        if self.hitbox.colliderect(ballchik.hitbox):
           
            if self.hitbox == playerchik.hitbox:
                ballchik.speedx = ballchik.speed
            else:
                ballchik.speedx = -ballchik.speed

        
            

                   
                 
playerchik = PLayer(100,300,player,10)
enemymchik = PLayer(700,300,enemy,4)

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONDOWN or e.type ==  KEYDOWN:
            ballchik.pause = False


    screen.blit(field, (0, 0))
    screen.blit(ball,ballchik.hitbox)
    screen.blit(player,playerchik.hitbox)
    screen.blit(enemy,enemymchik.hitbox)
    
    
    if ballchik.pause == False:
        playerchik.moving()
        ballchik.moving()
        enemymchik.autopilot()
    else:
        art = font.Font("minecraft_0.ttf",70).render(str(playerchik.score) + " : " + str(enemymchik.score), True,' black')
        art_hitbox = art.get_rect(center = (400, 100))
        screen.blit(art,art_hitbox)
    
    playerchik.collide()
    enemymchik.collide()







    time.Clock().tick(60)
    display.flip()
quit()
