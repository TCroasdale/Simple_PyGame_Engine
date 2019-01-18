# TextureInfo 
  Class Describing a Texture, it's source rectangle and animation frames. 

## Methods: 
* [Constructor(self, tex, f=1, sRect=None)](#Constructor) 
* [fetch(self)](#fetch) 
* [get_anim_event(self)](#get_anim_event) 
* [get_src_rect(self)](#get_src_rect) 
* [next_frame(self)](#next_frame) 
* [reset_anim(self)](#reset_anim) 
<div id="Constructor"></div>

## Constructor(self, tex, f=1, sRect=None) 

  

 > Creates this object, and calculates required values. Also creates an anim_finished_event, which can be subscribed to and is called each time the animation loops.

 

 **Keyword arguments:**

 tex -- The image data of this texture.

 f -- The number of frames of animation this texture has. (default = 1)

 sRect -- The source rectangle on the image of this Texture. (default = None) 

 --- 
<div id="fetch"></div>

## fetch(self) 

  

 > Fetches the image data for this texture. 

 --- 
<div id="get_anim_event"></div>

## get_anim_event(self) 

  

 > Fetches enim_finished_event so that it can be subscribed to. 

 --- 
<div id="get_src_rect"></div>

## get_src_rect(self) 

  

 > Fetches the current source Rect of this texture. 

 --- 
<div id="next_frame"></div>

## next_frame(self) 

  

 > Updates the current frame of animation. 

 --- 
<div id="reset_anim"></div>

## reset_anim(self) 

  

 > Resets the animation, of this texture. 

 --- 
