from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.cool_down = 0
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        unit_vector = unit_vector.rotate(self.rotation)
        unit_vector *= PLAYER_SPEED * dt
        self.position += unit_vector

    def shoot(self):
        if self.cool_down > 0:
            return
        
        self.cool_down = PLAYER_SHOOT_COOLDOWN_SECONDS

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * self.radius
        shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)

        unit_vector = pygame.Vector2(0,1)
        shot.position += unit_vector
        unit_vector = unit_vector.rotate(self.rotation)
        unit_vector *= PLAYER_SHOT_SPEED
        shot.velocity = unit_vector

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cool_down -= dt

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
