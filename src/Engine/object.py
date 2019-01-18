from src.engine.texturemanager import *

class Object:
    """
    An Object in the scene representing by a texture. An object can be attached to a scene node.
    """
    def __init__(self, scenenode=None):
        """
        Constructor for an object class.

        Keyword arguments:
        scenenode -- The scene node which this object is attached to. (default = None)
        """
        self.textureID = 'steve'
        self.size = (32, 32)
        self.node = scenenode

    def setTextureID(self, id):
        """
        Sets the textureID for this object.

        Keyword arguments:
        id -- The TextureID stored in TextureManager
        """
        self.textureID = id

    def setSize(self, size):
        """
        Sets the size of this object

        Keyword arguments:
        size -- A Tuple of Width and Height (w, h)
        """
        self.size = size

    def setSceneNode(self, node):
        """
        Sets the scenenode which this object is attached to, should never really be called except for by the scene node which it is attached to.

        Keyword arguments:
        node -- The node which this object is now attached to.
        """
        self.node = node

    def update(self, delta):
        """
        Blank function, Override this when creating a new object. Should contain most game logic for an object, called once per frame.

        Keyword arguments:
        delta -- The elapsed time since the last update call.
        """
        return

    def handle_collision(self, collision_data):
        """
        Blank function, Override this when creating a new object. Called when this object is in a collision.

        Keyword arguments:
        collision_data -- The CollisionInformation object describing the collision.
        """
        return

    def move(self, amount):
        """
        Tells node to move by amount

        Keyword arguments:
        amount -- (tx, ty) How much to translate by.
        """
        self.node.translate(amount)

    def switch_texture(self, newTexture):
        """
        Changes the texture id, and resets the new textures animation. It is better practise to use this than changing textureID or setTextureID()

        Keyword arguments:
        newTexture -- The TextureID to switch to.
        """
        if self.textureID == newTexture:
            return
        TextureManager.get_texture_info(newTexture).reset_anim()
        self.textureID = newTexture
