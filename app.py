from kivymd.app import MDApp
from kivy.lang import Builder

toolbar_helper = """
Screen:
    MDTextFieldRound:
        size_hint_x: None
        width: "100dp"
        id: Arrival
        hint_text: "Departure" 
        pos_hint: {"center_x": 0.75, "center_y": 0.8}

    MDTextFieldRound:
        size_hint_x: None 
        width: "100dp"
        id: Arrival
        hint_text: "Arrival" 
        pos_hint: {"center_x": 0.25, "center_y": 0.8}       
        
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Covid App"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: 'vertical'
                
                MDLabel:
                    text: 'Username'
                    font_style: 'Caption'
                MDLabel:
                    text: 'Location'
                    font_style: 'Caption'         
        
                    
                    
"""


class CovidApp(MDApp):

    def build(self):
        screen = Builder.load_string(toolbar_helper)
        return screen


CovidApp().run()
