from Engine.inputmanager import *
from Engine.object import *

class Player(Object):

    def __init__(self):
        super().__init__()
        self.textureID = "player_walk_right"
        # self.size = (64, 64)

        self.speed = 16

    def update(self, delta):
        if InputManager.get_control("move_up"):
            self.move((0, -self.speed * delta))
        if InputManager.get_control("move_down"):
            self.move((0, self.speed * delta))
        if InputManager.get_control("move_left"):
            self.move((-self.speed * delta, 0))
            self.textureID = "player_walk_left"
        if InputManager.get_control("move_right"):
            self.move((self.speed * delta, 0))
            self.textureID = "player_walk_right"
