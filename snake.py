import pygame
POSITION = 40
class Snake:
    def __init__(self, parent_screen, length):

        self.parent_screen = parent_screen
        self.length = length
        self.image = pygame.image.load("block.jpg").convert()
        self.direction = 'down'
        self.x = [POSITION] * length
        self.y = [POSITION] * length
        self.moveVertical = False
        self.moveHorizontal = True

    def move(self):

        if self.direction == 'right':
            self.x[0] += POSITION
            self.moveVertical = True
        if self.direction == 'left':
            self.x[0] -= POSITION
            self.moveVertical = True
        if self.direction == 'down':
            self.y[0] += POSITION
            self.moveHorizontal = True
        if self.direction == 'up':
            self.y[0] -= POSITION
            self.moveHorizontal = True
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        self.draw()

    # update body
    def draw(self):
        # color
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):

        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
