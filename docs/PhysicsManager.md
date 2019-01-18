# PhysicsManager 
 ```
 Manager class for physics calculations and representations. 
```
## Methods: 
* [add_collider(rectangle)](#add_collider) 
* [draw_debug(size, rootNode)](#draw_debug) 
* [handle_collision(node1, node2)](#handle_collision) 
* [remove_all_colliders()](#remove_all_colliders) 
* [run_checks(rootNode)](#run_checks) 
<div id="add_collider"></div>## add_collider(rectangle) 

  

 > Adds a static rectangle collider to the scene.

 

 **Keyword arguments:**

 rectangle -- The Rect to add to the scene. 

 --- 
<div id="draw_debug"></div>## draw_debug(size, rootNode) 

  

 > Draws all the colliders to the screen in transparent green.

 

 **Keyword arguments:**

 size -- The size of the surface to create and draw to.

 rootNode -- The root scene node of the scene.

 

 **Returns:**

 A pygame surface with all colliders drawn to it. 

 --- 
<div id="handle_collision"></div>## handle_collision(node1, node2) 

  

 > Called upon finding a collision. Fixes the collisions, and tells the scenenodes to handle_collision.

 

 **Keyword arguments:**

 node1 -- The primary node of the collision, will be the one reacting to the collision

 node2 -- The secondary node of the collision, or a Rect object of a static coliider. 

 --- 
<div id="remove_all_colliders"></div>## remove_all_colliders() 

  

 > Clears all static rectangle colliders from the scene. 

 --- 
<div id="run_checks"></div>## run_checks(rootNode) 

  

 > Called once per frame, checks the scene graph for collisions between scene nodes and startic colliders.

 

 **Keyword arguments:**

 rootNode -- The root scene node of the scene graph. 

 --- 
