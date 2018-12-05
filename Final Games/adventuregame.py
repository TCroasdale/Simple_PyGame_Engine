import pygame
from pygame.locals import *

from Engine.scenenode import *
from player import *
from game import *


class AdventureGame(Game):

    # This functions will create objects and add them to the scene.
    def create_scene(self):
        self.player = Player()
        SceneNode(self.rootSceneNode, self.player)
        return

if __name__ == "__main__":
    AdventureGame.start_game( AdventureGame())
