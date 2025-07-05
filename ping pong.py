from pygame import *

screen = display.set_mode((800, 600))

display.set_caption("PING PONG")

running = True






while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    display.flip()

quit()
