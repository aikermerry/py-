import pygame
from pygame.locals import *
import time
import random
class Bullet(object):
    def __init__(self,screen,x,y):
        self.x = x+40
        self.y =y-20
        self.screen = screen
        self.bullet=pygame.image.load("./feiji/bullet-3.gif").convert()
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def bulletMove(self):
        self.y-=2
    def judgeOut(self):
        if self.y<=30:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self,screen,x,y):
        self.x = x+70
        self.y =y+246
        self.screen = screen
        self.bullet=pygame.image.load("./feiji/bullet-1.gif").convert()
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def bulletMove(self):
        self.y+=1
    def judgeOut(self):
        if self.y>=890:
            return True
        else:
            return False

class EnemyPlane(object):
    def __init__(self,screen):
        self.x= 230
        self.y = 0
        self.screen = screen
        self.biaoshi =True
        self.mybullet=[]
        self.enemy = pygame.image.load("./feiji/enemy-3.gif").convert()
    
    def display(self):
        self.screen.blit(self.enemy,(self.x,self.y))
        balluteNeeedRemoved =[]
        
        for shootBullet in self.mybullet:
            shootBullet.display()
            shootBullet.bulletMove()
            if shootBullet.judgeOut():
                balluteNeeedRemoved.append(shootBullet)
        for i in balluteNeeedRemoved:
            self.mybullet.remove(i)
           
    
    def ememyMove(self):
        if self.biaoshi:
            self.x+=2
            if self.x>480-65:
                self.biaoshi =False
        if not self.biaoshi:
            self.x -=2
            if self.x<0:
                self.biaoshi = True

    def enemyShoot(self):
        randomBa=random.randint(1,100)
        if randomBa == 50:
            self.BulletS = EnemyBullet(self.screen,self.x,self.y)
            self.mybullet.append(self.BulletS)




class HeroPlane(object):
    def __init__(self,screen):
        self.myfly = pygame.image.load("./feiji/hero.gif").convert()
        self.x = 230
        self.y = 400
        self.screen = screen
        self.mybullet=[]
        
   
    def display(self):

        balluteNeeedRemoved =[]
        self.screen.blit(self.myfly,(self.x,self.y))
        for self.shootBullet in self.mybullet:
            self.shootBullet.display()
            self.shootBullet.bulletMove()
            if self.shootBullet.judgeOut():
                balluteNeeedRemoved.append(self.shootBullet)
                
        for i in balluteNeeedRemoved:
            self.mybullet.remove(i)
            pass
        time.sleep(0.01)

    def lift(self):
        self.x-=10
    def right(self):
        self.x+=10
    def up(self):
        self.y-=10
        
    def down(self):
        self.y+=10
       
    def shoot(self):
        self.BulletS = Bullet(self.screen,self.x,self.y)
        self.mybullet.append(self.BulletS)



       
if __name__== "__main__":
    screen = pygame.display.set_mode((480,890),0,32)
    imageFile = "./feiji/background.png"
    background = pygame.image.load(imageFile).convert()
  
    hero =  HeroPlane(screen)
    enemys = EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        enemys.ememyMove()
        hero.display()
        enemys.display()
        enemys.enemyShoot()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
             
                if event.key == K_a:
                    hero.x -=10
                elif event.key == K_d:
                    hero.x+=10
                elif event.key == K_w:
                    hero.y-=10
                elif event.key == K_s:
                    hero.y+=10
                elif event.key == 32:
                    hero.shoot()
                    print("space")
                elif event.key == 27:
                    exit()

        pygame.display.update()
