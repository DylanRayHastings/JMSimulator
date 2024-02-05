from asyncio import TaskGroup, taskgroups
from asyncio.mixins import _global_lock
import pickle, sys, math, random, os
from panda3d.core import Loader
from simulator.start_menu import StartMenu
from simulator.simulator import FranchiseSimulator
from panda3d.core import Point3, CardMaker, Vec4, Vec3, BitMask32, CollisionPlane, Plane, CollisionNode, CollisionSphere, DirectionalLight, NodePath, WindowProperties, TextNode, TexturePool, ModifierButtons, ClockObject
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame
from direct.task import Task

# TODO: Make start_menu work

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
print("Changed Working Directory to:", script_directory)

class FranchiseSimulatorGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # Load Jersey Mike's logo texture
        self.jersey_mikes_logo_path = "JM.png"
        self.jersey_mikes_logo_texture = self.loader.loadTexture(self.jersey_mikes_logo_path)
        if not self.jersey_mikes_logo_texture:
            sys.exit(f"Error: Could not load texture: {self.jersey_mikes_logo_path}")

        # Set up custom title font
        custom_title_font = self.loader.loadFont("Dosis-Medium.ttf")
        custom_title_font.setPixelsPerUnit(60)
        custom_title_font.setPageSize(512, 512)

        # Create title and shadow text
        self.title_text = OnscreenText(text="Jersey Mike's Franchise Simulator", pos=(0, 0.8), scale=0.1, fg=(0.8627, 0.149, 0.149, 1), align=TextNode.ACenter, mayChange=False, font=custom_title_font)
        self.shadow_text = OnscreenText(text="Jersey Mike's Franchise Simulator", pos=(0.005, 0.795), scale=0.1, fg=(0, 0, 0, 0.5), align=TextNode.ACenter, mayChange=False, font=custom_title_font)

        # Set initial values and states
        self.jersey_mikes_logo_scale = 1.0
        self.ignore("mouse1")
        self.ignore("mouse3")
        self.mouse_sensitivity = 0.1
        self.game, self.MENU_STATE, self.PLAYING_STATE, self.current_state = None, 'menu', 'playing', 'menu'
        self.new_game_button, self.load_game_button = None, None
        self.bounce_amplitude, self.bounce_frequency, self.bounce_offset = 0.1, 2.0, 0.0
        self.move_forward, self.move_backward, self.move_left, self.move_right = False, False, False, False
        self.heading, self.pitch, self.mouse_speed_x, self.mouse_speed_y = 0, 0, 0.2, 0.2

        # Set up input handling
        self.accept('w', self.start_move, ['forward'])
        self.accept('w-up', self.stop_move, ['forward'])
        self.accept('s', self.start_move, ['backward'])
        self.accept('s-up', self.stop_move, ['backward'])
        self.accept('a', self.start_move, ['left'])
        self.accept('a-up', self.stop_move, ['left'])
        self.accept('d', self.start_move, ['right'])
        self.accept('d-up', self.stop_move, ['right'])

        # Add bounce task
        self.task_mgr.add(self.bounce_task, 'bounce_task')

        # Set up player
        self.player = self.render.attachNewNode(CollisionNode("player"))
        self.player.setTag("player", "True")
        self.player.setCollideMask(BitMask32.bit(0))
        player_collision_sphere = CollisionSphere(0, 0, 0, 1.0)
        player_collision_node = CollisionNode("player_collision")
        player_collision_node.addSolid(player_collision_sphere)
        self.player.attachNewNode(player_collision_node)
        self.player.setColor(1, 1, 1, 1)
        self.player.setPos(0, 0, 5)

        # Set up directional light
        self.directional_light = DirectionalLight('directional_light')
        self.directional_light.setColor((1, 1, 1, 1))
        self.directional_light_np = self.render.attachNewNode(self.directional_light)
        self.directional_light_np.setPos(1, 1, 1)

        # Set up input handling and tasks
        self.accept('escape', self.quit_game)
        self.task_mgr.add(self.update_game, 'update_game_task')

        # Draw the start menu
        self.start_menu = StartMenu(self, self.loader)
        self.start_menu.draw_menu()

        # Set window properties
        wp = WindowProperties()
        wp.setSize(self.pipe.getDisplayWidth(), self.pipe.getDisplayHeight())
        wp.setFullscreen(True)
        self.win.requestProperties(wp)

        # Set initial camera position
        self.camera.setPos(0, -10, 2)
        self.camera.lookAt(Vec3(0, 0, 0))

    def quit_game(self):
        sys.exit()
    
    def start_move(self, direction):
        setattr(self, f'move_{direction}', True)
        
    def stop_move(self, direction):
        setattr(self, f'move_{direction}', False)
    
    def bounce_task(self, task):
        bounce_height = self.bounce_amplitude * math.sin(self.bounce_frequency * task.time + self.bounce_offset)
        self.camera.setZ(bounce_height + 2)
        return task.cont

    def update_game(self, task):
        dt = ClockObject.getGlobalClock().getDt()
        if self.current_state == self.PLAYING_STATE:
            self.handle_playing_state(dt)
        return task.cont

    def new_game_clicked(self):
        self.logo_card_np.setScale(0)
        self.logo_card_np.detachNode()
        self.title_text.destroy()
        self.new_game_button.destroy()
        self.load_game_button.destroy()
        self.shadow_text.destroy()
        self.game = FranchiseSimulator()
        self.current_state = self.PLAYING_STATE
        self.setup_game_environment()
        
    def setup_game_environment(self):
        floor_np = self.render.attachNewNode("floor")
        square_size, num_squares = 10, 100
        for i in range(-num_squares // 2, num_squares // 2):
            for j in range(-num_squares // 2, num_squares // 2):
                square_color = Vec4(1, 1, 1, 1) if (i + j) % 2 == 0 else Vec4(0, 0, 0, 1)
                square_maker = CardMaker(f"square_{i}_{j}")
                square_maker.setFrame(i * square_size, (i + 1) * square_size, j * square_size, (j + 1) * square_size)
                square_np = floor_np.attachNewNode(square_maker.generate())
                square_np.setColor(square_color)

        floor_collision_node = CollisionNode("floor_collision")
        floor_collision_node.addSolid(CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, 0))))
        floor_collision_np = floor_np.attachNewNode(floor_collision_node)
        floor_collision_np.setCollideMask(BitMask32.bit(0))

        self.player.setPos(0, 0, 5)
        self.player.setCollideMask(BitMask32.bit(0))
        self.camera.setPos(0, -10, 2)
        self.camera.lookAt(self.player)
                
    def load_game_clicked(self):
        self.new_game_button.destroy()
        self.load_game_button.destroy()
        self.game = self.load_game_from_saves()
        self.current_state = self.PLAYING_STATE

    def handle_playing_state(self, dt):
        if self.mouseWatcherNode.hasMouse():
            mouseX, mouseY = self.mouseWatcherNode.getMouse()
            self.heading -= mouseX * self.mouse_speed_x
            self.pitch += mouseY * self.mouse_speed_y
            self.pitch = max(min(self.pitch, 90), -90)
            self.player.setH(self.heading)
            self.camera.setHpr(self.heading, self.pitch, 0)
        self.disable_mouse_buttons()
        if self.move_forward: self.player.setY(self.player, 5 * dt)
        if self.move_backward: self.player.setY(self.player, -5 * dt)
        if self.move_left: self.player.setX(self.player, -5 * dt)
        if self.move_right: self.player.setX(self.player, 5 * dt)

    def disable_mouse_buttons(self):
        if self.mouseWatcherNode.hasMouse():
            mouseX, mouseY = self.mouseWatcherNode.getMouse()
            self.handle_mouse_click()

    def handle_mouse_click(self):
        if self.mouseWatcherNode.getMouse():
            mouseX, mouseY = self.mouseWatcherNode.getMouse()
            if self.new_game_button and self.new_game_button.contains(mouseX, 0, mouseY):
                self.new_game_clicked()
            if self.load_game_button and self.load_game_button.contains(mouseX, 0, mouseY):
                self.load_game_clicked()

    def load_game_from_saves(self):
        try:
            with open('save_game.pkl', 'rb') as file:
                saved_data = pickle.load(file)
            return saved_data
        except FileNotFoundError:
            print("No saved game found.")
            return None
        except Exception as e:
            print(f"Error loading saved game: {e}")
            return None

    def quit_game(self):
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    app = FranchiseSimulatorGame()
    app.run()