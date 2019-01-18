"""
This module contains classes for use within the physics system.
"""

from enum import Enum
import pygame
from pygame.locals import Rect
from engine.scenenode import NodeType


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
    def __init__(self, colDir, center_pos, other_node=None):
        """
        Constructor for this class.

        Keyword arguments:
        colDir -- The CollisionDirection of the described collision.
        center_pos -- The center position of the Collision.4
        other_node -- The other node affected by this collision, may not exist. (default = None)
        """
        self.direction = colDir
        self.position = center_pos
        self.other_node = other_node

    def __str__(self):
        """
        returns the string representation of this class.
        """
        return "Direction: {0}, centerposition: {1}, against: {2}".format(self.direction,
                                                                          self.position,
                                                                          self.other_node)

class PhysicsManager:
    """
    Manager class for physics calculations and representations.
    """
    @staticmethod
    def add_collider(rectangle):
        """
        Adds a static rectangle collider to the scene.

        Keyword arguments:
        rectangle -- The Rect to add to the scene.
        """
        if PhysicsManager.colliders is None:
            PhysicsManager.colliders = []

        print("Adding Collider: {0}".format(rectangle))
        PhysicsManager.colliders += [rectangle]

    @staticmethod
    def remove_all_colliders():
        """
        Clears all static rectangle colliders from the scene.
        """
        PhysicsManager.colliders = []

    @staticmethod
    def draw_debug(size, root_node):
        """
        Draws all the colliders to the screen in transparent green.

        Keyword arguments:
        size -- The size of the surface to create and draw to.
        root_node -- The root scene node of the scene.

        Returns:
        A pygame surface with all colliders drawn to it.
        """
        surf = pygame.Surface(size)
        surf.set_alpha(128)
        for wall in PhysicsManager.colliders:
            pygame.draw.rect(surf, (0, 255, 0, 150), wall)

        for node1 in root_node.get_all_children():
            pygame.draw.rect(surf, (0, 255, 0, 150), node1.get_bounds())
        return surf

    @staticmethod
    def handle_collision(node1, node2):
        """
        Called upon finding a collision. Fixes the collisions, and tells the scenenodes to \
        handle_collision.

        Keyword arguments:
        node1 -- The primary node of the collision, will be the one reacting to the collision
        node2 -- The secondary node of the collision, or a Rect object of a static coliider.
        """
        if not isinstance(node2, Rect):
            node2 = node2.get_bounds
        new_rect = node1.get_bounds().clip(node2)

        if node1.node_type == NodeType.Dynamic:
            # Correct position
            other = None if isinstance(node2, Rect) else node2

            if new_rect.width < new_rect.height:
                if new_rect.right > node1.get_bounds().centerx: # collider to the right
                    node1.translate((-new_rect.width, 0))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Right,
                                                                new_rect.center, other))
                elif new_rect.left < node1.get_bounds().centerx: # collider to the left
                    node1.translate((new_rect.width, 0))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Left,
                                                                new_rect.center, other))
            else:
                if new_rect.bottom > node1.get_bounds().centery: # collider to the bottom
                    node1.translate((0, -new_rect.height))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Bottom,
                                                                new_rect.center, other))
                elif new_rect.top < node1.get_bounds().centery: # collider to the up
                    node1.translate((0, new_rect.height))
                    node1.handle_collision(CollisionInformation(CollisionDirection.Top,
                                                                new_rect.center, other))

    @staticmethod
    def run_checks(root_node):
        """
        Called once per frame, checks the scene graph for collisions between scene nodes and \
        static colliders.

        Keyword arguments:
        root_node -- The root scene node of the scene graph.
        """
        for node1 in root_node.get_all_children():
            if node1.get_bounds().width > 0 or node1.get_bounds().height > 0:
                for node2 in root_node.get_all_children():
                    if node2.get_bounds().width > 0 or node2.get_bounds().height > 0:
                        if node1 is not node2:
                            if node1.get_bounds().colliderect(node2.get_bounds()):
                                # There is a collision
                                PhysicsManager.handle_collision(node1, node2)
                for wall in PhysicsManager.colliders:
                    if node1.get_bounds().colliderect(wall):
                        # There is a collision
                        PhysicsManager.handle_collision(node1, wall)
