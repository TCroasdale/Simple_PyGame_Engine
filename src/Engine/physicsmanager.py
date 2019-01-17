import pygame
from pygame.locals import *
from src.engine.scenenode import *

from enum import Enum


class CollisionDirection(Enum):
    """
    Collision Direction specifies the direction from which a collider hits the other collider
    i.e Top means the other collider is above this collider
    """
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3

class CollisionInformation:
    """
    Class containing relevant information from a collision.
    """
    def __init__(self, colDir, centerpos, otherNode=None):
        """
        Constructor for this class.

        Keyword arguments:
        colDir -- The CollisionDirection of the described collision.
        centerpos -- The center position of the Collision.4
        otherNode -- The other node affected by this collision, may not exist. (default = None)
        """
        self.direction = colDir
        self.position = centerpos
        self.otherNode = otherNode

    def __str__(self):
        """
        returns the string representation of this class.
        """
        return "Direction: {0}, centerposition: {1}, against: {2}".format(self.direction, self.position, self.otherNode)

class PhysicsManager:
    """
    Manager class for physics calculations and representations.
    """
    def add_collider(rectangle):
        """
        Adds a static rectangle collider to the scene.

        Keyword arguments:
        rectangle -- The Rect to add to the scene.
        """
        if PhysicsManager.colliders == None:
            PhysicsManager.colliders = []

        print("Adding Collider: {0}".format(rectangle))
        PhysicsManager.colliders += [rectangle]

    def remove_all_colliders():
        """
        Clears all static rectangle colliders from the scene.
        """
        PhysicsManager.colliders = []

    def draw_debug(size, rootNode):
        """
        Draws all the colliders to the screen in transparent green.

        Keyword arguments:
        size -- The size of the surface to create and draw to.
        rootNode -- The root scene node of the scene.
        
        Returns:
        A pygame surface with all colliders drawn to it.
        """
        surf = pygame.Surface(size)
        surf.set_alpha(128)    
        for wall in PhysicsManager.colliders:
            pygame.draw.rect(surf, (0, 255, 0, 150), wall)

        for node1 in rootNode.get_all_children():
            pygame.draw.rect(surf, (0, 255, 0, 150), node1.getBounds())
        return surf

    def handle_collision(node1, node2):
        """
        Called upon finding a collision. Fixes the collisions, and tells the scenenodes to handle_collision.

        Keyword arguments:
        node1 -- The primary node of the collision, will be the one reacting to the collision
        node2 -- The secondary node of the collision, or a Rect object of a static coliider.
        """
        if type(node2) != Rect:
            node2 = node2.getBounds
        newRect = node1.getBounds().clip(node2)    
            
        if node1.nodeType == NodeType.Dynamic:
            # Correct position
            other = None if type(node2) == Rect else node2

            if newRect.width < newRect.height:
                if newRect.right > node1.getBounds().centerx: # collider to the right
                    node1.translate((-newRect.width, 0))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Right, newRect.center, other))
                elif newRect.left < node1.getBounds().centerx: # collider to the left
                    node1.translate((newRect.width, 0))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Left, newRect.center, other))
            else:
                if newRect.bottom > node1.getBounds().centery: # collider to the bottom
                    node1.translate((0, -newRect.height))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Bottom, newRect.center, other))
                elif newRect.top < node1.getBounds().centery: # collider to the up
                    node1.translate((0, newRect.height))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Top, newRect.center, other))

    def run_checks(rootNode):
        """
        Called once per frame, checks the scene graph for collisions between scene nodes and startic colliders.

        Keyword arguments:
        rootNode -- The root scene node of the scene graph.
        """
        for node1 in rootNode.get_all_children():
            if node1.getBounds().width > 0 or node1.getBounds().height > 0:
                for node2 in rootNode.get_all_children():
                    if node2.getBounds().width > 0 or node2.getBounds().height > 0:
                        if node1 is not node2:
                            if node1.getBounds().colliderect(node2.getBounds()):
                                # There is a collision
                                PhysicsManager.handle_collision(node1, node2)
                for wall in PhysicsManager.colliders:
                    if node1.getBounds().colliderect(wall):
                        # There is a collision
                        PhysicsManager.handle_collision(node1, wall)
