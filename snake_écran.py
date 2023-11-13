import pygame
import random
pygame.init()

#constants
execute=True
HEIGHT=300
WIDTH=400
CLOCK_FREQUENCY=10
WHITE=(255, 255, 255)
BLACK=(0,0,0)
GREEN=(0,200,0)
RED=(200,0,0)
L=20

#format [ligne,colonne]
Snake=[[9,4],[9,5],[9,6], [9,7], [9,8]]
Apple=[4,5]
#écran
screen = pygame.display.set_mode( ( WIDTH,HEIGHT) )
#directions
up=True
down=False
right=False
left=False
Score=0
clock = pygame.time.Clock()
while execute:

    clock.tick(CLOCK_FREQUENCY)
    #dessiner l'écran
    screen.fill(WHITE)
    i=0
    while i <= HEIGHT:
        j=0
        while j<= WIDTH:
            rect = pygame.Rect(j, i, L, L)
            pygame.draw.rect(screen, BLACK, rect)
            j+=2*L
        i+=L
        j=L
        while j<= WIDTH:
            rect = pygame.Rect(j, i, L, L)
            pygame.draw.rect(screen, BLACK, rect)
            j+=2*L
        i+=L

    #dessiner le serpent
    for serpent in Snake:
        rect = pygame.Rect(serpent[1]*L,serpent[0]*L , L, L)
        pygame.draw.rect(screen, GREEN, rect)
    #dessiner la pomme
    rect = pygame.Rect(Apple[1]*L,Apple[0]*L , L, L)
    pygame.draw.rect(screen, RED, rect)

    
    #déplacer le serpent
    head=Snake[0]
    if up:
        Snake=[[head[0]-1,head[1]]]+Snake
    if down:
        Snake=[[head[0]+1,head[1]]]+Snake
    if left:
        Snake=[[head[0],head[1]-1]]+Snake
    if right:
        Snake=[[head[0],head[1]+1]]+Snake
    Snake.pop()
    #si le serpent mange
    if head==Apple:
        Score+=1
        print(Score)
        Snake= Snake +[[Snake[-1][0]-1, Snake[-1][1]]]
        ligne=random.randrange(0,HEIGHT/L)
        colonne=random.randrange(WIDTH/L)
        while [random.randrange(0,HEIGHT/L), random.randrange(WIDTH/L)] in Snake:
            ligne=random.randrange(0,HEIGHT/L)
            colonne=random.randrange(WIDTH/L)
        Apple=[ligne,colonne]

    #sortie du terrain
    if head[0]*L>HEIGHT or head[0]<0 or head[1]<0 or head[1]*L>WIDTH:
        execute=False
    
    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            execute=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                execute=False
            if event.key == pygame.K_z and not down:
                up=True
                down=False
                right=False
                left=False
            if event.key == pygame.K_q and not right:
                up=False
                down=False
                right=False
                left=True
            if event.key == pygame.K_d and not left:
                up=False
                down=False
                right=True
                left=False
            if event.key == pygame.K_s and not up:
                up=False
                down=True
                right=False
                left=False

    pygame.display.update()

quit(0)
pygame.quit()