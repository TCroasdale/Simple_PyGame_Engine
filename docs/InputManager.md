# InputManager 
 ```
 InputManager is the class responsible for registering, and keeping current inputs up to date. 
```
## assign_control(id, key) 

  

 > Assigns an ID to a pygame keycode, and registers it.

 > 

 > Keyword arguments:

 > id -- The ID to assign the keycode to.

 > key -- The keycode to assign 

## get_control(id) 

  

 > Returns whether a control by the name of id is currently down.

 > 

 > Keyword arguments:

 > id -- The ID assigned to the control. 

## get_control_pressed(id) 

  

 > Returns whether a control by the name of id got pressed down this frame.

 > 

 > Keyword arguments:

 > id -- The ID assigned to the control. 

## get_control_released(id) 

  

 > Returns whether a control by the name of id got released down this frame.

 > 

 > Keyword arguments:

 > id -- The ID assigned to the control. 

## setup() 

  

 > setup should be called when the game starts up, it creates empty dictionaries for the the controls. 

## update(events) 

  

 > Updates the current values for controls that ahve been registered.

 > 

 > Keyword arguments:

 > events -- The events list received from pygame.event.get() 

