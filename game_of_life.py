import pygame
import argparse
import logging
import os




class Cell:

    def __init__(self, position, state) -> None:
        self._position = position # tupple (line, column)
        self._state = state # string 'dead' or 'alive'
    
    def is_alive(self):
        if self._state == 'alive':
            return True
        return False
    
    def get_position(self):
        
        return self._position

    def get_neighbors(self, Set_Of_cells):
        neighbors = []
        x = self.get_position()[0]
        y = self.get_position()[1]
        if Cell( (x-1, y-1 ), 'dead' ) not in Set_Of_cells:#top left
            neighbors.append( Cell( (x-1, y-1 ), 'dead' ))
        else:
            neighbors.append( Cell( (x-1, y-1 ), 'alive' ))
        
        if Cell( (x-1, self.get_position()[1] ), 'dead') not in Set_Of_cells:#top
            neighbors.append( Cell( (x-1, y ), 'dead') )
        else:
            neighbors.append( Cell( (x-1, y ), 'alive') )
        
        if Cell( (x-1, y+1 ), 'dead')  not in Set_Of_cells:#top right
            neighbors.append( Cell( (x-1, y+1 ), 'dead') )
        else:
            neighbors.append( Cell( (x-1, y+1 ), 'alive') )
    
        if Cell( (x, y-1 ), 'dead')  not in Set_Of_cells:#left
            neighbors.append( Cell( (x, y-1 ), 'dead') )
        else:
            neighbors.append( Cell( (x, y-1 ), 'alive') )

        if Cell( (x, y+1 ), 'dead') not in Set_Of_cells:#right
            neighbors.append( Cell( (x, y+1 ), 'dead') )
        else:
            neighbors.append( Cell( (x, y+1 ), 'alive') )

        if Cell( (x+1, y-1 ), 'dead') not in Set_Of_cells:#bottom left
            neighbors.append( Cell( (x+1, y-1 ), 'dead') )
        else:
            neighbors.append( Cell( (x+1, y-1 ), 'alive') )

        if Cell( (x+1, y ), 'dead') not in Set_Of_cells:#bottom
            neighbors.append( Cell( (x+1, y ), 'dead') )
        else:
            neighbors.append( Cell( (x+1, y ), 'alive') )

        if Cell( (x+1, y+1 ), 'dead') not in Set_Of_cells:#bottom right
            neighbors.append( Cell( (x+1, y+1 ), 'dead') )
        else:
            neighbors.append( Cell( (x+1, y+1 ), 'alive') )
        
        return neighbors

class Set_Of_Cells:

    def __init__(self, list_of_cells) -> None:
        self._set = list_of_cells

    def __iter__(self):
        return iter(self._set)
    
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
                        if case == '1':#living cell
                            self._set.append( Cell((l, c), 'alive') )
        else:
            logging.error('input file not found')

    def save_state(self): #TODO
        pass

    def to_visit(self): #returns a list of all interesting cells to check for this turn
        return get_neighbors(self._set)

    def check_all(self):   #we go through all of the 'interesting cells'
        new_set = []
        cells_to_visit = self.to_visit()
        print(cells_to_visit)
        for cell in cells_to_visit:
            neighbors = cell.get_neighbors(self) #these are the direct neighbors of the cell 'cell', there state decide if cell lives or not
            alive = alive_in(neighbors) #int
            if cell.is_alive():
                if alive == 2 or alive == 3:
                    new_set.append( cell)
            else:
                if alive == 3:
                    new_set.append( cell)
        return Set_Of_Cells(new_set)



def get_neighbors(cells): # list of cell  -> list of cell
    neighbors = cells
    for cell in cells:
        x = cell.get_position()[0]
        y = cell.get_position()[1]
        if Cell( (x-1, y-1 ), 'alive' ) not in neighbors:#top left
            neighbors.append( Cell( (x-1, y-1 ), 'dead' ))  
        if Cell( (x-1, y ), 'alive') not in neighbors:#top
            neighbors.append( Cell( (x-1, y ), 'dead') )
        if Cell( (x-1, y+1 ), 'alive')  not in neighbors:#top right
            neighbors.append( Cell( (x-1, y+1 ), 'dead') )
        if Cell( (x, y-1 ), 'alive')  not in neighbors:#left
            neighbors.append( Cell( (x, y-1 ), 'dead') )
        if Cell( (x, y+1 ), 'alive') not in neighbors:#right
            neighbors.append( Cell( (x, y+1 ), 'dead') )
        if Cell( (x+1, y-1 ), 'alive') not in neighbors:#bottom left
            neighbors.append( Cell( (x+1, y-1 ), 'dead') )
        if Cell( (x+1, y ), 'alive') not in neighbors:#bottom
            neighbors.append( Cell( (x+1, y ), 'dead') )
        if Cell( (x+1, y+1 ), 'alive') not in neighbors:#bottom right
            neighbors.append( Cell( (x+1, y+1 ), 'dead') )
    
    return neighbors

def alive_in(list):
    n = 0
    for cell in list:
        if cell.is_alive():
            n += 1
    return n

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
    screen.fill('white')
    cells.display(screen, l)
    pygame.display.set_caption('Game Of Life')
    print('+++++++++++++++++++++++++++++++++++')
    pygame.display.update()


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main():

    #take potential inputs
    parser = argparse.ArgumentParser(description='Some description')
    parser = add_arguments(parser)#removed the big block
    args = parser.parse_args()

    #define local (to main) constants
    CLOCK_FREQUENCY = args.f
    HEIGHT = args.height
    WIDTH = args.width
    L = 10
    clock = pygame.time.Clock()
    cells = Set_Of_Cells([])#this is the set of living cells
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
            
            cells = cells.check_all()#updates who lives, who dies
            print('here')
            execute = process_events()

    else: #we do not want to display:
        logging.info("we don't display")
        for step in range(args.m):
            pass

main()