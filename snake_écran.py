import pygame
import random
pygame.init()
execute=True


#récupérer les arguments
import argparse
parser = argparse.ArgumentParser(description='Some description.')
parser.add_argument('--gb-color-1',default='white', help="background color 1")
parser.add_argument('--gb-color-2',default='black' , help="background color 2")
parser.add_argument('--height',default= 300, help="height")
parser.add_argument('--width',default=400 , help="width")
parser.add_argument('--fps',default=5 , help="ClockFrequency")
parser.add_argument('--fruit-color',default='red' , help="fruit color")
parser.add_argument('--snake-color',default='green' , help="snake color")
parser.add_argument('--snake-length',default=4 , help="snake length")
parser.add_argument('--tile-size',default=20, help="tile size, height et witdh doivent en etre des multiples")
parser.add_argument('--gameover-on-exit',action='store_true', help="flag")

args = parser.parse_args()

#print(args)
#print("The value of -a is accessed with args.a: " + args.a)

#check arguments
if int(args.height)%int(args.tile_size) != 0:
    execute = False
if int(args.width)%int(args.tile_size) != 0:
    execute = False
if args.height < 12:
    execute = False
if int(args.width) < 20:
    execute = False
if int(args.snake_length) < 2:
    execute = False
if args.gb_color_1 == args.gb_color_2:
    execute = False
if args.gb_color_1 == args.snake_color:
    execute = False
if args.gb_color_2 == args.snake_color:
    execute = False

#define constants 
HEIGHT = int(args.height)
WIDTH = int(args.width)
CLOCK_FREQUENCY = float(args.fps)
COLOR_1 = args.gb_color_1
COLOR_2 = args.gb_color_2
COLOR_SNAKE = args.snake_color
COLOR_APPLE ='red'
L = args.tile_size


#format [ligne,colonne]
Snake = [[5,5]]
for i in range (int(args.snake_length)):
    Snake.append([5,5+i])

Apple = [3,3]
#écran
screen = pygame.display.set_mode( ( WIDTH,HEIGHT) )
#directions
direction = 'left'
Score = 0
clock = pygame.time.Clock()
while execute:

    clock.tick(CLOCK_FREQUENCY)
    #dessiner l'écran
    screen.fill(COLOR_1)
    i = 0
    while i <= HEIGHT:
        j = 0
        while j <= WIDTH:
            rect = pygame.Rect(j, i, L, L)
            pygame.draw.rect(screen, COLOR_2, rect)
            j += 2*L
        i += L
        j = L
        while j <= WIDTH:
            rect = pygame.Rect(j, i, L, L)
            pygame.draw.rect(screen, COLOR_2, rect)
            j += 2*L
        i += L

    #dessiner le serpent
    for serpent in Snake:
        rect = pygame.Rect(serpent[1]*L,serpent[0]*L , L, L)
        pygame.draw.rect(screen, COLOR_SNAKE, rect)
    #dessiner la pomme
    rect = pygame.Rect(Apple[1]*L,Apple[0]*L , L, L)
    pygame.draw.rect(screen, COLOR_APPLE, rect)

    
    #déplacer le serpent
    head = Snake[0]
    if direction == 'up':
        Snake = [[head[0]-1,head[1]]]+Snake
    if direction == 'down':
        Snake = [[head[0]+1,head[1]]]+Snake
    if direction == 'left':
        Snake = [[head[0],head[1]-1]]+Snake
    if direction == 'right':
        Snake = [[head[0],head[1]+1]]+Snake
    Snake.pop()

    #si le serpent mange
    if head == Apple:
        Score += 1
        print(Score)
        Snake = Snake +[[Snake[-1][0]-1, Snake[-1][1]]]
        ligne = random.randrange(0,HEIGHT/L)
        colonne = random.randrange(WIDTH/L)
        while [random.randrange(0,HEIGHT/L), random.randrange(WIDTH/L)] in Snake:
            ligne = random.randrange(0,HEIGHT/L)
            colonne = random.randrange(WIDTH/L)
        Apple = [ligne,colonne]

    #sortie du terrain

    n = WIDTH/L#nb de colonnes
    m = HEIGHT/L#nb de lignes
    #si on meurt 
    if args.gameover_on_exit:
        if head[0]*L > HEIGHT or head[0] < 0 or head[1] < 0 or head[1]*L > WIDTH:
            execute = False
    #si on boucle
    else:
        if head[0] > m: #en bas
            Snake[0] = [0, head[1]]
        if head[0] < 0:#en haut
            Snake[0] = [(HEIGHT/L)-1, head[1]]
        if head[1] < 0:#a gauche
            Snake[0] = [head[0], (WIDTH/L)-1]
        if head[1] > n:#a droite
            Snake[0] = [head[0], 0]

    for event in pygame.event.get():
            
        if event.type == pygame.QUIT:
            execute = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                execute = False
            if event.key == pygame.K_z and direction != 'down':
                dierction = 'up'
            if event.key == pygame.K_q and direction != 'right':
                direction = 'right'
            if event.key == pygame.K_d and direction != 'left':
                direction = 'right'
            if event.key == pygame.K_s and direction != 'up':
                direction = 'down'

    pygame.display.update()

quit(0)
pygame.quit()