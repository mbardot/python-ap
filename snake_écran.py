import pygame

pygame.init()

#constants
Height=300
Width=400
ClockFrequency=1
White=(255, 255, 255)
Black=(0,0,0)
l=10

screen = pygame.display.set_mode( ( Width,Height) )

screen.fill(White)

#i=0
#while i <= Height:
#    
#    for m in range(l):
#        j= l
#        while j <= Width:
#            for k in range(l):
#                screen.set_at((j+k, i+m), Black) 
#            j=j+2*l
#    i=i+l
rect = pygame.Rect(0, 0, l, l)
pygame.draw.rect(screen, Black, rect)
i=0
while i <= Height:
    j=0
    while j<= Width:
        rect = pygame.Rect(j, i, l, l)
        pygame.draw.rect(screen, Black, rect)
        j+=l
    i+=l


clock = pygame.time.Clock()

while True:

    clock.tick(1/ClockFrequency)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.update()
