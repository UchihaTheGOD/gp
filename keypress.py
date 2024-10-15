import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Key Press and Release Example")
done = False

# Initialize variables to track key states
keys_pressed = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key not in keys_pressed:
                keys_pressed.append(event.key)  # Record key press
                print(f"Key pressed: {pygame.key.name(event.key)}")
        
        if event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed.remove(event.key)  # Remove key release
                print(f"Key released: {pygame.key.name(event.key)}")

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()

pygame.quit()
