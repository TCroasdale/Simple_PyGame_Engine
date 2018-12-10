import pygame
from pygame.locals import *
from Engine.scenenode import *

class PhysicsManager:
    def add_collider(rectangle):
        if PhysicsManager.colliders == None:
            PhysicsManager.colliders = []

        print("Adding Collider: {0}".format(rectangle))
        PhysicsManager.colliders += [rectangle]

    def remove_all_colliders():
        PhysicsManager.colliders = []

    def draw_debug(screen, rootNode):
        for wall in PhysicsManager.colliders:
            pygame.draw.rect(screen, (0, 255, 0), wall)

        for node1 in rootNode.get_all_children():
            pygame.draw.rect(screen, (0, 255, 0), node1.getBounds())

    def handle_collision(node1, node2bounds):
        newRect = node1.getBounds().clip(node2bounds)
        if node1.nodeType == NodeType.Dynamic:
            print("collision! between {0} and{1}".format(node1.getBounds(), node2bounds))
            # Correct position
            print(newRect)
            if newRect.centerx > node1.getBounds().centerx: # collider to the right
                print("moving by{0}".format((newRect.width, 0)))
                node1.translate((-newRect.width, 0))
            elif newRect.centerx < node1.getBounds().centerx: # collider to the left
                print("moving by{0}".format((newRect.width, 0)))
                node1.translate((newRect.width, 0))

            if newRect.centery > node1.getBounds().centery: # collider to the bottom
                print("moving by{0}".format((-newRect.height, 0)))
                node1.translate((0, -newRect.height))
            elif newRect.centery < node1.getBounds().centery: # collider to the up
                print("moving by{0}".format((newRect.height, 0)))
                node1.translate((0, newRect.height))

    def run_checks(rootNode):
        for node1 in rootNode.get_all_children():
            if node1.getBounds().width > 0 or node1.getBounds().height > 0:
                for node2 in rootNode.get_all_children():
                    if node2.getBounds().width > 0 or node2.getBounds().height > 0:
                        if node1 is not node2:
                            if node1.getBounds().colliderect(node2.getBounds()):
                                # There is a collision
                                PhysicsManager.handle_collision(node1, node2.getBounds())
                for wall in PhysicsManager.colliders:
                    if node1.getBounds().colliderect(wall):
                        # There is a collision
                        PhysicsManager.handle_collision(node1, wall)
