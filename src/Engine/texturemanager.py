import pygame
from pygame.locals import *
from src.engine.utility import Event


class TextureManager:
    """
    This manager loads, and assigns IDs to textures, and manages the animations for them.
    """
    textures = {}

    def load_texture(id, filename, size=None, pos=(0,0), numFrames=1):
        """
        Loads a texture from a file, and assigns it a unique TextureID, and possibly other data such as the source rectangle to use.

        Keyword arguments:
        id -- The ID to assign to this texure.
        filename -- The file location to load the texture from.
        size -- The size of this texture's source frame. (default = None)
        pos -- The position of this texture's position. (default = (0, 0))
        numFrame -- The number of frames in this animation strip. (default = 1)

        Raises:
        TextureExistsError -- When id is already in use.
        """
        if id not in TextureManager.textures:
            image = pygame.image.load(filename)
            if size == None: size = image.get_size()
            tex = TextureManager.textures[id] = TextureInfo(image, numFrames, Rect(pos, size))
            print("Loaded texture {0} from {1}".format(id, filename))
        else:
            raise TextureExistsError

    def get_texture_info(id):
        """
        Fetches the TexureInfo for the Texture with ID id.
        
        Keyword arguments:
        id -- The ID of the Texture.
        """
        if id in TextureManager.textures:
            tex_info = TextureManager.textures[id]
            return tex_info
        else:
            raise TextureDoesntExistError

    def get_texture(id):
        """
        Fetches the texture associated with this id.
        
        Keyword arguments:
        id -- The ID of the Texture.
        """
        if id in TextureManager.textures:
            tex_info = TextureManager.textures[id]
            return tex_info.fetch().subsurface(tex_info.get_src_rect())
        else:
            raise TextureDoesntExistError

    def next_frame():
        """
        Updates every animation to the next frame.
        """
        for id in TextureManager.textures:
            if TextureManager.textures[id].frames > 1:
                TextureManager.textures[id].next_frame()

class TextureInfo:
    """
    Class Describing a Texture, it's source rectangle and animation frames.
    """
    def __init__(self, tex, f=1, sRect=None):
        """
        Creates this object, and calculates required values. Also creates an anim_finished_event, which can be subscribed to and is called each time the animation loops.

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
        return Rect(self.frame_1+(self.current_frame*self.src_rect.width), self.src_rect.y, self.src_rect.width, self.src_rect.height)

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
