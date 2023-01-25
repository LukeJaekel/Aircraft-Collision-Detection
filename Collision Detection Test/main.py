import pygame
import os

pygame.init()

alarm = pygame.mixer.Sound('Collision Alarm.mp3')

# Window Generation
WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (14, 48, 5)
FPS = 5
VELOCITY = 5
RED = pygame.Color("red")

BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
PLANE_WIDTH, PLANE_HEIGHT = 25.05, 22.02

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Air Traffic Collision Detection")

# Two plane images
PLANE_IMAGE = pygame.image.load(
    os.path.join('Plane Icon.png'))
PLANE = pygame.transform.rotate(pygame.transform.scale(
    PLANE_IMAGE, (PLANE_WIDTH, PLANE_HEIGHT)), -45)

PLANE_IMAGE_2 = pygame.image.load(
    os.path.join('Plane Icon.png'))
PLANE_2 = pygame.transform.rotate(pygame.transform.scale(
    PLANE_IMAGE_2, (PLANE_WIDTH, PLANE_HEIGHT)), 145)

PLANE_IMAGE_RED = pygame.image.load(
    os.path.join('Plane Icon Red.png'))
PLANE_RED = pygame.transform.rotate(pygame.transform.scale(
    PLANE_IMAGE_RED, (PLANE_WIDTH, PLANE_HEIGHT)), -45)

PLANE_IMAGE_2_RED = pygame.image.load(
    os.path.join('Plane Icon Red.png'))
PLANE_2_RED = pygame.transform.rotate(pygame.transform.scale(
    PLANE_IMAGE_2_RED, (PLANE_WIDTH, PLANE_HEIGHT)), 145)

# Display In-Game
def draw_window(plane , plane_2, plane_red, plane_2_red):
    WIN.fill(DARK_GREEN)
    pygame.draw.rect(WIN, DARK_GREEN, BORDER)
    radar()
    WIN.blit(PLANE, (plane.x, plane.y))
    WIN.blit(PLANE_2, (plane_2.x, plane_2.y))
    WIN.blit(PLANE_RED, (plane_red.x, plane_red.y))
    WIN.blit(PLANE_2_RED, (plane_2_red.x, plane_2_red.y))
    pygame.display.update()

def radar():
    TEN_NM = [325, 125, 250, 250]
    TWENTY_NM = [200, 0, 500, 500]
    FOURTY_NM = [75, -125, 750, 750]
    pygame.draw.ellipse(WIN, GREEN, TEN_NM, 2)
    pygame.draw.ellipse(WIN, GREEN, TWENTY_NM, 2)
    pygame.draw.ellipse(WIN, GREEN, FOURTY_NM, 2)

def plane_flashing(plane, plane_2):
    pygame.Surface.set_alpha(PLANE_RED, 0)
    pygame.Surface.set_alpha(PLANE_2_RED, 0)
    if plane.colliderect(plane_2):
        pygame.mixer.Sound.play(alarm)
        pygame.Surface.set_alpha(PLANE_RED, 255)
        pygame.Surface.set_alpha(PLANE_2_RED, 255)

# Controls Left Plane (WASD)
def plane_controls(keys_pressed, plane, plane_red):
    if keys_pressed[pygame.K_a] and (plane.x and plane_red.x) - VELOCITY > BORDER.x: # LEFT
        plane.x -= VELOCITY
        plane_red.x -= VELOCITY
    if keys_pressed[pygame.K_d] and (plane.x and plane_red.x) + VELOCITY + plane.width < WIDTH: # RIGHT
        plane.x += VELOCITY
        plane_red.x += VELOCITY
    if keys_pressed[pygame.K_w] and (plane.y and plane_red.y) - VELOCITY > BORDER.y: # UP
        plane.y -= VELOCITY
        plane_red.y -= VELOCITY
    if keys_pressed[pygame.K_s] and (plane.y and plane_red.y) + VELOCITY + plane.height < HEIGHT - 10: # DOWN
        plane.y += VELOCITY
        plane_red.y += VELOCITY

# Controls Right Plane (Arrow Keys)s
def plane_2_controls(keys_pressed, plane_2, plane_2_red):
    if keys_pressed[pygame.K_LEFT] and (plane_2.x and plane_2_red.x) - VELOCITY > BORDER.x: # LEFT
        plane_2.x -= VELOCITY
        plane_2_red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and (plane_2.x and plane_2_red.x) + VELOCITY + plane_2.width < WIDTH - 10: # RIGHT
        plane_2.x += VELOCITY
        plane_2_red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and (plane_2.y and plane_2_red.y) - VELOCITY > BORDER.y: # UP
        plane_2.y -= VELOCITY
        plane_2_red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and (plane_2.y and plane_2_red.y) + VELOCITY + plane_2.height < HEIGHT - 10: # DOWN
        plane_2.y += VELOCITY
        plane_2_red.y += VELOCITY


# Main Game Functions Loop
def main():
    plane = pygame.Rect(30, 30, PLANE_WIDTH, PLANE_HEIGHT)
    plane_2 = pygame.Rect(830, 430, PLANE_WIDTH, PLANE_HEIGHT)
    plane_red = pygame.Rect(30, 30, PLANE_WIDTH, PLANE_HEIGHT)
    plane_2_red = pygame.Rect(830, 430, PLANE_WIDTH, PLANE_HEIGHT)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()
        plane_flashing(plane, plane_2)
        plane_controls(keys_pressed, plane, plane_red)
        plane_2_controls(keys_pressed, plane_2, plane_2_red)
        draw_window(plane, plane_2, plane_red, plane_2_red)

        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
