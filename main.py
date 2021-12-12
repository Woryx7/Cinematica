import pygame
import math
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Square:
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.color = color
        self.l = 30
        self.x = x
        self.y = y

    def create(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.rect(self.screen, self.color, self.rect)


class Trayectory:
    def __init__(self, gravity, initialVelocity, angle) -> None:
        self.gravity = gravity
        self.initialVelocity = initialVelocity
        self.angle = angle
        self.time = 0
        self.vx = self.initialVelocity * (math.cos(math.radians(self.angle)))
        self.voy = self.initialVelocity * (math.sin(math.radians(self.angle)))

    def calculate(self, object, deltaTime):
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
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y

    def display(self, font, message):
        img = font.render(message, True, self.color)
        self.screen.blit(img, (self.x, self.y))


def run():
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("C:\Windows\Fonts\Arial", 24)
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Juego")
    particula = Trayectory(9.81, 50, 45)
    cuadrado = Square(screen, 0, 0, (150, 230, 250))
    start = time.time()
    timeLabel = Text(screen, GREEN, 20, 20)
    distanceLabel = Text(screen, GREEN, 20, 40)
    heightLabel = Text(screen, GREEN, 20, 60)

    def menu1():
        nonlocal start
        delta = time.time() - start
        start = time.time()
        screen.fill([0, 0, 0])
        particula.calculate(cuadrado, delta)
        cuadrado.create()
        timeLabel.display(font, f" Time: {particula.time:.0f}s")
        distanceLabel.display(font, f" Height: {abs((cuadrado.y-600+30)*-1):.0f}m")
        heightLabel.display(font, f" Distance: {cuadrado.x:.0f}m")
    

    def loop():
        run = True
        while run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            menu1()
            pygame.display.flip()

    loop()


def main():
    run()


main()
