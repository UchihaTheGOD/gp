import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Shape Drawing Example")
done = False

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the background with white
    screen.fill(WHITE)

    # Draw a rectangle
    pygame.draw.rect(screen, RED, (50, 50, 200, 100))  # (x, y, width, height)

    # Draw a circle
    pygame.draw.circle(screen, GREEN, (400, 150), 75)  # (center_x, center_y, radius)

    # Draw a triangle
    pygame.draw.polygon(screen, BLUE, [(600, 100), (550, 200), (650, 200)])  # List of vertices

    # Draw an ellipse
    pygame.draw.ellipse(screen, (255, 165, 0), (200, 300, 400, 200))  # (x, y, width, height)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
