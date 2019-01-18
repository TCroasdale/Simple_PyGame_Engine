# Object 
  An Object in the scene representing by a texture. An object can be attached to a scene node. 

## Methods: 
* [Constructor(self, scenenode=None)](#Constructor) 
* [handle_collision(self, collision_data)](#handle_collision) 
* [move(self, amount)](#move) 
* [setSceneNode(self, node)](#setSceneNode) 
* [setSize(self, size)](#setSize) 
* [setTextureID(self, id)](#setTextureID) 
* [switch_texture(self, newTexture)](#switch_texture) 
* [update(self, delta)](#update) 
<div id="Constructor"></div>

## Constructor(self, scenenode=None) 

  

 > Constructor for an object class.

 

 **Keyword arguments:**

 scenenode -- The scene node which this object is attached to. (default = None) 

 --- 
<div id="handle_collision"></div>

## handle_collision(self, collision_data) 

  

 > Blank function, Override this when creating a new object. Called when this object is in a collision.

 

 **Keyword arguments:**

 collision_data -- The CollisionInformation object describing the collision. 

 --- 
<div id="move"></div>

## move(self, amount) 

  

 > Tells node to move by amount

 

 **Keyword arguments:**

 amount -- (tx, ty) How much to translate by. 

 --- 
<div id="setSceneNode"></div>

## setSceneNode(self, node) 

  

 > Sets the scenenode which this object is attached to, should never really be called except for by the scene node which it is attached to.

 

 **Keyword arguments:**

 node -- The node which this object is now attached to. 

 --- 
<div id="setSize"></div>

## setSize(self, size) 

  

 > Sets the size of this object

 

 **Keyword arguments:**

 size -- A Tuple of Width and Height (w, h) 

 --- 
<div id="setTextureID"></div>

## setTextureID(self, id) 

  

 > Sets the textureID for this object.

 

 **Keyword arguments:**

 id -- The TextureID stored in TextureManager 

 --- 
<div id="switch_texture"></div>

## switch_texture(self, newTexture) 

  

 > Changes the texture id, and resets the new textures animation. It is better practise to use this than changing textureID or setTextureID()

 

 **Keyword arguments:**

 newTexture -- The TextureID to switch to. 

 --- 
<div id="update"></div>

## update(self, delta) 

  

 > Blank function, Override this when creating a new object. Should contain most game logic for an object, called once per frame.

 

 **Keyword arguments:**

 delta -- The elapsed time since the last update call. 

 --- 
