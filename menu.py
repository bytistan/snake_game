import pygame 
from settings import *
from helper import read_json_file, update_json_file
import sys 
from game import Game

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.settings = read_json_file("./resources/settings/settings.json")

        self.page = {
            0:"home",
            1:"play",
            2:"settings",
            3:"map",
            4:"speed",
            5:"sound",
            6:"pause"
        }

        self.arrow_index = 0
        self.page_number = 0

        self.key_pressed = False 
        self.flag = False

        self.space = {
            0:{
                1:2
            },
            2:{
                0:3,
                1:4,
                2:5
            }
        }

        self.coordinate = {
            "home":[(80,161),(80,220),(80,283)],
            "settings":[(80,158),(80,222),(80,286)]
        }

        self.arrow_controller = {
            "home":{
                "controller":{
                    pygame.K_UP:self.change_arrow_position,
                    pygame.K_DOWN:self.change_arrow_position
                }
            },
            "settings":{
                "controller":{
                    pygame.K_UP:self.change_arrow_position,
                    pygame.K_DOWN:self.change_arrow_position
                }
            },
            "map":{
                "controller":{
                    pygame.K_LEFT:self.change_map,
                    pygame.K_RIGHT:self.change_map
                }
            },
            "sound":{
                "controller":{
                    pygame.K_LEFT:self.change_sound,
                    pygame.K_RIGHT:self.change_sound
                }
            },
            "speed":{
                "controller":{
                    pygame.K_LEFT:self.change_speed,
                    pygame.K_RIGHT:self.change_speed
                }
            }
        }

        self.game = Game()
        self.pause = False 

    def exit(self):
        pygame.quit()
        sys.exit() 

    def change_speed(self,event):
        if event.key == pygame.K_RIGHT and self.settings["speed"] % 3 < len(speed_image) - 1:
            self.settings["speed"] += 4
        if event.key == pygame.K_LEFT and self.settings["speed"] % 3 > 0:
            self.settings["speed"] -= 4

    def change_sound(self,event):
        if event.key == pygame.K_RIGHT and self.settings["sound"] < 2:
            self.settings["sound"] += 1
        if event.key == pygame.K_LEFT and self.settings["sound"] > 0:
            self.settings["sound"] -= 1

    def change_map(self,event):
        if event.key == pygame.K_LEFT:
            if self.settings["map"] > 0:
                self.settings["map"] -= 1
            else: 
                self.settings["map"] = len(MAP) - 1

        elif event.key == pygame.K_RIGHT:
            if self.settings["map"] < len(MAP) - 1:
                self.settings["map"] += 1
            else:
                self.settings["map"] = 0

    def change_page(self,event):
        if event.key == pygame.K_ESCAPE:
            if self.page_number in [3,4,5]:
                self.page_number = 2
            elif self.page_number == 2:
                self.page_number = 0
        elif event.key == pygame.K_SPACE: 
            self.page_number = self.space[self.page_number][self.arrow_index]
        self.arrow_index = 0

    def set_settings(self,event):
        self.page_number = 2
        return update_json_file("./resources/settings/settings.json",self.settings)

    def change_arrow_position(self,event):
        if self.arrow_index < len(self.coordinate[self.page[self.page_number]]) - 1 and event.key == pygame.K_DOWN:
            self.arrow_index += 1
        if self.arrow_index > 0 and event.key == pygame.K_UP:
            self.arrow_index -= 1
    
    def input(self,event):
        if event.type == pygame.KEYDOWN and not self.key_pressed:
            self.key_pressed = True
            self.action_handler(event)
        elif event.type == pygame.KEYUP:
            self.key_pressed = False         

    def event_loop(self):
        for event in pygame.event.get():
            if not self.flag:
                self.input(event)

            if self.flag:
                if event.type == pygame.K_ESCAPE:
                    self.pause = True
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    

    def action_handler(self,event):
        if event.key in [pygame.K_SPACE,pygame.K_ESCAPE]:
            if self.page_number in [0,2]:
                if self.arrow_index == 0 and self.page_number == 0:
                    self.flag = True
                    self.game.flag = True
                    self.game.c = True
                else:
                    self.change_page(event)
            else:
                self.set_settings(event)

        elif event.key in self.arrow_controller[self.page[self.page_number]]["controller"].keys():
            self.arrow_controller[self.page[self.page_number]]["controller"][event.key](event)

    def draw(self):
        for data in page[self.page[self.page_number]]:
            self.display_surface.blit(data["img"],data["coordinate"])
        
        if self.page_number in [0,2]:
            self.display_surface.blit(arrow_info["img"],(self.coordinate[self.page[self.page_number]][self.arrow_index][0]-42,self.coordinate[self.page[self.page_number]][self.arrow_index][1]))

        if self.page_number == 3:
            self.display_surface.blit(map_image[self.settings["map"]],(177,125))

        if self.page_number == 4:
            self.display_surface.blit(speed_image[self.settings["speed"]%3]["img"],speed_image[self.settings["speed"]%3]["coordinate"])

        if self.page_number == 5:
            self.display_surface.blit(sound_image[self.settings["sound"]]["img"],sound_image[self.settings["sound"]]["coordinate"])

    def update(self):
        self.event_loop()
        if not self.flag:
            self.draw()
        else:
            self.game.update(self.pause)
            if not self.game.flag:
                self.flag = False
                self.game.clean()