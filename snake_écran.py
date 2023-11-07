import pygame

pygame.init()

#constants
Height=300
Width=400
ClockFrequency=1
White=(255, 255, 255)
Black=(0,0,0)

screen = pygame.display.set_mode( ( Width,Height) )

clock = pygame.time.Clock()

while True:

    clock.tick(1/ClockFrequency)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(White)

    pygame.display.update()
