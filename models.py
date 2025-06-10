import pygame

class Player:
    
    position = pygame.Vector2(0, 0)
    
    def __init__(self, position):
        self.position = position
    
    def movement_change(self, keys):
        direction = None
        
        if keys[pygame.K_w]:
            direction = "up"
        if keys[pygame.K_s]:
            direction = "down"
        if keys[pygame.K_a]:
            direction = "left"
        if keys[pygame.K_d]:
            direction = "right"
            
        return direction
        
    def move(self, direction, delta_time):
        if direction == "up":
            self.position.y -= 300 * delta_time
        if direction == "down":
            self.position.y += 300 * delta_time
        if direction == "left":
            self.position.x -= 300 * delta_time
        if direction == "right":
            self.position.x += 300 * delta_time
            
        