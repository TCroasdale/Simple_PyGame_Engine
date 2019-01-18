# TextureManager 
  This manager loads, and assigns IDs to textures, and manages the animations for them. 

## Methods: 
* [get_texture(id)](#get_texture) 
* [get_texture_info(id)](#get_texture_info) 
* [load_texture(id, filename, size=None, pos=(0, 0), numFrames=1)](#load_texture) 
* [next_frame()](#next_frame) 
<div id="get_texture"></div>

## get_texture(id) 

  

 > Fetches the texture associated with this id.

 

 **Keyword arguments:**

 id -- The ID of the Texture. 

 --- 
<div id="get_texture_info"></div>

## get_texture_info(id) 

  

 > Fetches the TexureInfo for the Texture with ID id.

 

 **Keyword arguments:**

 id -- The ID of the Texture. 

 --- 
<div id="load_texture"></div>

## load_texture(id, filename, size=None, pos=(0, 0), numFrames=1) 

  

 > Loads a texture from a file, and assigns it a unique TextureID, and possibly other data such as the source rectangle to use.

 

 **Keyword arguments:**

 id -- The ID to assign to this texure.

 filename -- The file location to load the texture from.

 size -- The size of this texture's source frame. (default = None)

 pos -- The position of this texture's position. (default = (0, 0))

 numFrame -- The number of frames in this animation strip. (default = 1)

 

 **Raises:**

 TextureExistsError -- When id is already in use. 

 --- 
<div id="next_frame"></div>

## next_frame() 

  

 > Updates every animation to the next frame. 

 --- 
