import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Display")

image = pygame.image.load("luffy.png")

image = pygame.transform.scale(image, (width, height))

image_rect = image.get_rect(center=(width // 2, height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    screen.fill((255, 255, 255))
 
    screen.blit(image, image_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
