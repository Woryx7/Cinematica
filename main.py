import pygame
import math
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)

class Square:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.color = (150, 230, 250)
        self.l = 30
        self.x = x
        self.y = y

    def create(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.rect(self.screen, self.color, self.rect)

class Trayectory:

    def __init__(self,gravity,initialVelocity,angle) -> None:
        self.gravity = gravity
        self.initialVelocity = initialVelocity
        self.angle = angle
        self.time = 0
        self.vx = self.initialVelocity*(math.cos(math.radians(self.angle)))
        self.voy = self.initialVelocity*(math.sin(math.radians(self.angle)))
    
    def calculate(self, object, deltaTime):
        if object.y >= 570 and self.time > 0:
            self.vy = 0
            self.vx = 0
        else:
            self.time += deltaTime
            object.x = self.vx*self.time
            object.y = ((self.voy*self.time)-(0.5*self.gravity*(self.time**2))-570)*-1

class Text:
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
    def display(self, font, message):
        img = font.render(message, True, self.color)
        self.screen.blit(img, (self.x, self.y))

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("C:\Windows\Fonts\Arial", 24)
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Juego")
        self.particula = Trayectory(9.81,50,45)
        self.cuadrado = Square(self.screen,0,0)
        self.start = time.time()
        self.timeLabel = Text(self.screen,GREEN,20,20)
        self.distanceLabel = Text(self.screen,GREEN,20,40)
        self.heightLabel = Text(self.screen,GREEN,20,60)
        self.dLabel = Text(self.screen,GREEN,20,80)
        self.loop()
    def loop(self):
        run = True
        while run == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.execute()
            pygame.display.flip()
    def execute(self):
        delta = time.time() - self.start
        self.start = time.time()
        self.screen.fill([0,0,0])
        self.particula.calculate(self.cuadrado,delta)
        self.cuadrado.create()
        self.timeLabel.display(self.font, f" Time: {self.particula.time:.0f}s")
        self.distanceLabel.display(self.font, f" Height: {abs((self.cuadrado.y-600+30)*-1):.0f}m")
        self.heightLabel.display(self.font, f" Distance: {self.cuadrado.x:.0f}m")
def main():
    Game()
main()
