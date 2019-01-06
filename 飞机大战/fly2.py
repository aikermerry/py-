import pygame
from pygame.locals import *
import time
import random

class Status(object):
    def __init__(self,screen,image,x,y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image).convert()

class PullicByllet(Status):
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def bulletMove(self,num):
        self.y+=num
        
    def judgeOut(self):
        if self.y<0 or self.y>890:
            return True
        else:
            return False

class SatusPlane(Status):
    def __init__(self,screen,image,x,y):
        super(SatusPlane,self).__init__(screen,image,x,y)
        self.image = pygame.image.load(image).convert()
        self.mybullet=[]
        self.HP =100

    def display(self,num):

        balluteNeeedRemoved =[]
        self.screen.blit(self.image,(self.x,self.y))
        for self.shootBullet in self.mybullet:
            self.shootBullet.display()
            self.shootBullet.bulletMove(num)
            if self.shootBullet.judgeOut():
                balluteNeeedRemoved.append(self.shootBullet)  
        for i in balluteNeeedRemoved:
            self.mybullet.remove(i)
            pass
        time.sleep(0.01)

    def Shoot(self,image,numx,numy):
        self.BulletS = PullicByllet(self.screen,image,self.x+numx,self.y+numy)
        self.mybullet.append(self.BulletS)
    
    def shanghai(self):
        self.HP -=5
        if self.HP<0:
            return True
    def panduan(self):



class HeroPlane(SatusPlane):
    def __init__(self,screen):
        image ="./feiji/hero.gif"
        super(HeroPlane,self).__init__(screen,image,x=230,y=600)

    def lift(self):
        self.x-=10

    def right(self):
        self.x+=10

    def up(self):
        self.y-=10
        
    def down(self):
        self.y+=10
       
    def shoot(self):
        image="./feiji/bullet-3.gif"
        super(HeroPlane,self).Shoot(image,40,-20)

class EnemyPlane(SatusPlane):
    def __init__(self,screen):
        image ="./feiji/enemy-3.gif"
        self.biaoshi = True
        super(EnemyPlane,self).__init__(screen,image,x=230,y=0)

    def ememyMove(self):
        if self.biaoshi:
            self.x+=2
            if self.x>480-65:
                self.biaoshi =False
        if not self.biaoshi:
            self.x -=2
            if self.x<0:
                self.biaoshi = True

    def shoot(self):
        image = "./feiji/bullet-1.gif"
        randomBa=random.randint(1,50)
        if randomBa == 25:
            super(EnemyPlane,self).Shoot(image,70,240)

       
if __name__== "__main__":
    screen = pygame.display.set_mode((480,890),0,32)
    image = "./feiji/background.png"
    background = pygame.image.load(image).convert()
    hero =  HeroPlane(screen)
    enemys = EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        enemys.ememyMove()
        hero.display(-2)
        enemys.display(2)
        enemys.shoot()

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
