"""This module handles the creation of a pygame app that simulates a parabolic motion
with the data recieved from the tkinter form"""

import math
import time
import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Square:
    """The square class creates a square on the pygame screen
    with the coordinates provided for its top left corner"""

    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.color = color
        self.l = 30
        self.x = x
        self.y = y

    def create(self):
        """The create method displays the square object to the screen
        after it is initialized"""
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.rect(self.screen, self.color, self.rect)


class Trayectory:
    """The Trayectory class determines where a particle would be in space
    at a certain time given a certain gravity, initial velocity and angle
    of said velocity"""

    def __init__(self, gravity, initialVelocity, angle) -> None:
        self.gravity = gravity
        self.initialVelocity = initialVelocity
        self.angle = angle
        self.time = 0
        self.vx = self.initialVelocity * (math.cos(math.radians(self.angle)))
        self.voy = self.initialVelocity * (math.sin(math.radians(self.angle)))

    def calculate(self, object, deltaTime):
        """The calculate method calculates a particle position if it has
        not touched the ground"""

        if object.y >= 570 and self.time > 0:
            self.vy = 0
            self.vx = 0
        else:
            self.time += deltaTime
            object.x = self.vx * self.time
            object.y = (
                (self.voy * self.time) - (0.5 * self.gravity * (self.time ** 2)) - 570
            ) * -1


class Text:
    """The text class displays text into a pygame screen"""

    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y

    def display(self, font, message):
        img = font.render(message, True, self.color)
        self.screen.blit(img, (self.x, self.y))


def run(grav, vel, ang):
    """The run function creates a functional pygame app"""
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("C:\Windows\Fonts\Arial", 24)
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Juego")
    particula = Trayectory(grav, vel, ang)
    cuadrado = Square(screen, 0, 0, (150, 230, 250))
    start = time.time()
    timeLabel = Text(screen, WHITE, 20, 20)
    distanceLabel = Text(screen, WHITE, 20, 40)
    heightLabel = Text(screen, WHITE, 20, 60)

    def show():
        """The show function handles the pieces that will be displayed
        to the screen and continuously update in the loop method"""
        nonlocal start
        delta = time.time() - start
        start = time.time()
        screen.fill([14, 41, 72])
        particula.calculate(cuadrado, delta)
        cuadrado.create()
        timeLabel.display(font, f" Time: {particula.time:.0f}s")
        distanceLabel.display(font, f" Height: {abs((cuadrado.y-600+30)*-1):.0f}m")
        heightLabel.display(font, f" Distance: {cuadrado.x:.0f}m")

    def loop():
        """The loop function ensures the window stays open indefinitely until
        it is closed, it calls the show function to dynamically update its
        contents"""
        run = True
        while run is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    return

            show()
            pygame.display.flip()
            clock.tick()

    loop()
