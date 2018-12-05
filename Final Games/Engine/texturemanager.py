import pygame
from pygame.locals import *

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

    def get_src_rect(self):
        return self.src_rect

    def next_frame(self):
        if self.current_frame+1 == self.frames:
            self.src_rect = Rect(0, self.src_rect.y, self.src_rect.width, self.src_rect.height)
            self.current_frame = 0
        else:
            self.src_rect = self.src_rect.move(self.src_rect.width, 0)
            self.current_frame += 1

    def fetch(self):
        return self.texture

class TextureExistsError(Exception):
    pass

class TextureDoesntExistError(Exception):
    pass
