from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import input
from main import covid19api


class CovidApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        self.user_input = Builder.load_string(input.user)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        screen.add_widget(self.user_input)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        data = covid19api()
        for content in data['Country']:
            if content['name'] == self.user_input.text:
                dialog = MDDialog(title='Covid 19 stats in your preferred area', text=self.user_input.text)
                dialog.open()
                print(content)


CovidApp().run()
