# LevelManager 
 ```
 This class manages loading and reading level files. 
```
## Methods: * [get_fill_colour()](/#get_fill_colour) 
* [load_level(levelname)](/#load_levellevelname) 
* [render_level(screen-foreground=False)](/#render_levelscreen-foreground=False) 
* [setup()](/#setup) 
## get_fill_colour() 

  

 > Returns the fill colour specified in the level file. 

## load_level(levelname) 

  

 > Loads an OGMO level from the levels direction into memory, 

 

 **Keyword arguments:**

 levelname -- The file name of the OGMO level, exluding the directory and .oel extension. 

## render_level(screen, foreground=False) 

  

 > Draws all tiles loaded in memer to the screen provided.

 

 **Keyword arguments:**

 screen -- The pygame screen to blit the images to.

 foreground -- Whether to draw foregroudn layers or not. (default = False) 

## setup() 

  

 > Setups the LevelManager and reads in the level project data, such as all layers and background colour. 

--- 