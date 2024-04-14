import pygame 
from settings import * 
from wall import Wall
from helper import read_json_file
from snake import Snake
from food import Food 
import random

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.wall = pygame.sprite.Group()
        self.snake = pygame.sprite.GroupSingle()
        self.food = pygame.sprite.GroupSingle()
        self.settings = read_json_file("./resources/settings/settings.json")

        self.wall_coordinates = []
        self.flag = True 

        self.setup()

    def crash_wall(self):
        for sprite in self.wall.sprites():
            if sprite.rect.colliderect(self.snake.sprite.rect):
                self.flag = False 

    def bite_tail(self):
        c = 0
        for sprite in self.snake.sprite.tail.sprites():
            if sprite.rect.colliderect(self.snake.sprite.rect):
                c += 1
        if c > 1:
            self.flag = False 

    def food_pos_control(self,pos):
        if pos not in self.wall_coordinates and pos != (self.snake.sprite.rect.x,self.snake.sprite.rect.y):
            for sprite in self.snake.sprite.tail.sprites():
                if pos == (sprite.rect.x,sprite.rect.y):
                     return False
            return True
        else:
            return False
       
    def food_change_pos(self):
        while True:
            x = random.randint(1, 19) * size
            y = random.randint(1, 19) * size
            if self.food_pos_control((x,y)):
                break

        self.food.sprite.rect.x = x
        self.food.sprite.rect.y = y               
                
    def eat(self):
        if self.snake.sprite.rect.colliderect(self.food.sprite.rect):
            self.snake.sprite.score += 1
            self.food_change_pos()

    def setup(self):
        for row_index,row in enumerate(MAP[self.settings["map"]]):
            for column_index,cell in enumerate(row):
                x = column_index * size 
                y = row_index * size 

                if cell == "0":
                    self.wall.add(Wall((x,y)))
                    self.wall_coordinates.append((x,y))
                if cell == "P":
                    self.snake.add(Snake((x,y)))
                if cell == "F":
                    self.food.add(Food((x,y)))

    def loop(self):
        self.wall.draw(self.display_surface)
        self.food.draw(self.display_surface)
        self.snake.draw(self.display_surface)
        self.snake.update()

        self.eat()
        self.bite_tail()
        self.crash_wall()