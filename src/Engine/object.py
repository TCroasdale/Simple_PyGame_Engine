from Engine.texturemanager import *

class Object:
    def __init__(self, scenenode=None):
        self.textureID = 'steve'
        self.size = (32, 32)
        self.node = scenenode

    def setTextureID(self, id):
        self.textureID = idea

    def setSize(self, size):
        self.size = size

    def setSceneNode(self, node):
        self.node = node

    def update(self, delta):
        return

    def handle_collision(self, collision_data):
        return

    def move(self, amount):
        self.node.translate(amount)

    def switch_texture(self, newTexture):
        if self.textureID == newTexture:
            return
        TextureManager.get_texture_info(newTexture).reset_anim()
        self.textureID = newTexture
