import pygame
from pygame.locals import *

class InputManager:
    """
    InputManager is the class responsible for registering, and keeping current inputs up to date.
    """

    def setup():
        """
        
        """
        InputManager.controls = {}
        InputManager.old_control_values = {}
        InputManager.control_values = {}


    def get_control(id):
        if id in InputManager.controls:
            key = InputManager.controls[id]
            if key in InputManager.control_values:
                return InputManager.control_values[key] == 1
            return False
        raise ControlDoesntExistException

    def get_control_pressed(id):
        if id in InputManager.controls:
            key = InputManager.controls[id]
            if key in InputManager.control_values and key in InputManager.old_control_values:
                return InputManager.control_values[key] == 1 and InputManager.old_control_values[key] == 0
            return False
        raise ControlDoesntExistException

    def get_control_released(id):
        if id in InputManager.controls:
            key = InputManager.controls[id]
            if key in InputManager.control_values and key in InputManager.old_control_values:
                return InputManager.control_values[key] == 0 and InputManager.old_control_values[key] == 1
            return False
        raise ControlDoesntExistException


    def update(events):
        InputManager.old_control_values = InputManager.control_values
        InputManager.control_values = {}
        for e in events:
            if e.type == pygame.KEYDOWN:
                InputManager.control_values[e.key] = 1
            elif e.type == pygame.KEYUP:
                InputManager.control_values[e.key] = 0

        for key in InputManager.old_control_values:
            if key not in InputManager.control_values:
                InputManager.control_values[key] = InputManager.old_control_values[key]

    def assign_control(id, key):
        if id not in InputManager.controls:
            print("Assigning key {0} to id: {1}".format(pygame.key.name(key), id))
            InputManager.controls[id] = key
        else:
            raise ControlExistsException


class ControlExistsException(Exception):
    pass

class ControlDoesntExistException(Exception):
    pass
