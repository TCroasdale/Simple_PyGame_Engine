import pygame
from pygame.locals import *

class InputManager:
    """
    InputManager is the class responsible for registering, and keeping current inputs up to date.
    """

    def setup():
        """
        setup should be called when the game starts up, it creates empty dictionaries for the the controls.
        """
        InputManager.controls = {}
        InputManager.old_control_values = {}
        InputManager.control_values = {}


    def get_control(id):
        """
        Returns whether a control by the name of id is currently down.

        Keyword arguments:
        id -- The ID assigned to the control.

        Raises:
        ControlDoesntExistException -- When id has not been assigned to a control.
        """
        if id in InputManager.controls:
            key = InputManager.controls[id]
            if key in InputManager.control_values:
                return InputManager.control_values[key] == 1
            return False
        raise ControlDoesntExistException

    def get_control_pressed(id):
        """
        Returns whether a control by the name of id got pressed down this frame.

        Keyword arguments:
        id -- The ID assigned to the control.
        
        Raises:
        ControlDoesntExistException -- When id has not been assigned to a control.
        """
        if id in InputManager.controls:
            key = InputManager.controls[id]
            if key in InputManager.control_values and key in InputManager.old_control_values:
                return InputManager.control_values[key] == 1 and InputManager.old_control_values[key] == 0
            return False
        raise ControlDoesntExistException

    def get_control_released(id):
        """
        Returns whether a control by the name of id got released down this frame.

        Keyword arguments:
        id -- The ID assigned to the control.
        
        Raises:
        ControlDoesntExistException -- When id has not been assigned to a control.
        """
        if id in InputManager.controls:
            key = InputManager.controls[id]
            if key in InputManager.control_values and key in InputManager.old_control_values:
                return InputManager.control_values[key] == 0 and InputManager.old_control_values[key] == 1
            return False
        raise ControlDoesntExistException


    def update(events):
        """
        Updates the current values for controls that ahve been registered.

        Keyword arguments:
        events -- The events list received from pygame.event.get()
        """
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
        """
        Assigns an ID to a pygame keycode, and registers it.

        Keyword arguments:
        id -- The ID to assign the keycode to.
        key -- The keycode to assign

        Raises:
        ControlExistsExeception -- When id has already been assigned to a control.
        """
        if id not in InputManager.controls:
            print("Assigning key {0} to id: {1}".format(pygame.key.name(key), id))
            InputManager.controls[id] = key
        else:
            raise ControlExistsException


class ControlExistsException(Exception):
    """
    Raised when a trying to register a keycode to an ID that already exists.
    """
    pass

class ControlDoesntExistException(Exception):
    """
    Raised when a trying to find a control with an ID that doesn't exist.
    """
    pass
