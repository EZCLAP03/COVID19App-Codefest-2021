from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import input



class CovidApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.country = Builder.load_string(input.country)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        screen.add_widget(self.country)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        print(self.country.text)
<<<<<<< Updated upstream
=======
        for content in data['Country']:
            if content['name'] == self.country.text:
                dialog = MDDialog(text=content["Total_cases"])
                dialog.open()
                print(content["Total_cases"])
>>>>>>> Stashed changes


CovidApp().run()