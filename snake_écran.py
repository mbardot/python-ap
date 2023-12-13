import pygame
import random
import argparse
import logging
import os

def add_arg(parser):
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
    parser.add_argument('--debug',action='store_true', help="enable debug log output")
    parser.add_argument('--high-score-file',default='~/snake_scores.txt', help="file to save high scores")
    parser.add_argument('--max-high-scores',default=5, help="number of saved scores")
    return parser

#check arguments
def read_args(height, tile_size, width, snake_lenght, gb_color_1, gb_color_2, snake_color, execute):
    if int(height)%int(tile_size) != 0:
        logging.critical('unvalid tile size')
        execute = False
    if int(width)%int(tile_size) != 0:
        execute = False
    if height < 12:
        logging.warning('height is too small')
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
    return execute

#display snake
def draw_snake(snake, l, screen, color):#color is color of snake
    if snake == []:
        logging.error('snake is empty')
    for serpent in snake:
            rect = pygame.Rect(serpent[1]*l,serpent[0]*l , l, l)
            pygame.draw.rect(screen, color, rect)

#display score
def get_score(score, screen, high_score):
    police = pygame.font.Font(None, 36)
    green = (0, 255, 0)
    texte_score = police.render("Score: {}".format(score), True, green)
    high_score = int(high_score[-1][1])
    hs = police.render("High Score: {}".format(high_score), True, green)
    screen.blit(texte_score, (10, 10))
    screen.blit(hs, (10, 40))
    
#display apple
def draw_fruit(apple, l, screen, color_apple):
    rect = pygame.Rect(apple[1]*l,apple[0]*l , l, l)
    pygame.draw.rect(screen, color_apple, rect)

#display screen
def draw_checkerboard(color_1, h, w, screen, color_2, l):
    screen.fill(color_1)
    i = 0
    while i <= h:
        j = 0
        while j <= w:
            rect = pygame.Rect(j, i, l, l)
            pygame.draw.rect(screen, color_2, rect)
            j += 2*l
        i += l
        j = l
        while j <= w:
            rect = pygame.Rect(j, i, l, l)
            pygame.draw.rect(screen, color_2, rect)
            j += 2*l
        i += l

#move snake
def move_snake(Snake, direction, execute):
    head = Snake[0]
    if head in Snake[2:]: #collision
        logging.info('collision')
        execute = False
    if direction == 'up':
        Snake = [[head[0]-1,head[1]]]+Snake
    if direction == 'down':
        Snake = [[head[0]+1,head[1]]]+Snake
    if direction == 'left':
        Snake = [[head[0],head[1]-1]]+Snake
    if direction == 'right':
        Snake = [[head[0],head[1]+1]]+Snake
    Snake.pop()
    return Snake, execute

#eat
def update_fruit(Apple, Score, Snake, h, l, w):
    head = Snake[0]
    if head == Apple:
        Score += 1
        Snake = Snake +[[Snake[-1][0]-1, Snake[-1][1]]]
        ligne = random.randrange(0,int(h/l))#not necessary but python warns randrange prefers int type
        colonne = random.randrange(int(w/l))
        while [ligne, colonne] in Snake:
            ligne = random.randrange(0,int(h/l))
            colonne = random.randrange(int(h/l))
        Apple = [ligne,colonne]
        logging.info('fruit eaten')
    return Snake, Apple, Score

#exit
def exit_screen(l, w, h, Snake, gameover_on_exit, execute):
    head = Snake[0]
    n = w/l#nb de colonnes
    m = h/l#nb de lignes
    #dying 
    if gameover_on_exit:
        if head[0]*l > h or head[0] < 0 or head[1] < 0 or head[1]*l > w:
            execute = False
    #living
    else:
        if head[0] > m: #en bas
            Snake[0] = [0, head[1]]
        if head[0] < 0:#en haut
            Snake[0] = [(h/l)-1, head[1]]
        if head[1] < 0:#a gauche
            Snake[0] = [head[0], (w/l)-1]
        if head[1] > n:#a droite
            Snake[0] = [head[0], 0]
    return execute

