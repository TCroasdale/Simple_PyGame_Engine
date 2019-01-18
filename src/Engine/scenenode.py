"""
This module provides classes required for using scenenodes.
"""
from enum import Enum
from pygame.locals import Rect
from engine.texturemanager import TextureManager



class NodeType(Enum):
    """
    An enum representing whether a node is dynamic (can move) or static (Stationary, unable to move)
    """
    Dynamic = 0
    Static = 1

class SceneNode:
    """
    A Scene node which will be added to the scene graph. Can have an associated object attached to \
    it.
    """
    def __init__(self, parent=None, obj=None, n_type=NodeType.Dynamic):
        """
        Creates a Scene Node.

        Keyword arguments:
        parent -- The parent Scene Node of this Node. (default = None)
        object -- The object which will be attached to this object. (default = None)
        type -- The NodeType of this Node (default = NodeType.Dynamic)
        """
        self.children = []
        self.parent = parent
        if self.parent != None:
            self.parent.add_child(self)

        self.attached_object = None
        self.attach_object(obj)
        self.position = (50, 50)
        self.node_type = n_type

    def translate(self, amount):
        """
        Moves this node by amount.

        Keyword arguments:
        amount -- (tx, ty) How much to move this node by.
        """
        self.position = (self.position[0]+amount[0], self.position[1]+amount[1])

    def add_child(self, node):
        """
        Adds a child node to the children of this node.

        Keyword arguments:
        node -- The node to become a child of this
        """
        self.children.append(node)

    def attach_object(self, obj):
        """
        Attaches an object to this node.

        Keyword arguments:
        obj -- The Object to attach to this node.
        """
        if obj != None:
            self.attached_object = obj
            self.attached_object.setSceneNode(self)

    def get_world_position(self):
        """
        Returns the position of this node, relative to the world.

        Returns:
        A Tuple (x, y) representing the position of this node.
        """
        if self.parent is None:
            return self.position

        parentpos = self.parent.get_world_position()
        return (parentpos[0] + self.position[0], parentpos[1] + self.position[1])


    def get_bounds(self):
        """
        returns a Rectangle containing the attached object.

        Returns:
        a Rect containing the world position and size of this node.
        """
        return Rect(self.get_world_position(), self.attached_object.size)


    def handle_collision(self, coll_data):
        """
        Called when this node is in a collision

        Keyword arguments:
        coll_data -- The CollisionInformation Object describing the collision.
        """
        if self.attached_object != None:
            self.attached_object.handle_collision(coll_data)

    def update(self, delta):
        """
        Updates the attached object and calls update() on the children of this node.

        Keyword arguments:
        delta -- The time elapsed since update() was last called.
        """
        if self.attached_object != None:
            self.attached_object.update(delta)

        for child in self.children:
            child.update(delta)

    def render(self, screen):
        """
        Draws the attached object to screen, and called render() on children nodes.

        Keyword arguments:
        screen -- The Pygame surface to blit the attached object to.
        """
        if self.attached_object != None:
            texture = TextureManager.get_texture(self.attached_object.textureID)
            rect = Rect(self.get_world_position(), self.attached_object.size)
            screen.blit(texture, rect)

        for child in self.children:
            child.render(screen)

    def get_all_children(self):
        """
        Returns a list of every child node beneath this node in the scene graph.

        Returns:
        A list of SceneNodes
        """
        all_children = []
        for child in self.children:
            all_children += [child]
            all_children += child.get_all_children()
        return all_children

    def to_string(self, numtabs=0):
        """
        A simple function to print the scenegraph beneath this node to the console.

        Keyword arguments:
        numtabs -- The number of tabs to put before printing the node. (default = 0)
        """
        print(" "*numtabs, "node")
        for child in self.children:
            child.print_to_console(numtabs+1)


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
