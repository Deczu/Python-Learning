import pygame
import sys

pygame.init();

rez=(800,600);
screen = pygame.display.set_mode(rez);
paddleSize=(rez[0]/40,rez[1]/5)
ballSize=rez[0]/40;

playerPaddle = pygame.Rect(0,(rez[1]/2) - paddleSize[1]/2,paddleSize[0],paddleSize[1]);
enemyPaddle = pygame.Rect(rez[0]-paddleSize[0],(rez[1]/2) - paddleSize[1]/2,paddleSize[0],paddleSize[1]);
paddleSpeed = 10;

ball = pygame.Rect((rez[0]/2)-ballSize/2,(rez[1]/2)-ballSize/2,ballSize,ballSize);

score=[0,0];

clock = pygame.time.Clock();
delta=0.0

flagX = -2;
flagY = -2;

pygame.display.set_caption('PyPong');

def ballReset(playerScored):
    ball.x=(rez[0]/2)-ballSize/2;
    ball.y=(rez[1]/2)-ballSize/2;
    score[playerScored]+=1;
    print(score)

def isScored():
    if ball.x > rez[0]:
        ballReset(0);
    elif ball.x < 0:
       ballReset(1);


def render():
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),playerPaddle);
    pygame.draw.rect(screen,(255,255,255),enemyPaddle);
    pygame.draw.rect(screen,(255,0,0),ball);
    sys_font = pygame.font.SysFont("None",60)
    text=str(score[0])+":"+str(score[1]);
    rendered = sys_font.render(text,0,(25,215,255))
    screen.blit(rendered,((rez[0]/2)-60,0))
    pygame.display.update();
    pygame.display.flip();


while True:
    #Handle events like closing window etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0);
    #Score on top

    #Tick to slow down loop for framerate
    delta += clock.tick()/1000.0;
    while delta > 1/50.0:

        #Check for input
        keys = pygame.key.get_pressed();
        if keys[pygame.K_s]:
            playerPaddle.y+=paddleSpeed;

        if keys[pygame.K_w]:
            playerPaddle.y-=paddleSpeed;
            
        
        ball.x+=flagX;
        ball.y+=flagY;

        if flagY > 0:
            enemyPaddle.y+=paddleSpeed-2;
        elif flagY < 0:
            enemyPaddle.y-=paddleSpeed+2;

        if ball.x > playerPaddle.x and ball.x < playerPaddle.x+paddleSize[0]+4 and ball.y > playerPaddle.y and ball.y < playerPaddle.y+paddleSize[1]+4:
            flagY=abs(flagY)+1;
            flagX=flagX*-1;
            
        if ball.x > enemyPaddle.x-paddleSize[0] and ball.x < enemyPaddle.x:
            flagY=abs(flagY)+1;
            flagX=flagX*-1;
            
        #ball bumps side of field;
        if ball.y < 0:
            flagY = flagY * -1;
        if ball.y > rez[1]-ballSize:
            flagY = flagY * -1;

        delta -= 1/50.0;

    #Check if paddle want to go OoB
    if playerPaddle.y < 0:
        playerPaddle.y = 0;
    if playerPaddle.y > rez[1]-paddleSize[1]:
        playerPaddle.y = rez[1]-paddleSize[1]

    if enemyPaddle.y < 0:
        enemyPaddle.y=0;
    if enemyPaddle.y > rez[1]-paddleSize[1]:
        enemyPaddle.y = rez[1]-paddleSize[1]


    #check for collisions heuiehqwekqwujen FAU
    sumScore=sum(score);
    isScored();
    if sum(score) > sumScore:
        sumScore = sum(score);
        if flagY > 0:
            flagY = 2;
        else:
            flagY = -2;


    #Draw rect etc.
    render();
