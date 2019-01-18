"""
The module holds classes for use in the texture loading system.
"""

import pygame
from pygame.locals import Rect
from engine.utility import Event


class TextureManager:
    """
    This manager loads, and assigns IDs to textures, and manages the animations for them.
    """
    textures = {}

    @staticmethod
    def load_texture(tex_id, filename, size=None, pos=(0, 0), num_frames=1):
        """
        Loads a texture from a file, and assigns it a unique TextureID, and possibly other data \
        such as the source rectangle to use.

        Keyword arguments:
        tex_id -- The ID to assign to this texure.
        filename -- The file location to load the texture from.
        size -- The size of this texture's source frame. (default = None)
        pos -- The position of this texture's position. (default = (0, 0))
        numFrame -- The number of frames in this animation strip. (default = 1)

        Returns:
        The TextureInfo object which has been loaded.

        Raises:
        TextureExistsError -- When id is already in use.
        """
        if tex_id not in TextureManager.textures:
            image = pygame.image.load(filename)
            if size is None:
                size = image.get_size()
            tex = TextureManager.textures[tex_id] = TextureInfo(image, num_frames, Rect(pos, size))
            print("Loaded texture {0} from {1}".format(tex_id, filename))
            return tex
        else:
            raise TextureExistsError

    @staticmethod
    def get_texture_info(tex_id):
        """
        Fetches the TexureInfo for the Texture with ID tex_id.

        Keyword arguments:
        tex_id -- The ID of the Texture.
        """
        if tex_id in TextureManager.textures:
            tex_info = TextureManager.textures[tex_id]
            return tex_info
        else:
            raise TextureDoesntExistError

    @staticmethod
    def get_texture(tex_id):
        """
        Fetches the texture associated with this id.

        Keyword arguments:
        tex_id -- The ID of the Texture.
        """
        if tex_id in TextureManager.textures:
            tex_info = TextureManager.textures[tex_id]
            return tex_info.fetch().subsurface(tex_info.get_src_rect())
        else:
            raise TextureDoesntExistError

    @staticmethod
    def next_frame():
        """
        Updates every animation to the next frame.
        """
        for tex_id in TextureManager.textures:
            if TextureManager.textures[tex_id].frames > 1:
                TextureManager.textures[tex_id].next_frame()

class TextureInfo:
    """
    Class Describing a Texture, it's source rectangle and animation frames.
    """
    def __init__(self, tex, f=1, sRect=None):
        """
        Creates this object, and calculates required values. Also creates an anim_finished_event, \
        which can be subscribed to and is called each time the animation loops.

        Keyword arguments:
        tex -- The image data of this texture.
        f -- The number of frames of animation this texture has. (default = 1)
        sRect -- The source rectangle on the image of this Texture. (default = None)

        """
        self.texture = tex
        self.frames = f
        self.current_frame = 0
        self.src_rect = sRect
        self.frame_1 = sRect.x
        self.anim_finished_event = Event()

    def get_anim_event(self):
        """
        Fetches enim_finished_event so that it can be subscribed to.
        """
        return self.anim_finished_event

    def get_src_rect(self):
        """
        Fetches the current source Rect of this texture.
        """
        pos_x = self.frame_1+(self.current_frame*self.src_rect.width)
        pos_y = self.src_rect.y
        width = self.src_rect.width
        height = self.src_rect.height
        return Rect(pos_x, pos_y, width, height)

    def reset_anim(self):
        """
        Resets the animation, of this texture.
        """
        self.current_frame = 0

    def next_frame(self):
        """
        Updates the current frame of animation.
        """
        if self.current_frame+1 == self.frames:
            self.current_frame = 0
            self.anim_finished_event()
        else:
            self.current_frame += 1

    def fetch(self):
        """
        Fetches the image data for this texture.
        """
        return self.texture

class TextureExistsError(Exception):
    """
    Raised when a TextureID is already in use.
    """
    pass

class TextureDoesntExistError(Exception):
    """
    Raised when a TextureID does not exist.
    """
    pass
