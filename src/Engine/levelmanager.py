import pygame
from pygame.locals import *

from Engine.texturemanager import *
from Engine.physicsmanager import *
import xml.etree.ElementTree as ET
import csv
import math

# Class to represent a single tile
class Tile:
    def __init__(self, id, position):
        self.tileID = id
        self.position = position

    def __str__(self):
        return "tile: id: {0}, position: {1}".format(self.tileID, self.position)

# Class to represent a layer of tiles
class Layer:
    def __init__(self, name, tX, tY, tiles=[], tileset=None):
        self.name = name
        self.gridsize = (int(tX), int(tY))
        self.tiles=tiles
        self.tileset=tileset

    def __str__(self):
        tiles = []
        for tile in self.tiles:
            tiles += [str(tile)]
        return "layer: name: {0}, gridsize: {1}, {2}, tiles: {3}, tileset{4}".format(self.name, self.gridsize[0], self.gridsize[1], tiles, self.tileset)

# Class to represent (and load) a tile set image
class Tileset:
    def __init__(self, id, locale, tX, tY):
        self.name = id
        self.path = locale
        self.gridsize = (int(tX), int(tY))
        locale = locale.split('../')[1]
        TextureManager.load_texture(id, locale)

    def __str__(self):
        return "tileset: id: {0}, locale: {1}, tx: {2}, ty: {3}".format(self.name, self.path, self.gridsize[0], self.gridsize[1])   



class LevelManager:

    # Returns the BackgroundColor defined in the oep file
    def get_fill_colour():
        return LevelManager.colour

    # Draws every tile to the screen
    def render_level(screen, foreground=False):
        if LevelManager.isLevelLoaded: #If the level isn't loaded, don't render
            layers = LevelManager.fg_layers if foreground else LevelManager.bg_layers
            for layerdef in layers: # Draw Every layer
                if layerdef.tileset != None: # Don't try to draw it if there is no tileset attached
                    texture = TextureManager.get_texture(layerdef.tileset.name) # Fetch the tile set texture
                    # Get the number of tiles perrow in the tileset
                    ts_w = texture.get_width()  / layerdef.tileset.gridsize[0]
                    for tile in layerdef.tiles: # For every tile in this layer
                        # Find it's position in the texture
                        srcX = (tile.tileID % ts_w) * layerdef.tileset.gridsize[0]
                        srcY = math.floor(tile.tileID / ts_w) * layerdef.tileset.gridsize[1]
                        srcRect = Rect(srcX, srcY, layerdef.tileset.gridsize[0], layerdef.tileset.gridsize[1])
                        # Put it on the screen
                        screen.blit(texture, tile.position, srcRect)



    def load_level(levelname):
        PhysicsManager.remove_all_colliders()
        tree = ET.parse('levels/{0}.oel'.format(levelname))
        root = tree.getroot()
        level_width = int(root.get('width'))
        level_height = int(root.get('height'))

        LevelManager.level_data = {}
        for layerdef in LevelManager.bg_layers + LevelManager.fg_layers:
            leveldata = root.find(layerdef.name)
            if leveldata.get('exportMode') == 'Rectangles':
                for rect in leveldata.findall("rect"):
                    x = int(rect.get('x'))
                    y = int(rect.get('y'))
                    w = int(rect.get('w'))
                    h = int(rect.get('h'))
                    PhysicsManager.add_collider(Rect(x, y, w, h))
            elif leveldata.get('exportMode') == 'CSV':
                layerdef.tileset = LevelManager.tilesets[leveldata.get('tileset')]
                rows = [x for x in leveldata.text.split('\n')]
                tiles = []
                y = 0
                for row in rows:
                    x = 0
                    tile_ids = [int(t) for t in row.split(',')]
                    for tile in tile_ids:
                        if int(tile) >= 0:
                            tiles += [Tile(tile, (x, y))]
                        x += layerdef.gridsize[0]
                    y += layerdef.gridsize[1]

                layerdef.tiles = tiles

        print("Loaded Level {0}".format(levelname))
        LevelManager.isLevelLoaded = True


    def setup():
        LevelManager.isLevelLoaded = False
        tree = ET.parse('levels/ogmo.oep')
        root = tree.getroot()

        # Load BackgroundColor
        bgColour = root.find('BackgroundColor')
        r = int(bgColour.get('R'))
        g = int(bgColour.get('G'))
        b = int(bgColour.get('B'))
        a = int(bgColour.get('A'))
        LevelManager.colour = Color(r, g, b, a)

        LevelManager.fg_layers = []
        LevelManager.bg_layers = []
        #Load all layer definitions
        for layer_def in root.find('LayerDefinitions'):
            layer_name = layer_def.find('Name').text
            layer_grid = layer_def.find('Grid')
            layer_tx = layer_grid.find('Width').text
            layer_ty = layer_grid.find('Height').text
            if layer_name[:2] == "fg":
                LevelManager.fg_layers += [Layer(layer_name, layer_tx, layer_ty)]
            else:
                LevelManager.bg_layers += [Layer(layer_name, layer_tx, layer_ty)]


        #Load all texture sheets
        LevelManager.tilesets = {}
        for tileset in root.find('Tilesets'):
            set_name = tileset.find('Name').text
            set_file = tileset.find('FilePath').text.replace('\\', '/')
            tile_size = tileset.find('TileSize')
            tile_tx = tile_size.find('Width').text
            tile_ty = tile_size.find('Height').text
            LevelManager.tilesets[set_name] = Tileset(set_name, set_file, tile_tx, tile_ty)
