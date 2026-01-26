import pygame
import sys
from logger import log_state, log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}\n' + 
          f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    clock = pygame.time.Clock()
    dt = 0

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        log_state()
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()
            

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
