import pygame
from models import Player, Reward

DISPLAY_WIDHT = 900
DISPLAY_HEIGHT = 600
REWARD_SPACING = 70

PLAYER_RADIUS = 20
REWARD_RADIUS = 5

#Initializing game
pygame.init()
pygame.display.set_caption("Pacman")
screen = pygame.display.set_mode((DISPLAY_WIDHT, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
running = True

delta_time = 0
direction = "" #Non moving direction

# Rewards array
rewards = []

for a in range(REWARD_SPACING, DISPLAY_HEIGHT, REWARD_SPACING):
    for b in range(REWARD_SPACING, DISPLAY_WIDHT, REWARD_SPACING):
        reward_pos = pygame.Vector2(a, b)
        rewards.append(Reward(reward_pos, REWARD_RADIUS))

#Initializing Player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = Player(player_pos, PLAYER_RADIUS)

while running:
    #pygame.QUIT means the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if rewards == []:
        running = False
    
    #Draw the background
    screen.fill(pygame.Color("black"))
    
    #Draw Player
    player.draw(screen, PLAYER_RADIUS)
    
    #Draw Rewards
    for reward in rewards:
        if pygame.Rect.colliderect(player.collider, reward.collider):
            rewards.remove(reward)
            print(rewards)
        else:
            reward.draw(screen, REWARD_RADIUS)
    
    #Player movement
    keys = pygame.key.get_pressed()
    movement = player.check_movement_change(keys)
    
    if movement != None:
        direction = movement
    
    player.move(direction, delta_time)

    pygame.display.flip()
    
    delta_time = clock.tick(60) / 1000

pygame.quit()
