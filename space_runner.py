# import pygame
import pygame
# sys module
from sys import exit

# starts pygame, always first
pygame.init()

# create display surface - window
screen = pygame.display.set_mode((800, 400))

# game title
pygame.display.set_caption("Space Runner")

# game icon - didnt know how to use surface yet so couldnt get it to work
# pygame_icon = pygame.image.load("icon.png")
# pygame.display.set_icon(pygame_icon)

# keep screen open
while True:

    # draw all elements
    # update elements
    # eveything happens in loop

    # close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # updates display
    pygame.display.update()
