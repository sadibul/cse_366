import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
AGENT_COLOR = (0, 128, 255)  # Blue
AGENT_COLOR_B = (255, 0, 0)  # Red
TEXT_COLOR = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame AI Simulation Framework")

# Clock to control frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 36)

# Agent class for the simulation
class Agent(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_x, start_y
        self.speed = 8

    def update(self, keys, control_scheme):
        """Update the agent's position based on key input."""
        if control_scheme == "arrows":
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
                self.rect.x += self.speed
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += self.speed
        elif control_scheme == "wasd":
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_d] and self.rect.right < WINDOW_WIDTH:
                self.rect.x += self.speed
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < WINDOW_HEIGHT:
                self.rect.y += self.speed

# Setup the agents and sprite group
agent_a = Agent(AGENT_COLOR, 100, 100)
agent_b = Agent(AGENT_COLOR_B, 200, 200)
all_sprites = pygame.sprite.Group()
all_sprites.add(agent_a)
all_sprites.add(agent_b)

# Main loop
running = True
while running:
    # Limit frame rate to 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Update the agents based on user input
    agent_a.update(keys, "arrows")
    agent_b.update(keys, "wasd")

    # Fill the screen background
    screen.fill(BACKGROUND_COLOR)

    # Draw the agents
    all_sprites.draw(screen)

    # Display the frame count as an example text (debug info)
    frame_text = font.render(f"Frame: {pygame.time.get_ticks() // 1000}", True, TEXT_COLOR)
    screen.blit(frame_text, (10, 10))

    # Flip the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()