import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FROG_WIDTH = 40
FROG_HEIGHT = 40
CAR_WIDTH = 50
CAR_HEIGHT = 40
FPS = 50

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

# Load frog image
frog_image = pygame.Surface((FROG_WIDTH, FROG_HEIGHT))
frog_image.fill(GREEN)

# Load car image
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(RED)

# Frog class
class Frog:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - FROG_HEIGHT, FROG_WIDTH, FROG_HEIGHT)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Keep frog within screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - FROG_WIDTH:
            self.rect.x = SCREEN_WIDTH - FROG_WIDTH
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > SCREEN_HEIGHT - FROG_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - FROG_HEIGHT

# Car class
class Car:
    def __init__(self, y):
        self.rect = pygame.Rect(SCREEN_WIDTH, y, CAR_WIDTH, CAR_HEIGHT)
        self.speed = random.randint(5, 10)

    def move(self):
        self.rect.x -= self.speed
        if self.rect.x < -CAR_WIDTH:
            self.rect.x = SCREEN_WIDTH
            self.speed = random.randint(5, 10)

# Main game loop
def main():
    clock = pygame.time.Clock()
    frog = Frog()
    cars = [Car(random.randint(50, SCREEN_HEIGHT - 50)) for _ in range(5)]
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            frog.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            frog.move(5, 0)
        if keys[pygame.K_UP]:
            frog.move(0, -5)
        if keys[pygame.K_DOWN]:
            frog.move(0, 5)

        # Move cars
        for car in cars:
            car.move()

        # Check for collisions
        for car in cars:
            if frog.rect.colliderect(car.rect):
                print("Game Over! Your score:", score)
                running = False

        # Check if frog reached the top
        if frog.rect.y < 0:
            score += 1
            frog.rect.y = SCREEN_HEIGHT - FROG_HEIGHT  # Reset frog position

        # Draw everything
        screen.fill(WHITE)
        screen.blit(frog_image, frog.rect)
        for car in cars:
            screen.blit(car_image, car.rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()