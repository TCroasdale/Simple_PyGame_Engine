import pygame
from pygame.locals import *

from engine.scenenode import *
from engine.levelmanager import *
from platformerplayer import *
from game import *


class PlatformerGame(Game):

    # This functions will create objects and add them to the scene.
    def create_scene(self):
        self.player = PlatformerPlayer()
        SceneNode(self.rootSceneNode, self.player)

        LevelManager.load_level('castle')

if __name__ == "__main__":
    PlatformerGame.start_game( PlatformerGame())
