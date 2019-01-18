# Game 
  This class represents and runs the full Game 

## Methods: 
* [Constructor(self)](#Constructor) 
* [create_scene(self)](#create_scene) 
* [quit(self)](#quit) 
* [render(self)](#render) 
* [setup(self)](#setup) 
* [start_game(gameclass)](#start_game) 
* [update(self)](#update) 
* [updateTime(self)](#updateTime) 
<div id="Constructor"></div>

## Constructor(self) 

  

 > Sets all values for the game, will eventaully read from a config.py 

 --- 
<div id="create_scene"></div>

## create_scene(self) 

  

 > Create The initial scene, should be overriden and create whatever objects your game needs. 

 --- 
<div id="quit"></div>

## quit(self) 

  

 > Ends the game after this frame is completed 

 --- 
<div id="render"></div>

## render(self) 

  

 > Called once per frames, draws all objects to the screen, and all level tiles 

 --- 
<div id="setup"></div>

## setup(self) 

  

 > Called at startup to create the screen, load textures, assign controls and create a rootSceneNode 

 --- 
<div id="start_game"></div>

## start_game(gameclass) 

  

 > Initialises the game, setups all all Manager classes, creates the scene and then runs the game loop 

 --- 
<div id="update"></div>

## update(self) 

  

 > Called once per frame, updates all animations scenenodes (and attached objects) and then runs physics checks 

 --- 
<div id="updateTime"></div>

## updateTime(self) 

  

 > Called once per frame, to set the values for lastElapsed and lastTime variables 

 --- 
