import pygame as pg
from nodes import HomeNode, ExitNode


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1-x2) + abs(y1-y2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20

ROWS_MAX = 33
COLS_MAX = 38

MARGIN = 3

grid = []
for row in range(ROWS_MAX):
    grid.append([])
    for column in range(COLS_MAX):
        grid[row].append(0)

pg.init()
WINDOW_SIZE = [875, 765]
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("A* Path-finding Algorithm")
done = False
home_created = False
exit_created = False
home_node = HomeNode(-1, -1)  # So not to color in a square on the screen
exit_node = ExitNode(-1, -1)

clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if event.button == 1:
                if home_created is False:
                    home_node.change_pos(row, column)
                    home_created = True
                    grid[home_node.get_row()][home_node.get_column()] = 1
                else:
                    home_node.change_pos(row, column)
                # print(f'{home_node.get_row()} and {home_node.get_column()}')
            elif event.button == 2:
                grid[row][column] = 2
            elif event.button == 3:
                if exit_created is False:
                    exit_node.change_pos(row, column)
                    exit_created = True
                    grid[exit_node.get_row()][exit_node.get_column()] = 1
                else:
                    exit_node.change_pos(row, column)
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                print("Enter pressed")
                while home_node.get_row() is not exit_node.get_row() and home_node.get_column() is not exit_node.get_column():
                    print("Waiting for algorithm")

    screen.fill(BLACK)

    for row in range(ROWS_MAX):
        for column in range(COLS_MAX):
            color = WHITE
            if row == home_node.get_row() and column == home_node.get_column():
                color = GREEN
            if row == exit_node.get_row() and column == exit_node.get_column():
                color = RED
            if grid[row][column] == 2:
                color = BLACK
            pg.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    clock.tick(120)
    pg.display.flip()

pg.quit()
