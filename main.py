import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    X = SCREEN_WIDTH / 2
    Y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(X, Y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)

        for p in updatable:
            p.update(dt)

        for p in drawable:
            p.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
