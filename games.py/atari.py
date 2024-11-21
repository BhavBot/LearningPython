import pygame 
import random
# rajini style birthday 
# 21 nov 2024

SCREENWIDTH=800
SCREENHEIGHT=600
class Ball():
    def __init__(self):
        self.x=SCREENWIDTH/2
        self.y=SCREENHEIGHT-150
        
        self.radius=10
        
        self.color=(147,8,182)
        
        self.dx=5
        self.dy=-5
            
    def disball(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
    
    def collisiondetectionwithwall(self):
        if self.x<0 or self.x>SCREENWIDTH-self.radius:
            self.reflectionlaws("x")
        if self.y<0:
            self.reflectionlaws("y")
    
    def colpad(self,paddle):
        if paddle.x+paddle.width > self.x>paddle.x:
            if paddle.y+paddle.height>(self.y+self.radius)>paddle.y:
                self.reflectionlaws("y")
        
        
        
    def reflectionlaws(self,xory):
        if xory=="x":
            self.dx=-self.dx
        if xory=="y":
            self.dy=-self.dy
            
class Paddle():
    def __init__(self):
        
        self.x=SCREENWIDTH/2
        self.y=SCREENHEIGHT-100
        
        self.width=500
        self.height=10
        
        self.color=(255,0,140)
        
        self.speed=10
    def move(self,direction):
        if direction=="left" and self.x>0:
            self.x-=self.speed
        if direction=="right" and self.x<SCREENWIDTH-self.width:
            self.x+=self.speed
        
    def dispaddle(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        
class Breakout():
    def __init__(self,name):
        pygame.init()
        pygame.display.set_caption(name)
        self.screen=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        self.clock=pygame.time.Clock()
        
    def rungame(self):
        loopcon=True
        while loopcon==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    loopcon=False
            keys=pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.paddle.move("left")
            if keys[pygame.K_d]:
                self.paddle.move("right")
                
            self.ball.move()
            self.ball.collisiondetectionwithwall()
            self.ball.colpad(self.paddle)
            self.display()
            self.paddle.dispaddle(self.screen)
            self.ball.disball(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            
    def display(self):
        self.screen.fill((233,200,255))
        
    def popobj(self):
        self.paddle=Paddle()
        self.ball=Ball()
        
        
        
if __name__=="__main__":
    game=Breakout("rajini")
    game.popobj()
    game.rungame()