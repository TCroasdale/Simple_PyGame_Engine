
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

    def move(self, amount):
        self.node.translate(amount)
