from Engine.texturemanager import *

class SceneNode:

    def __init__(self, parent=None, object=None):
        self.children = []
        self.parent = parent
        if self.parent != None:
            self.parent.addChild(self)

        self.attachedObject = None
        self.attachObject(object)
        self.position = (50, 50)

    def addChild(self, node):
        self.children.append(node)
        node.setParent(self)

    def setParent(self, node):
        self.parent = node

    def attachObject(self, obj):
        if obj != None:
            self.attachedObject = obj
            self.attachedObject.setSceneNode(self)

    def getWorldPosition(self):
        if self.parent == None:
            return self.position

        parentpos = self.parent.getWorldPosition()
        return (parentpos[0] + self.position[0], parentpos[1] + self.position[1])



    def update(self, delta):
        if self.attachedObject != None:
            self.attachedObject.update(delta)

        for child in self.children:
            child.update(delta)

    def render(self, screen):
        if self.attachedObject != None:
            texture = TextureManager.get_texture(self.attachedObject.textureID)
            rect = Rect(self.getWorldPosition(), self.attachedObject.size)
            screen.blit(texture, rect)

        for child in self.children:
            child.render(screen)
