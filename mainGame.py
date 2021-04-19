import pygame
from pygame.locals import *
import time
from SnakeGame.apple import Apple
from SnakeGame.snake import Snake
from SnakeGame.collision import collision

class Game:
    def __init__(self):

        pygame.init()
        self.surface = pygame.display.set_mode((600, 600))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.factor = 0.3
        self.stopExec = False

    def speed(self):
        time.sleep(self.factor)

    def play(self):
        if not self.stopExec:
            self.snake.move()

        # Collision with walls
        coordinates = [-40, 600]
        if self.snake.x[0] in coordinates or self.snake.y[0] in coordinates:
            self.game_over()

        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move_apple(self.snake.x,self.snake.y,self.snake.length)
            if self.factor > 0.1:
                self.factor = self.factor - 0.01

        # NEAR MISS
        direction_array = [["left","right"],["up","down"]]
        for i in range(2,self.snake.length):

            if self.snake.y[0] == self.snake.y[i] and self.snake.direction in direction_array[0]:
                if abs(self.snake.x[0] - self.snake.x[i]) == 40 and i > 2:
                    time.sleep(0.5)
            if self.snake.x[0] == self.snake.x[i] and self.snake.direction in direction_array[1]:
                if abs(self.snake.y[0] - self.snake.y[i]) == 40 and i > 2:
                    time.sleep(0.5)

            if collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.game_over()

    def paused_game(self,pausedGame):
        if pausedGame:
            font = pygame.font.SysFont('arial', 60)
            pauseText = font.render("The game is paused", True, (200, 200, 200))
            self.surface.blit(pauseText, (100, 300))

    def display_score(self):
        font = pygame.font.SysFont('arial', 20)
        score = font.render(f"Score: {self.snake.length-2}", True, (200, 200, 200))
        self.surface.blit(score, (500, 10))

    def game_over(self):
        self.stopExec = True
        font = pygame.font.SysFont('arial', 40)
        gameOver = font.render("GAME OVER! press SPACE to restart", True, (200, 200, 200))
        esc = font.render("Press ESC to quit", True, (200, 200, 200))
        finalScore = font.render(f"Final Score: {self.snake.length-2}", True, (200, 200, 200))
        self.surface.blit(gameOver, (10, 30))
        self.surface.blit(esc, (10, 70))
        self.surface.blit(finalScore, (10, 110))

    def reset(self):
        self.snake = Snake(self.surface,2)
        self.apple = Apple(self.surface)
        self.factor = 0.3

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        self.stopExec = not self.stopExec
                        self.paused_game(self.stopExec)
                    if event.key == K_SPACE:
                        if self.stopExec:
                            self.reset()
                            self.stopExec = False

                    if self.snake.moveHorizontal:
                        if event.key == K_RIGHT:
                            self.snake.moveHorizontal = False
                            self.snake.direction = 'right'

                    if self.snake.moveHorizontal:
                        if event.key == K_LEFT:
                            self.snake.moveHorizontal = False
                            self.snake.direction = 'left'

                    if self.snake.moveVertical:
                        if event.key == K_DOWN:
                            self.snake.moveVertical = False
                            self.snake.direction = 'down'

                    if self.snake.moveVertical:
                        if event.key == K_UP:
                            self.snake.moveVertical = False
                            self.snake.direction = 'up'

                elif event.type == QUIT:
                    running = False
            self.play()
            self.speed()

if __name__== '__main__':
    game = Game()
    game.run()