#this function is here to know the current high score when you start a game, 
# if it is the first game, on the device, creates a file for high scores
def loading_high_scores(directory_to_high_scores):
    hs = directory_to_high_scores
    if os.path.exists(hs):#file already exists
        with open(hs) as fichier:
            if os.path.getsize(hs) == 0:#file is empty (should be impossible i believe)
                return[('nobody', 0)]
            else:
                high_score_list = []
                for line in fichier:
                    name = line.split()[0]
                    score = float(line.split()[1])
                    high_score_list.append((name, score))
                    print(name, score)
                return high_score_list#this list is sorted from lowest to highest score
    else:#file does not exist yet
        with open(hs, 'w') as file:
            pass
        return [('nobody', 0)]

def update_high_score(score, directory_to_high_scores, high_scores, max_high_scores):
    if score > high_scores[0][1]:
        name = input("enter username")
        high_scores.append((name, score))
        #high_scores now needs to be sorted
        sorted_list = sorted(high_scores, key=lambda x: x[1])
        sorted_list = sorted_list[-max_high_scores:]#this list must be max_high_scores long
        print('High Scores:')
        with open(directory_to_high_scores, "w") as fichier:
            for couple in sorted_list:#couple is (name, score)
                fichier.write(str(couple[0])+' '+str(couple[1])+'\n')
                print(couple[0], ':', couple[1])

def process_events(direction, execute):
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
    return direction, execute

def draw(color_1, h, w, screen, color_2, l, Snake, color_snake, Apple, color_apple):
    #draw screen
    draw_checkerboard(color_1, h, w, screen, color_2, l)

    #display snake
    draw_snake(Snake, l, screen, color_snake)

    #display apple
    draw_fruit(Apple, l, screen, color_apple)

def update_display(color_1, h, w, screen, color_2, l, Snake, color_snake, Apple, color_apple, Score, high_score):
    draw(color_1, h, w, screen, color_2, l, Snake, color_snake, Apple, color_apple)
    get_score(Score, screen, high_score)
    pygame.display.set_caption('Snake GAME')
    pygame.display.update()


def main():
    pygame.init()
    execute=True

    #take potential inputs
    parser = argparse.ArgumentParser(description='Some description.')
    
    parser = add_arg(parser)#removed the big block

    args = parser.parse_args()

    #define local (to main) constants 
    HEIGHT = int(args.height)
    WIDTH = int(args.width)
    CLOCK_FREQUENCY = float(args.fps)
    COLOR_1 = args.gb_color_1
    COLOR_2 = args.gb_color_2
    COLOR_SNAKE = args.snake_color
    COLOR_APPLE ='red'
    L = int(args.tile_size)
    directory_to_high_scores = os.path.expanduser(args.high_score_file)
    max_high_scores = args.max_high_scores

    execute = read_args(HEIGHT, L, WIDTH, args.snake_length, COLOR_1, COLOR_2, COLOR_SNAKE, execute)

    # Configure logging based on the debug argument
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info('enter main loop')
    
    high_scores = loading_high_scores(directory_to_high_scores)#should be a list with 5 couples (name, score) sorted from lowest to highest score

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

        draw(COLOR_1, HEIGHT, WIDTH, screen, COLOR_2, L, Snake, COLOR_SNAKE, Apple, COLOR_APPLE)
        
        #move the snake
        Snake, execute = move_snake(Snake, direction, execute)

        #if the snake eats
        Snake, Apple, Score = update_fruit(Apple, Score, Snake, HEIGHT, L, WIDTH)

        #exiting the screen
        execute = exit_screen(L, WIDTH, HEIGHT, Snake, args.gameover_on_exit, execute)
        
        #keyboard actions
        direction, execute = process_events(direction , execute)

        update_display(COLOR_1, HEIGHT, WIDTH, screen, COLOR_2, L, Snake, COLOR_SNAKE, Apple, COLOR_APPLE, Score, high_scores)

    # end of the game
    update_high_score(Score, directory_to_high_scores, high_scores, max_high_scores)

main()
quit(0)
pygame.quit()