import pygame

pygame.init()

#constants
execute=True
Height=300
Width=400
ClockFrequency=10
White=(255, 255, 255)
Black=(0,0,0)
Green=(0,200,0)
l=20

#format [ligne,colonne]
Snake=[[9,4],[9,5],[9,6], [9,7], [9,8]]

screen = pygame.display.set_mode( ( Width,Height) )

up=False
down=False
right=False
left=True

clock = pygame.time.Clock()
while execute:

    clock.tick(ClockFrequency)
    #dessiner l'écran
    screen.fill(White)
    i=0
    while i <= Height:
        j=0
        while j<= Width:
            rect = pygame.Rect(j, i, l, l)
            pygame.draw.rect(screen, Black, rect)
            j+=2*l
        i+=l
        j=l
        while j<= Width:
            rect = pygame.Rect(j, i, l, l)
            pygame.draw.rect(screen, Black, rect)
            j+=2*l
        i+=l

    #dessiner le serpent
    for c in Snake:
        rect = pygame.Rect(c[1]*l,c[0]*l , l, l)
        pygame.draw.rect(screen, Green, rect)
    
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
    
    
    
   

    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            execute=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                execute=False
            if event.key == pygame.K_z and not down:
                print('touché')
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