import pygame
import time

# EDIT THESE:
SIZE = 800      # if set other than 0, square screen size
WIDTH = SIZE if SIZE != 0 else      1300    # screen width
HEIGHT = SIZE if SIZE != 0 else     800     # screen height
SLEEP = 0.1     # sleep after each line drawn
WAIT = 5        # sleep at end of execution
CIRCLE = True   # draw circles to compare at end
N = 250          # total number of lines
black = (0,0,0)         # colors
pink = (255,200,200)    # colors
FILL_COLOR = pink       # background color
LINE_COLOR = black      # line color


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(FILL_COLOR)
pygame.display.update()

mod_H = HEIGHT/2    # halfway
mod_W = WIDTH/2     # halfway
n = int(N/4)        # each corner


# bottom left
for i in range(n):
    xfrom = 0
    yfrom = mod_H + i * (mod_H/n)
    xto = (i + 1) * (mod_W/n)
    yto = HEIGHT
    print(i, xfrom, yfrom, xto, yto)
    pygame.draw.line(screen, LINE_COLOR, (xfrom, yfrom), (xto, yto), 1)
    pygame.display.update()
    time.sleep(SLEEP)

# bottom right
for i in range(n):
    xfrom = mod_W + i * (mod_W/n)
    yfrom = HEIGHT
    xto = WIDTH
    yto = HEIGHT - (i + 1) * (mod_H/n)
    print(i, xfrom, yfrom, xto, yto)
    pygame.draw.line(screen, LINE_COLOR, (xfrom, yfrom), (xto, yto), 1)
    pygame.display.update()
    time.sleep(SLEEP)

# top right
for i in range(n):
    xfrom = WIDTH
    yfrom = mod_H - i * (mod_H/n)
    xto = WIDTH - (i + 1) * (mod_W/n)
    yto = 0
    print(i, xfrom, yfrom, xto, yto)
    pygame.draw.line(screen, LINE_COLOR, (xfrom, yfrom), (xto, yto), 1)
    pygame.display.update()
    time.sleep(SLEEP)

# top left
for i in range(n):
    xfrom = mod_W - i * (mod_W/n)
    yfrom = 0
    xto = 0
    yto = (i + 1) * (mod_H/n)
    pygame.draw.line(screen, LINE_COLOR, (xfrom, yfrom), (xto, yto), 1)
    pygame.display.update()
    time.sleep(SLEEP)

# pygame.draw.line(screen, black, (0,0), (100,100),1)
# pygame.display.update()
if (CIRCLE):
    for i in range (n):
        radius = (i + 1) * (( SIZE/2 ) / n)
        pygame.draw.circle(screen, black, (mod_H, mod_W), radius, 1 if i < (n-1) else 0)
        pygame.display.update()
        time.sleep(SLEEP)
        # print(int( n / (i + 1) ))

time.sleep(WAIT)
