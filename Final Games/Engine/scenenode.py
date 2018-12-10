from Engine.texturemanager import *
from enum import Enum


class NodeType(Enum):
    Dynamic = 0
    Static = 1

class SceneNode:

    def __init__(self, parent=None, object=None, type=NodeType.Dynamic):
        self.children = []
        self.parent = parent
        if self.parent != None:
            self.parent.addChild(self)

        self.attachedObject = None
        self.attachObject(object)
        self.position = (50, 50)
        self.nodeType = type

    def translate(self, amount):
        self.position = (self.position[0]+amount[0], self.position[1]+amount[1])

    def addChild(self, node):
        self.children.append(node)

    def attachObject(self, obj):
        if obj != None:
            self.attachedObject = obj
            self.attachedObject.setSceneNode(self)

    def getWorldPosition(self):
        if self.parent == None:
            return self.position

        parentpos = self.parent.getWorldPosition()
        return (parentpos[0] + self.position[0], parentpos[1] + self.position[1])


    def getBounds(self):
        return Rect(self.getWorldPosition(), self.attachedObject.size)


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

    def get_all_children(self):
        if len(self.children) == 0:
            return []
        else:
            all_children = []
            for child in self.children:
                all_children += [child]
                all_children += child.get_all_children()
            return all_children

    def to_string(self, numtabs=0):
        print(" "*numtabs, "node")
        for child in self.children:
            child.to_string


    #Iterator Functions
    def __iter__(self):
        self.n = 0
        self.recursive_children = self.get_all_children()
        return self

    def __next__(self): #def next() if py2
        self.n += 1
        if self.n >= len(self.recursive_children):
            raise StopIteration
        else:
            return self.recursive_children[self.n]
