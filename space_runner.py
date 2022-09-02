# import pygame
import pygame
# starts pygame, always first
pygame.init()
# create display surface - window
screen = pygame.display.set_mode((800, 400))
# keep screen open
while True:
    # draw all elements
    # update elements
    # eveything happens in loop
    # close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # updates display
    pygame.display.update()
