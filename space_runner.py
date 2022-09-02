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

# Clock object
clock = pygame.time.Clock()

# Font
game_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Surfaces
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = game_font.render("Space Runner", False, "Black")

# Enemies
snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_x_pos = 600

# keep screen open - game loop
while True:

    # close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 25))

    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 275))

    # updates display
    pygame.display.update()
    clock.tick(60)
