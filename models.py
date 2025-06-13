import pygame

class Player:
    
    def __init__(self, position, player_radius):
        self.position = position
        self.last_position = self.position
        self.directions = {"up": "down", 
                           "down": "up", 
                           "left": "right", 
                           "right": "left",
                           "": "abcd"
                           }
        self.is_colliding = False
                
        col_x = self.position.x - player_radius
        col_y = self.position.y - player_radius
        
        self.collider = pygame.Rect((col_x, col_y), (player_radius * 2, player_radius * 2))
    
    def draw(self, screen, radius):
        #pygame.draw.rect(screen, pygame.Color("green"), self.collider)
        pygame.draw.circle(screen, pygame.Color("yellow"), self.position, radius)  
    
    def checkMovementChange(self, keys):
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
            self.last_position = self.position
            self.position.y -= 300 * delta_time
            
        if direction == "down":
            self.last_position = self.position
            self.position.y += 300 * delta_time
            
        if direction == "left":
            self.last_position = self.position
            self.position.x -= 300 * delta_time
            
        if direction == "right":
            self.last_position = self.position
            self.position.x += 300 * delta_time
            
        self.collider.center = (self.position.x, self.position.y)
        
    def getLastPosition(self):
        return self.last_position
            
            
class Reward:
 
    def __init__(self, position, reward_radius):
        self.position = position
        
        col_x = self.position.x - reward_radius
        col_y = self.position.y - reward_radius
        
        self.collider = pygame.Rect((col_x, col_y), (reward_radius * 2, reward_radius * 2))
        
    def draw(self, screen, radius):
        #pygame.draw.rect(screen, pygame.Color("green"), self.collider)
        pygame.draw.circle(screen, pygame.Color("white"), self.position, radius)  
        
        
class Wall:
 
    def __init__(self, position, reward_radius):
        self.position = position
        
        col_x = self.position.x - reward_radius
        col_y = self.position.y - reward_radius
        
        self.collider = pygame.Rect((col_x, col_y), (reward_radius * 2, reward_radius * 2))
        
    def draw(self, screen, radius):
        #pygame.draw.rect(screen, pygame.Color("green"), self.collider)
        pygame.draw.rect(screen, pygame.Color("white"), self.collider)  