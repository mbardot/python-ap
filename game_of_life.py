import pygame
import argparse
import logging
import os




class Cell:

    def __init__(self, position) -> None:
        self._position = position # tupple (line, column)
    
    def get_position(self):
        return self._position


class Set_Of_Cells:

    def __init__(self, list_of_cells) -> None:
        self._set = list_of_cells

    def display(self, screen, l):
        for cell in self._set:
            pos = cell.get_position()
            rect = pygame.Rect(pos[1]*l,pos[0]*l , l, l)
            pygame.draw.rect(screen, 'black', rect)
    
    def load_state(self, path):
        if os.path.exists(path):#file already exists
            with open(path) as file:
                for l, line in enumerate(file):
                    for c, case in enumerate(line):
                        if case == '1':#dead cell
                            self._set.append( (l, c) )
        else:
            logging.error('input file not found')

    def save_state(self): #TODO
        pass


def add_arguments(parser):
    parser.add_argument('-i', help="to set the path to the initial pattern file")
    parser.add_argument('-o', help="to set the path to the output file")
    parser.add_argument('-m',default = 20, help=" to set the number of steps to run, when display is off")
    parser.add_argument('-d',action='store_true', help="display flag")
    parser.add_argument('-f',default = 10, help=" The number of frames per second to use with pygame")
    parser.add_argument('--width',default = 800, help=" initial width of the pygame screen")
    parser.add_argument('--height',default = 600, help=" initial height of the pygame screen")
    return parser




def draw(screen, cells, l):
    #display dead cells
    cells.display(screen, l)
    pygame.display.set_caption('Game Of Life')
    pygame.display.update()


def main():

    #take potential inputs
    parser = argparse.ArgumentParser(description='Some description')
    parser = add_arg(parser)#removed the big block
    args = parser.parse_args()

    #define local (to main) constants
    CLOCK_FREQUENCY = args.f
    HEIGHT = args.height
    WIDTH = args.width
    L = 10
    cells = Set_Of_Cells([])
    cells.load_state(args.i)

    # Configure logging
    log_level = logging.DEBUG #change to logging.INFO if debug is not necessary
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

    if args.d : #we want to display with pygame
    
        logging.info('we display')
        pygame.init()
        execute = True
        screen = pygame.display.set_mode( ( WIDTH,HEIGHT) )

        while execute:
            
            clock.tick(CLOCK_FREQUENCY)

            draw(screen, cells, L)



    else: #we do not want to display:
        logging.info("we don't display")
        for step in range(args.m):
            