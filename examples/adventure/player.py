from Engine.scenenode import *
from Engine.texturemanager import *
from Engine.inputmanager import *
from Engine.object import *

class Player(Object):

    def __init__(self):
        super().__init__()
        self.switch_texture("player_walk_right")
        self.size = (16, 24)
        self.direction = "down"
        self.speed = 64
        self.attacking = False

        # Subscribe to event
        evt_u = TextureManager.get_texture_info("player_attack_up").get_anim_event()
        evt_u += self.on_anim_finish
        evt_d = TextureManager.get_texture_info("player_attack_down").get_anim_event()
        evt_d += self.on_anim_finish
        evt_l = TextureManager.get_texture_info("player_attack_left").get_anim_event()
        evt_l += self.on_anim_finish
        evt_r = TextureManager.get_texture_info("player_attack_right").get_anim_event()
        evt_r += self.on_anim_finish

    def on_anim_finish(self):
        if not self.attacking:
           return

        self.attacking = False
        if self.direction == "up" and self.textureID == "player_attack_up":
            self.switch_texture("player_walk_up")

        elif self.direction == "down"  and self.textureID == "player_attack_down":
            self.switch_texture("player_walk_down")

        elif self.direction == "left" and self.textureID == "player_attack_left":
            self.switch_texture("player_walk_left")

        elif self.direction == "right" and self.textureID == "player_attack_right":
            self.switch_texture("player_walk_right")


    def update(self, delta):
        if not self.attacking:
            if InputManager.get_control("move_up"):
                self.move((0, -self.speed * delta))
                self.switch_texture("player_walk_up")
                self.direction = "up"

            if InputManager.get_control("move_down"):
                self.move((0, self.speed * delta))
                self.switch_texture("player_walk_down")
                self.direction = "down"

            if InputManager.get_control("move_left"):
                self.move((-self.speed * delta, 0))
                self.switch_texture("player_walk_left")
                self.direction = "left"

            if InputManager.get_control("move_right"):
                self.move((self.speed * delta, 0))
                self.switch_texture("player_walk_right")
                self.direction = "right"

        if InputManager.get_control_pressed("attack") and not self.attacking:
            if self.direction == "up":
                self.switch_texture("player_attack_up")

            elif self.direction == "down":
                self.switch_texture("player_attack_down")

            elif self.direction == "left":
                self.switch_texture("player_attack_left")

            elif self.direction == "right":
                self.switch_texture("player_attack_right")

            self.attacking = True
