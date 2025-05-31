import pygame 
import random
import time
# rajini style birthday 
# 21 nov 2024

SCREENWIDTH=800
SCREENHEIGHT=600
class Brick():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=60
        self.height=20
        self.color=(106,14,186)
    
    def disbrick(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        
class Ball():
    def __init__(self):
        self.x=SCREENWIDTH/2
        self.y=SCREENHEIGHT-150
        
        self.radius=10
        
        self.color=(147,8,182)
        
        self.dx=random.choice([-5,5])
        self.dy=-5                           # (-1)*(random.choice(list(range(1,10))))
            
    def disball(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    
    def move(self):
        self.x+=self.dx
        self.y+=self.dy
    
    def collisiondetectionwithwall(self):
        if self.x<0 or self.x>SCREENWIDTH-self.radius*2:
            self.reflectionlaws("x")
        if self.y<0:
            self.reflectionlaws("y")
    
    def colpad(self,paddle):
        if paddle.x+paddle.width/2 > self.x>paddle.x:
            if paddle.y+paddle.height>(self.y+self.radius)>paddle.y:
                self.dx=(-1)*abs(self.dx)
                self.reflectionlaws("y")
                
        elif paddle.x+paddle.width > self.x>paddle.x+paddle.width/2:
            if paddle.y+paddle.height>(self.y+self.radius)>paddle.y:
                self.reflectionlaws("y")
                self.dx=abs(self.dx)
                
    def breakbrick(self,bricks,gamescore):
        for brick in bricks:
            if brick.x<self.x<brick.x+brick.width:
                if brick.y<self.y<brick.y+brick.height:
                    bricks.remove(brick)
                    self.reflectionlaws("y")
                    gamescore["score"]+=10
                
           
    def reflectionlaws(self,xory):
        if xory=="x":
            self.dx=-self.dx
            # print("x bounce: ",self.dx)
        if xory=="y":
            self.dy=-self.dy
            # print("y bounce: ",self.dy)
            
class Paddle():
    def __init__(self):
        
        self.x=SCREENWIDTH/2
        self.y=SCREENHEIGHT-100
        
        self.width=200
        self.height=10
        
        self.colorleft=(255,0,140)
        self.colorright=(245,48,252)
        
        self.speed=10
    def move(self,direction,acceleration=1):
        if direction=="left" and self.x>0:
            self.x-=self.speed*acceleration
        if direction=="right" and self.x<SCREENWIDTH-self.width:
            self.x+=self.speed*acceleration
        
    def dispaddle(self,screen):
        pygame.draw.rect(screen,self.colorleft,(self.x,self.y,self.width/2,self.height))
        pygame.draw.rect(screen,self.colorright,(self.x+self.width/2,self.y,self.width/2,self.height))
        
class Breakout():
    def __init__(self,name):
        pygame.init()
        pygame.display.set_caption(name)
        self.screen=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        self.clock=pygame.time.Clock()
        
    def rungame(self):
        lastkeytime={"a":0,"d":0}
        doublepressthreshhold=0.2
        loopcon=True
        while loopcon==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    loopcon=False
                    return "quit"
                if event.type==pygame.KEYDOWN:
                    keyname=pygame.key.name(event.key)
                    if keyname in lastkeytime:
                        currenttime=time.time()
                        if (currenttime-lastkeytime[keyname])<=doublepressthreshhold:
                            if keyname=="a":
                                self.paddle.move("left",15)
                            if keyname=="d":
                                self.paddle.move("right",15)
                            # print("double tap wohooo ",keyname)
                        lastkeytime[keyname]=currenttime
                        
            keys=pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.paddle.move("left")
            if keys[pygame.K_d]:
                self.paddle.move("right")
                
            self.ball.move()
            if self.ball.y>SCREENHEIGHT:
                # pygame.quit()
                return "failed"
            if len(self.bricks)==0:
                # pygame.quit()
                return "won"
                
            self.ball.collisiondetectionwithwall()
            self.ball.colpad(self.paddle)
            self.ball.breakbrick(self.bricks,self.gamescore)
            self.display()
            self.paddle.dispaddle(self.screen)
            self.ball.disball(self.screen)
            
            for brick in self.bricks:
                brick.disbrick(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        print("yo score is: ",self.gamescore["score"])
        
        
    def display(self):
        self.screen.fill((233,200,255))
        
    def popobj(self):
        self.paddle=Paddle()
        self.ball=Ball()
        self.bricks=[]
        self.gamescore={"name":"name","score":0}
        for coloumb in range(10):
            for row in range(10):
                x=coloumb*82
                y=row*30
                # print(f"placing brick at pixel x,y: {row,coloumb}")
                brick=Brick(x,y)
                self.bricks.append(brick)
                
def showenddialog(game, message):
    # Clear the screen
    game.screen.fill((23,34,56))
    
    font = pygame.font.Font(None, 36)
    
    # Render the message
    text = font.render(message, True, (123,45,234))
    text_rect = text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 50))
    game.screen.blit(text, text_rect)
    # Render instructions to restart or quitaaaad
    restart_text = font.render("Press R to Restart or Q to Quit", True, (234,32,43))
    restart_text_rect = restart_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50))
    game.screen.blit(restart_text, restart_text_rect)
    pygame.display.flip()        
        
        
def endgame(game,verdict):
    if verdict=="won":
        showenddialog(game,f"YOU WON LETS GO: {game.gamescore["score"]}")
    elif verdict=="failed":
        showenddialog(game,f"you lost, failure.: {game.gamescore["score"]}")
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                     return "restart"
                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
    return None
              
    
if __name__=="__main__":
    while True:
        game=Breakout("rajini")
        game.popobj()
        verdict=game.rungame()
        useraction=endgame(game,verdict)
        if useraction!="restart":
            break
        
    # print("score: ",game.gamescore["score"])