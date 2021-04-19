import pygame
import random
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple.jpg").convert()
        self.x = 280
        self.y = 280

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move_apple(self,x,y,length):
        if length < 225:
            random_x = random.randint(1, 14) * 40
            random_y = random.randint(1, 14) * 40
            i = 0
            while i < length:
                if random_x == x[i] and random_y == y[i]:
                    random_x = random.randint(1, 14) * 40
                    random_y = random.randint(1, 14) * 40
                    i = -1
                i = i + 1
            self.x = random_x
            self.y = random_y
        else:
            print("Well done you beat the game")
            exit()