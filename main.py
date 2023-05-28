import pygame
import os

pygame.init()

#Global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Char", "CharRun1.png")), 
           pygame.image.load(os.path.join("Assets/Char", "CharRun2.png"))]

JUMMPING = pygame.image.load(os.path.join("Assets/Char", "CharJump.png"))

DUCKING = [pygame.image.load(os.path.join("Assets/Char", "CharDuck1.png")),
           pygame.image.load(os.path.join("Assets/Char", "CharDuck2.png"))]

SMALL_TRAP = pygame.image.load(os.path.join("Assets/Traps", "SmallTrap.png"))
LARGE_TRAP = pygame.image.load(os.path.join("Assets/Traps", "LargeTrap.png"))

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")), 
           pygame.image.load(os.path.join("Assets/Bird", "Bird2.png")), 
           pygame.image.load(os.path.join("Assets/Bird", "Bird3.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "bg1.png"))


class Character:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMMPING
        
        self.char_duck = False
        self.char_run = True 
        self.char_jump = False
        
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.char_rect = self.image.get_rect()
        self.char_rect.x = self.X_POS
        self.char_rect.y - self.Y_POS
        
    def update(self, userInput):
        if self.char_duck:
            self.duck()
        if self.char_run:
            self.run()
        if self.char_jump:
            self.jump()
        
        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.char_jump:
           self.char_duck = False
           self.char_run = False
           self.char_jump = True
        elif userInput[pygame.K_DOWN] and not self.char_jump:
           self.char_duck = True
           self.char_run = False
           self.char_jump = False
        elif not (self.char_jump or userInput[pygame.K_DOWN]):
           self.char_duck = False
           self.char_run = True
           self.char_jump = False

    def duck (self):
        self.image = self.duck_img[self.step_index // 5]
        self.char_rect = self.image.get_rect()
        self.char_rect.x = self.X_POS
        self.char_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.char_rect = self.image.get_rect()
        self.char_rect.x = self.X_POS
        self.char_rect.y = self.Y_POS
        self.step_index += 1




    def jump(self):
        self.image = self.jump_img
        if self.char_jump:
            self.char_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.char_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
     SCREEN.blit(self.image, (self.char_rect.x, self.char_rect.y))





def main():
    run = True
    clock = pygame.time.Clock()
    player = Character()
   
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()         
    
        player.draw(SCREEN)
        player.update(userInput)
        
        clock.tick(30)
        pygame.display.update()
    



main()
