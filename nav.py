from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.app import MDApp

Window.size = (300, 500)
navigation_helper = """
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Spectral Bat"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"
                MDTextField:
                    hint_text: "Enter Your Destination"
                    helper_text: "or your area"
                    helper_text_mode: "on_focus"
                    icon_right: "menu"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x:None
                    width:300
                
                MDRectangleFlatButton: 
                    text: 'Show'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_release: self.show_data

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Map"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

                ScrollView:
                    MDList:

                        OneLineListItem:
                            text: "Screen 1"
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "scr 1"

                        OneLineListItem:
                            text: "Screen 2"
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "scr 2"


"""


class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        screen_manager = ObjectProperty()
        nav_drawer = ObjectProperty()

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen

    def on_start(self):
        pass


DemoApp().run()
