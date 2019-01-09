from Engine.scenenode import *
from Engine.texturemanager import *
from Engine.inputmanager import *
from Engine.physicsmanager import *
from Engine.object import *

class PlatformerPlayer(Object):

    def __init__(self):
        super().__init__()
        self.switch_texture("player_walk_right")
        self.size = (16, 24)
        self.direction = "down"
        self.speed = (0, 0)
        self.moveSpeed = 64


    def update(self, deltaTime):
        if InputManager.get_control("move_left"):
            self.speed = ((-self.moveSpeed * deltaTime, self.speed[1]))
            self.switch_texture("player_walk_left")
            self.direction = "left"

        elif InputManager.get_control("move_right"):
            self.speed = ((self.moveSpeed * deltaTime, self.speed[1]))
            self.switch_texture("player_walk_right")
            self.direction = "right"

        else:
            self.speed = ((0, self.speed[1]))
            self.switch_texture("player_walk_down")
            self.direction = "down"

        self.speed = (self.speed[0], self.speed[1] + (9.8 * deltaTime))
        self.move(self.speed)

    def handle_collision(self, coll_data):
        if coll_data.direction == CollisionDirection.Bottom:
            self.speed = (self.speed[0], 0)

