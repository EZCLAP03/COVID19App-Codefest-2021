from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
import input
from main import covid19api
from kivymd.theming import ThemeManager


class CovidApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Screen()
        theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        self.user = Builder.load_string(input.user)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)

        screen.add_widget(self.user)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        print(self.user.text)
        data = covid19api()
        for content in data['Country']:
            if content['name'] == self.user.text:
                dialog = MDDialog(title=f'Covid 19 Cases in the area {content["Total_cases"]} \
                    \nCovid 19 Deaths in the Country {content["Total_deaths"]} \
                    \nCovid 19 Recovered in the Country {content["Total_recovered"]} \
                    \nCovid 19 Active cases in the Country {content["Active_cases"]} \
                    \nCovid 19 Serious critical cases in the Country {content["Serious_critical"]}  \
                    \nTotal Population of the Country {content["Total_population"]}')
                dialog.open()
                print(content["Total_cases"])


CovidApp().run()
