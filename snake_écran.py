import pygame

pygame.init()

#constants
execute=True
Height=300
Width=400
ClockFrequency=1
White=(255, 255, 255)
Black=(0,0,0)
Green=(0,200,0)
l=20
Snake=[(9,4),(9,5),(9,6)]

screen = pygame.display.set_mode( ( Width,Height) )

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

for case in Snake:
    rect = pygame.Rect(case[1]*l,case[0]*l , l, l)
    pygame.draw.rect(screen, Green, rect)



clock = pygame.time.Clock()
while execute:

    clock.tick(1/ClockFrequency)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                execute=False
        if event.type == pygame.QUIT:
            execute=False
    pygame.display.update()
quit(0)
pygame.quit()