# https://www.pygame.org/docs/
from calendar import c
from tkinter import W
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
WIDTH, HEIGHT = 1280, 720
clock = pygame.time.Clock()
running = True
FPS = 60
#Character_image = pygame.image.load('character.png')
#character_image = pygame.transform.scale(character_image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_WIDTH, CHARACTER_HEIGHT= 50, 50
CHARACTER_COLOR = (0, 128, 255)
class Character:
    def __init__(self):
            self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, CHARACTER_WIDTH, CHARACTER_HEIGHT)
            self.speed = 5
        
    def move(self, dx, dy):
            self.rect.x += dx
            self.rect.y += dy
            
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > WIDTH - CHARACTER_WIDTH:
                self.rect.x = WIDTH - CHARACTER_WIDTH
            if self.rect.y < 0 :
                self.rect.y = 0
            if self.rect.y > HEIGHT - CHARACTER_HEIGHT:
                self.rect.y = HEIGHT - CHARACTER_HEIGHT
    def draw(self, screen):
            pygame.draw.rect(screen, CHARACTER_COLOR, self.rect)
   
            
character = Character()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("pink")
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -character.speed 
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = character.speed 
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -character.speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = character.speed
    
    character.move(dx,dy)
    character.draw(screen)



    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()
