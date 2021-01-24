from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
import main
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
import os
from kivy_garden.mapview import MapView

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
                    id: mtf
                    hint_text: "Enter Your Destination"
                    helper_text: "or your area"
                    helper_text_mode: "on_focus"
                    icon_right: "android"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x:None
                    width:250


                MDRectangleFlatButton:
                    id: 'amulcool'
                    text: "show"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    on_press: app.show_data()
            Screen:
                name: 'scr 2'
                MapView:
                    id: map_view
                    zoom: 2
                    lat: 12.97
                    lon: 77.59

                MDRectangleFlatButton:
                    text: "Quit"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    on_release: screen_manager.current = "scr 1"

            Screen:
                name: 'scr 3'
                MDTextField:
                    id: mtf2
                    hint_text: "Enter Your Region"
                    helper_text: "or your area"
                    helper_text_mode: "on_focus"
                    icon_right: "android"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x:None
                    width:250

                MDRectangleFlatButton:
                    id: 'amulcool2'
                    text: "show"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    on_press: app.show_data2()



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

                ScrollView:
                    MDList:

                        OneLineListItem:
                            text: "Covid19 Statistics"
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "scr 1"

                        OneLineListItem:
                            text: "Map"
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "scr 2"
                        
                        OneLineListItem:
                            text: "Weather Statistics"
                            on_press:
                                nav_drawer.set_state("close")
                                screen_manager.current = "scr 3"

"""


class DemoApp(MDApp):
    screenboi = ObjectProperty(None)

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

    def show_data(self):
        data = main.covid19api()
        mtf = self.root.ids.mtf.text
        for content in data['Country']:
            if content['name'] == mtf:
                dialog = MDDialog(title=f'Covid 19 Cases in the area {content["Total_cases"]} \
                \nCovid 19 Deaths in the Country {content["Total_deaths"]} \
                \nCovid 19 Recovered in the Country {content["Total_recovered"]} \
                \nCovid 19 Active cases in the Country {content["Active_cases"]} \
                \nCovid 19 Serious critical cases in the Country {content["Serious_critical"]}  \
                \nTotal Population of the Country {content["Total_population"]}')
                dialog.open()
                print(content["Total_cases"])
    
    def show_data2(self):
        data = main.weatherapi()
        mtf2 = self.root.ids.mtf2.text
        for content in data['Country']:
            if mtf2 in content['name']:
                dialog = MDDialog(title=content['Temperature'])
                dialog.open()
                print(content)
            

DemoApp().run()
