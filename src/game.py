import pygame
from pygame.locals import *

from src.engine.scenenode import *
from src.engine.texturemanager import *
from src.engine.inputmanager import *
from src.engine.object import *
from src.engine.levelmanager import *


class Game:
    """
    This class represents and runs the full Game
    """
    def __init__(self):
        """
        Sets all values for the game, will eventaully read from a config.py
        """
        self.screen_width = 640
        self.screen_height = 480
        self.running = True
        self.lastTime = pygame.time.get_ticks()/1000.0
        self.lastElapsed = 1/60.0
        self.animation_fps = 8
        self.animation_frame_time = 0.0

    
    def updateTime(self):
        """
        Called once per frame, to set the values for lastElapsed and lastTime variables
        """
        self.lastElapsed = pygame.time.get_ticks()/1000.0 - self.lastTime
        self.lastTime = pygame.time.get_ticks()/1000.0
        

    
    def setup(self):
        """
        Called at startup to create the screen, load textures, assign controls and create a rootSceneNode
        """
        size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(size)

        # Loading Textures
        # TextureManager.load_texture('steve', 'textures/steve.gif')
        TextureManager.load_texture('player_idle_right', 'textures/character.png', (32, 32), (0,32), 13)
        TextureManager.load_texture('player_idle_left', 'textures/character.png', (32, 32), (0,256), 13)

        TextureManager.load_texture('player_walk_down', 'textures/character.png', (16, 24), (0,0), 4)
        TextureManager.load_texture('player_walk_right', 'textures/character.png', (16, 24), (0,24), 4)
        TextureManager.load_texture('player_walk_up', 'textures/character.png', (16, 24), (0,48), 4)
        TextureManager.load_texture('player_walk_left', 'textures/character.png', (16, 24), (0,72), 4)
        
        TextureManager.load_texture('player_attack_down', 'textures/character.png', (16, 24), (0,96), 4)
        TextureManager.load_texture('player_attack_up', 'textures/character.png', (16, 24), (0,120), 4)
        TextureManager.load_texture('player_attack_right', 'textures/character.png', (16, 24), (0,144), 4)
        TextureManager.load_texture('player_attack_left', 'textures/character.png', (16, 24), (0,168), 4)

        TextureManager.load_texture('robot_blue_right', 'textures/robots.png', (32, 32), (0,0), 1)
        TextureManager.load_texture('robot_blue_left', 'textures/robots.png', (32, 32), (0,32), 1)
        TextureManager.load_texture('robot_green_right', 'textures/robots.png', (32, 32), (32,0), 1)
        TextureManager.load_texture('robot_green_left', 'textures/robots.png', (32, 32), (32,32), 1)
        TextureManager.load_texture('robot_red_right', 'textures/robots.png', (32, 32), (61,0), 1)
        TextureManager.load_texture('robot_red_left', 'textures/robots.png', (32, 32), (61,32), 1)
        

        # Setup controls
        InputManager.assign_control('move_up', pygame.K_UP)
        InputManager.assign_control('move_left', pygame.K_LEFT)
        InputManager.assign_control('move_right', pygame.K_RIGHT)
        InputManager.assign_control('jump', pygame.K_UP)
        InputManager.assign_control('move_down', pygame.K_DOWN)
        InputManager.assign_control('attack', pygame.K_SPACE)

        self.rootSceneNode = SceneNode()


    def create_scene(self):
        """
        Create The initial scene, should be overriden and create whatever objects your game needs.
        """
        pass


    def update(self):
        """
        Called once per frame, updates all animations scenenodes (and attached objects) and then runs physics checks
        """
        dT = pygame.time.get_ticks()/1000.0 - self.lastTime 

        # Update the animations
        self.animation_frame_time += dT
        if self.animation_frame_time >= 1.0/self.animation_fps:
            TextureManager.next_frame()
            self.animation_frame_time = 0.0

        self.rootSceneNode.update(dT)

        PhysicsManager.run_checks(self.rootSceneNode)


    def render(self):
        """
        Called once per frames, draws all objects to the screen, and all level tiles
        """
        fillcolour = LevelManager.get_fill_colour()
        self.screen.fill(fillcolour)

        LevelManager.render_level(self.screen)

        self.rootSceneNode.render(self.screen)
        # self.screen.blit(PhysicsManager.draw_debug((self.screen_width, self.screen_height), self.rootSceneNode), (0,0))

        LevelManager.render_level(self.screen, True)

        pygame.display.flip()

    
    def quit(self):
        """
        Ends the game after this frame is completed
        """
        self.running = False

   
    def start_game(gameclass):
        """
        Initialises the game, setups all all Manager classes, creates the scene and then runs the game loop
        """
        pygame.init() # Start pygame.
        InputManager.setup()
        LevelManager.setup()

        game = gameclass
        game.setup() # Set up the window
        game.create_scene()


        while(game.running):
            events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.quit()
                else:
                    events.append(event)
            InputManager.update(events)

            game.update() # Update the game code
            game.render() # Render all the game objects

            game.updateTime()
            # pygame.time.delay(int(((1/60.0) - game.lastElapsed) * 1000))
            pygame.time.delay(16) # 60 FPS


if __name__ == "__main__":
    Game.start_game( Game() )
