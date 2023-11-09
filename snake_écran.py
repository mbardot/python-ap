import pygame

pygame.init()

#constants
Height=300
Width=400
ClockFrequency=1
White=(255, 255, 255)
Black=(0,0,0)
l=20

screen = pygame.display.set_mode( ( Width,Height) )

screen.fill(White)

rect = pygame.Rect(0, 0, l, l)
pygame.draw.rect(screen, Black, rect)
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


clock = pygame.time.Clock()

while True:

    clock.tick(1/ClockFrequency)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit(0)
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame(0)
            pygame.quit()


    pygame.display.update()
