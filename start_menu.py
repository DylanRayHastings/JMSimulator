# start_menu.py
from panda3d.core import TexturePool, CardMaker, Vec4
from panda3d.core import Loader
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectFrame import DirectFrame

class StartMenu:
    def __init__(self, parent, loader):
        self.parent = parent
        self.loader = loader
        self.jersey_mikes_logo_path = "JM.png"
        self.jersey_mikes_logo_texture = TexturePool.loadTexture(self.jersey_mikes_logo_path)

        custom_font = self.loader.loadFont("Dosis-ExtraLight.ttf")
        custom_font.setPixelsPerUnit(60)
        custom_font.setPageSize(512, 512)
        self.custom_font = custom_font

    def draw_menu(self):
        print("Drawing menu...")
        menu_frame = DirectFrame(parent=self.aspect2d, frameColor=(1, 1, 1, 1), frameSize=(-1, 1, -1, 1), pos=(0, 0, 0))
        menu_frame.setBin("fixed", 0)

        logo_card_maker = CardMaker("logo_card")
        logo_card_maker.setFrame(-1, 1, -1, 1)

        logo_card_np = menu_frame.attachNewNode(logo_card_maker.generate())
        logo_card_np.setTexture(self.jersey_mikes_logo_texture)

        horizontal_scale_factor, vertical_scale_factor = 1, 0.125
        logo_card_np.setScale(horizontal_scale_factor, 1, vertical_scale_factor)

        print("Creating buttons...")
        self.new_game_button = DirectButton(parent=menu_frame, text="New Game", command=self.parent.new_game_clicked, text_fg=(1, 1, 1, 1), text_scale=(0.1, 0.1), text_pos=(0, -0.02), relief=None, text_font=self.custom_font, pos=(0, 0, 0.5), text_shadow=(0, 0, 0, 0.5))
        self.load_game_button = DirectButton(parent=menu_frame, text="Load Game", command=self.parent.load_game_clicked, text_fg=(1, 1, 1, 1), text_scale=(0.1, 0.1), text_pos=(0, -0.02), relief=None, text_font=self.custom_font, pos=(0, 0, 0.2), text_shadow=(0, 0, 0, 0.5))

        print("New Game Button:", self.new_game_button.isHidden())
        print("Load Game Button:", self.load_game_button.isHidden())
