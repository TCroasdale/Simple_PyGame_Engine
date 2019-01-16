import pygame
from pygame.locals import *
from Engine.utility import Event

class TextureManager:
    textures = {}

    def load_texture(id, filename, size=None, pos=(0,0), numFrames=1):
        if id not in TextureManager.textures:
            image = pygame.image.load(filename)
            if size == None: size = image.get_size()
            tex = TextureManager.textures[id] = TextureInfo(image, numFrames, Rect(pos, size))
            print("Loaded texture {0} from {1}".format(id, filename))
        else:
            raise TextureExistsError

    def get_texture_info(id):
        if id in TextureManager.textures:
            tex_info = TextureManager.textures[id]
            return tex_info
        else:
            raise TextureDoesntExistError

    def get_texture(id):
        if id in TextureManager.textures:
            tex_info = TextureManager.textures[id]
            return tex_info.fetch().subsurface(tex_info.get_src_rect())
        else:
            raise TextureDoesntExistError

    def next_frame():
        for id in TextureManager.textures:
            if TextureManager.textures[id].frames > 1:
                TextureManager.textures[id].next_frame()

class TextureInfo:
    def __init__(self, tex, f=1, sRect=None):
        self.texture = tex
        self.frames = f
        self.current_frame = 0
        self.src_rect = sRect
        self.frame_1 = sRect.x
        self.anim_finished_event = Event()

    def get_anim_event(self):
        return self.anim_finished_event

    def get_src_rect(self):
        return Rect(self.frame_1+(self.current_frame*self.src_rect.width), self.src_rect.y, self.src_rect.width, self.src_rect.height)

    def reset_anim(self):
        self.current_frame = 0

    def next_frame(self):
        if self.current_frame+1 == self.frames:
            self.current_frame = 0
            self.anim_finished_event()
        else:
            self.current_frame += 1

    def fetch(self):
        return self.texture

class TextureExistsError(Exception):
    pass

class TextureDoesntExistError(Exception):
    pass
