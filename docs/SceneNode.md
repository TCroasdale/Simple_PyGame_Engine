# SceneNode 
 ```
 A Scene node which will be added to the scene graph. Can have an associated object attached to it. 
```
## Methods: 
* [Constructor(self, parent=None, object=None, type=<NodeType.Dynamic: 0>)](#Constructor) 
* [addChild(self, node)](#addChild) 
* [attachObject(self, obj)](#attachObject) 
* [getBounds(self)](#getBounds) 
* [getWorldPosition(self)](#getWorldPosition) 
* [handle_collision(self, coll_data)](#handle_collision) 
* [translate(self, amount)](#translate) 
* [update(self, delta)](#update) 
<div id="Constructor"></div>## Constructor(self, parent=None, object=None, type=<NodeType.Dynamic: 0>) 

  

 > Creates a Scene Node.

 

 **Keyword arguments:**

 parent -- The parent Scene Node of this Node. (default = None)

 object -- The object which will be attached to this object. (default = None)

 type -- The NodeType of this Node (default = NodeType.Dynamic) 

 --- 
<div id="addChild"></div>## addChild(self, node) 

  

 > Adds a child node to the children of this node.

 

 **Keyword arguments:**

 node -- The node to become a child of this 

 --- 
<div id="attachObject"></div>## attachObject(self, obj) 

  

 > Attaches an object to this node.

 

 **Keyword arguments:**

 obj -- The Object to attach to this node. 

 --- 
<div id="getBounds"></div>## getBounds(self) 

  

 > returns a Rectangle containing the attached object.

 

 **Returns:**

 a Rect containing the world position and size of this node. 

 --- 
<div id="getWorldPosition"></div>## getWorldPosition(self) 

  

 > Returns the position of this node, relative to the world.

 

 **Returns:**

 A Tuple (x, y) representing the position of this node. 

 --- 
<div id="handle_collision"></div>## handle_collision(self, coll_data) 

  

 > Called when this node is in a collision

 

 **Keyword arguments:**

 coll_data -- The CollisionInformation Object describing the collision. 

 --- 
<div id="translate"></div>## translate(self, amount) 

  

 > Moves this node by amount.

 

 **Keyword arguments:**

 amount -- (tx, ty) How much to move this node by. 

 --- 
<div id="update"></div>## update(self, delta) 

  

 > Updates the attached object and calls update() on the children of this node.

 

 **Keyword arguments:**

 delta -- The time elapsed since update() was last called. 

 --- 
