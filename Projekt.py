import pygame, sys
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)
RED = (255, 0, 0)
DISPLAY_SURFACE = pygame.display.set_mode((850, 650))
DISPLAY_SURFACE.fill(GRAY)
wozek = pygame.image.load("wozek.jpg")
screen = pygame.display.get_surface()
kratka = pygame.image.load("kratka.png")
zielona = pygame.image.load("zielona.png")





class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((abs(child.position[0] - end_node.position[0]))) + ((abs(child.position[1] - end_node.position[1])) )
            child.f = child.g + child.h
            

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
        
        
#jazda do celu
def jazda(przedmiot,gdzie):
    screen.blit(przedmiot,(gdzie[1]*50,gdzie[0]*50))
    pygame.display.update()
    pygame.time.wait(200)
# zamiana przejechanej drogi na czerwona kratke    
def jazda1(przedmiot1,gdzie1):
    screen.blit(przedmiot1,(gdzie1[1]*50,gdzie1[0]*50))
    pygame.display.update()
    
    
    
def main():

    maze = [[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,0]]
   # pygame.draw.rect(DISPLAY_SURFACE, BLACK, (0, 0, 50, 50)) #wspolrzedne x,y; wielkosc prostokątu
    wartosci_i = 0
    wartosci_j = 0
    for i in maze:
        wartosci_j = 0
        for j in i:
            if j == 1:
                pygame.draw.rect(DISPLAY_SURFACE, BLACK, (wartosci_j, wartosci_i, 49, 49))
            else:
                pygame.draw.rect(DISPLAY_SURFACE, GREEN, (wartosci_j, wartosci_i, 49, 49))

            wartosci_j = wartosci_j + 50
        wartosci_i = wartosci_i + 50

    start = (4, 0)
    end = (11, 12)
    
    path = astar(maze, start, end)
    print(path)
    
    # JAZDA DO PRZODU
    for krotka in path:
        pygame.draw.rect(DISPLAY_SURFACE, RED, (krotka[1]*50,krotka[0]*50, 49, 49))
        jazda(wozek,krotka)
        jazda1(kratka,krotka) # kratka - > zdjęcie, czerwonej kratki
        
    path.reverse() # obrót listy path
    
    #JAZDA POWROTNA
    for back in path:
        jazda(wozek,back)
        jazda1(zielona,back)
    
if __name__ == '__main__':
    main()        
    
            
        
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        



    

