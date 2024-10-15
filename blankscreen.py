import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()

pygame.quit()
