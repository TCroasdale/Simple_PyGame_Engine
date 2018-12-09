import pygame
from pygame.locals import *

from Engine.scenenode import *
from Engine.levelmanager import *
from player import *
from game import *


class AdventureGame(Game):

    # This functions will create objects and add them to the scene.
    def create_scene(self):
        self.player = Player()
        SceneNode(self.rootSceneNode, self.player)

        LevelManager.load_level('level1')

if __name__ == "__main__":
    AdventureGame.start_game( AdventureGame())
