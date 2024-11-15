import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 30
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue
GRASS_COLOR = (34, 139, 34)
DIRT_COLOR = (139, 69, 19)

# Dash constants
DASH_SPEED = 10  # Speed during dash
NORMAL_SPEED = 5  # Normal speed
DASH_TIME_LIMIT = 0.2  # Time limit in seconds for double-tap to be considered a dash

# Bullet constants
BULLET_SPEED = 5  # Initial bullet speed
BULLET_SPEED_INCREASE = 0.05  # Rate of increase in bullet speed over time
BULLET_SIZE = 15  # Increase bullet size for better visibility

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft-like Game with Dash and Bullets")

# Clock to control frame rate
clock = pygame.time.Clock()

# World size
world_width = WIDTH // BLOCK_SIZE
world_height = HEIGHT // BLOCK_SIZE

# Bullet Class
class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        # Change the bullet color to blue
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), BULLET_SIZE)

    def is_off_screen(self):
        return self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT

# Generate random bullets
def generate_bullet():
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        x = random.randint(0, WIDTH)
        y = 0
        dx = random.choice([-1, 1]) * random.randint(1, 3)
        dy = BULLET_SPEED
    elif side == "bottom":
        x = random.randint(0, WIDTH)
        y = HEIGHT
        dx = random.choice([-1, 1]) * random.randint(1, 3)
        dy = -BULLET_SPEED
    elif side == "left":
        x = 0
        y = random.randint(0, HEIGHT)
        dx = BULLET_SPEED
        dy = random.choice([-1, 1]) * random.randint(1, 3)
    else:  # "right"
        x = WIDTH
        y = random.randint(0, HEIGHT)
        dx = -BULLET_SPEED
        dy = random.choice([-1, 1]) * random.randint(1, 3)
    
    return Bullet(x, y, dx, dy)

# Generate a simple world with grass and dirt blocks
def generate_world():
    world = []
    for y in range(world_height):
        row = []
        for x in range(world_width):
            # Randomly generate grass or dirt blocks
            if y < world_height // 2:
                row.append('grass')
            else:
                row.append('dirt')
        world.append(row)
    return world

# Draw the world
def draw_world(world):
    for y in range(world_height):
        for x in range(world_width):
            block = world[y][x]
            if block == 'grass':
                color = GRASS_COLOR
            elif block == 'dirt':
                color = DIRT_COLOR
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Draw player
def draw_player(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x - BLOCK_SIZE // 2, y - BLOCK_SIZE // 2, BLOCK_SIZE, BLOCK_SIZE))

# Handle player interactions (breaking blocks)
def break_block(world, x, y):
    grid_x = x // BLOCK_SIZE
    grid_y = y // BLOCK_SIZE
    world[grid_y][grid_x] = 'air'  # Change the block to 'air'

# Main game loop
def main():
    global player_x, player_y
    player_x, player_y = WIDTH // 2, HEIGHT // 2
    world = generate_world()

    # Variables for double-tap detection
    last_key_time = {pygame.K_w: 0, pygame.K_a: 0, pygame.K_s: 0, pygame.K_d: 0}
    last_key_pressed = None

    # Bullet list and game speed
    bullets = []
    last_bullet_time = time.time()
    bullet_speed_increase = 0  # Increment bullet speed over time

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Handle player movement (WASD controls with dash)
        keys = pygame.key.get_pressed()
        
        # Time check for double-tap detection
        current_time = time.time()

        # Check each direction for double-tap (W, A, S, D)
        if keys[pygame.K_w]:
            if last_key_pressed == pygame.K_w and (current_time - last_key_time[pygame.K_w] < DASH_TIME_LIMIT):
                # Dash up
                player_y -= DASH_SPEED
            else:
                # Normal movement
                player_y -= NORMAL_SPEED
            last_key_time[pygame.K_w] = current_time
            last_key_pressed = pygame.K_w

        if keys[pygame.K_a]:
            if last_key_pressed == pygame.K_a and (current_time - last_key_time[pygame.K_a] < DASH_TIME_LIMIT):
                # Dash left
                player_x -= DASH_SPEED
            else:
                # Normal movement
                player_x -= NORMAL_SPEED
            last_key_time[pygame.K_a] = current_time
            last_key_pressed = pygame.K_a

        if keys[pygame.K_s]:
            if last_key_pressed == pygame.K_s and (current_time - last_key_time[pygame.K_s] < DASH_TIME_LIMIT):
                # Dash down
                player_y += DASH_SPEED
            else:
                # Normal movement
                player_y += NORMAL_SPEED
            last_key_time[pygame.K_s] = current_time
            last_key_pressed = pygame.K_s

        if keys[pygame.K_d]:
            if last_key_pressed == pygame.K_d and (current_time - last_key_time[pygame.K_d] < DASH_TIME_LIMIT):
                # Dash right
                player_x += DASH_SPEED
            else:
                # Normal movement
                player_x += NORMAL_SPEED
            last_key_time[pygame.K_d] = current_time
            last_key_pressed = pygame.K_d

        # Handle block breaking (spacebar)
        if keys[pygame.K_SPACE]:
            break_block(world, player_x, player_y)

        # Bullet spawning
        if current_time - last_bullet_time > 1 - bullet_speed_increase:
            bullets.append(generate_bullet())
            last_bullet_time = current_time
            bullet_speed_increase += BULLET_SPEED_INCREASE

        # Move and draw bullets
        for bullet in bullets[:]:
            bullet.move()
            bullet.draw()

            # Check for collision with player
            if abs(bullet.x - player_x) < BLOCK_SIZE // 2 and abs(bullet.y - player_y) < BLOCK_SIZE // 2:
                print("Player hit by a bullet!")
                running = False  # End the game on collision

            # Remove bullets that are off the screen
            if bullet.is_off_screen():
                bullets.remove(bullet)

        # Fill screen with background color
        screen.fill(BACKGROUND_COLOR)

        # Draw the world
        draw_world(world)

        # Draw the player
        draw_player(player_x, player_y)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()