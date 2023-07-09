# Example file showing a circle moving on screen
import pygame
from IO.Controller import Controller, ControllerType
from IO.Button import State, ButtonInput

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

cont = Controller(0,ControllerType.JOYSTICK)

color = "red"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, color, player_pos, 40)

    cont.getInput()

    for button in cont.buttonMap.values():
        if button.get_state() == State.PRESSED or button.get_state() == State.HELD:
            if button.buttonType == ButtonInput.UP:
                player_pos.y -= 300 *dt
            if button.buttonType == ButtonInput.DOWN:
                player_pos.y += 300 *dt
            if button.buttonType == ButtonInput.LEFT:
                player_pos.x -= 300 *dt
            if button.buttonType == ButtonInput.RIGHT:
                player_pos.x += 300 *dt
            if button.buttonType == ButtonInput.A and button.get_state() == State.PRESSED:
                if color == "red":
                    color = "green"
                elif color == "green":
                    color = "red"
            if button.buttonType == ButtonInput.X:
                color = "blue"

    '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
    '''
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()