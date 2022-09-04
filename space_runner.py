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

# Background Surfaces
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Score Text
score_surface = game_font.render("Score:", False, (64, 64, 64))
score_rectangle = score_surface.get_rect(center=(400, 25))

# Snail Enemy
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))

# Player
player_surface = pygame.image.load(
    "graphics/Player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

# keep screen open - game loop
while True:

    # close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print("collission")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")

        if event.type == pygame.KEYUP:
            print("key up")

    # Background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # Score
    pygame.draw.rect(screen, "#c0e8ec", score_rectangle)
    screen.blit(score_surface, score_rectangle)

    # Snail
    snail_rectangle.x -= 4
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)

    # Player
    screen.blit(player_surface, player_rectangle)

    # Input
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE] is True:
    #     print("jump")

    # Collision
    # if player_rectangle.colliderect(snail_rectangle) is True:
    #     print("collision")

    Mouse
    mouse_pos = pygame.mouse.get_pos()
    if player_rectangle.collidepoint((mouse_pos)):
        print("mouse is colliding")

    # updates display
    pygame.display.update()
    clock.tick(60)
