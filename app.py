from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

toolbar_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Covid App"
                        elevation: 10
                        left_action_items: [['menu', lambda x: tool_drawer.toggle_tool_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: tool_drawer
"""


class CovidApp(MDApp):

    def build(self):
        screen = Builder.load_string(toolbar_helper)
        return screen

CovidApp().run()



