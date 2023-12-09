import pygame
import random
import argparse

#check arguments
def check_arguments(height, tile_size, width, snake_lenght, gb_color_1, gb_color_2, snake_color, execute):
    if int(height)%int(tile_size) != 0:
        execute = False
    if int(width)%int(tile_size) != 0:
        execute = False
    if height < 12:
        execute = False
    if int(width) < 20:
        execute = False
    if int(snake_lenght) < 2:
        execute = False
    if gb_color_1 == gb_color_2:
        execute = False
    if gb_color_1 == snake_color:
        execute = False
    if gb_color_2 == snake_color:
        execute = False

#display snake
def print_snake(snake, L, screen, color):#color is color of snake
    for serpent in snake:
            rect = pygame.Rect(serpent[1]*L,serpent[0]*L , L, L)
            pygame.draw.rect(screen, color, rect)

#display score
def display_score(score):


#display apple
def print_apple(apple, L, screen, COLOR_APPLE):
    rect = pygame.Rect(apple[1]*L,apple[0]*L , L, L)
    pygame.draw.rect(screen, COLOR_APPLE, rect)

#display screen
def print_screen(COLOR_1, HEIGHT, WIDTH, screen, COLOR_2, L):
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

#move snake
def move_snake(Snake, direction):
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
    return Snake

#eat
def make_snake_eat(Apple, Score, Snake, HEIGHT, L, WIDTH):
    head = Snake[0]
    if head == Apple:
        Score += 1
        print(Score)
        Snake = Snake +[[Snake[-1][0]-1, Snake[-1][1]]]
        ligne = random.randrange(0,int(HEIGHT/L))#not necessary but python warns randrange prefers int type
        colonne = random.randrange(int(WIDTH/L))
        while [ligne, colonne] in Snake:
            ligne = random.randrange(0,int(HEIGHT/L))
            colonne = random.randrange(int(WIDTH/L))
        Apple = [ligne,colonne]
    return Snake, Apple, Score

#exit
def exit_screen(L, WIDTH, HEIGHT, Snake, gameover_on_exit):
    head = Snake[0]
    n = WIDTH/L#nb de colonnes
    m = HEIGHT/L#nb de lignes
    #dying 
    if gameover_on_exit:
        if head[0]*L > HEIGHT or head[0] < 0 or head[1] < 0 or head[1]*L > WIDTH:
            execute = False
    #living
    else:
        if head[0] > m: #en bas
            Snake[0] = [0, head[1]]
        if head[0] < 0:#en haut
            Snake[0] = [(HEIGHT/L)-1, head[1]]
        if head[1] < 0:#a gauche
            Snake[0] = [head[0], (WIDTH/L)-1]
        if head[1] > n:#a droite
            Snake[0] = [head[0], 0]

def main():
    pygame.init()
    execute=True

    #take potential inputs
    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('--gb-color-1',default='white', help="background color 1")
    parser.add_argument('--gb-color-2',default='black' , help="background color 2")
    parser.add_argument('--height',default= 300, help="height")
    parser.add_argument('--width',default=400 , help="width")
    parser.add_argument('--fps',default=4 , help="ClockFrequency")
    parser.add_argument('--fruit-color',default='red' , help="fruit color")
    parser.add_argument('--snake-color',default='green' , help="snake color")
    parser.add_argument('--snake-length',default=4 , help="snake length")
    parser.add_argument('--tile-size',default=20, help="tile size, height et witdh doivent en etre des multiples")
    parser.add_argument('--gameover-on-exit',action='store_true', help="flag")

    args = parser.parse_args()

    check_arguments(args.height, args.tile_size, args.width, args.snake_length, args.gb_color_1, args.gb_color_2, args.snake_color, execute)

    #define local (to main) constants 
    HEIGHT = int(args.height)
    WIDTH = int(args.width)
    CLOCK_FREQUENCY = float(args.fps)
    COLOR_1 = args.gb_color_1
    COLOR_2 = args.gb_color_2
    COLOR_SNAKE = args.snake_color
    COLOR_APPLE ='red'
    L = args.tile_size

    #initialize variables
    Snake = [[5,5]]#format [ligne,colonne]
    for i in range (int(args.snake_length)):
        Snake.append([5,5+i])
    Apple = [3,3]
    screen = pygame.display.set_mode( ( WIDTH,HEIGHT) )
    direction = 'left'
    Score = 0
    clock = pygame.time.Clock()

    #while loop
    while execute:

        clock.tick(CLOCK_FREQUENCY)

        #dessiner l'écran
        print_screen(COLOR_1, HEIGHT, WIDTH, screen, COLOR_2, L)

        #display snake
        print_snake(Snake, L, screen, COLOR_SNAKE)

        #display apple
        print_apple(Apple, L, screen, COLOR_APPLE)

        #display score
        #print_score(Score)
        
        #move the snake
        Snake = move_snake(Snake, direction)

        #if the snake eats
        Snake, Apple, Score = make_snake_eat(Apple, Score, Snake, HEIGHT, L, WIDTH)

        #exiting the screen
        exit_screen(L, WIDTH, HEIGHT, Snake, args.gameover_on_exit)
        
        #keyboard actions
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                execute = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    execute = False
                if event.key == pygame.K_UP and direction != 'down':
                    direction = 'up'
                if event.key == pygame.K_LEFT and direction != 'right':
                    direction = 'left'
                if event.key == pygame.K_RIGHT and direction != 'left':
                    direction = 'right'
                if event.key == pygame.K_DOWN and direction != 'up':
                    direction = 'down'

        pygame.display.update()

main()
quit(0)
pygame.quit()