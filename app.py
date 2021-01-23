import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


class Layout(PageLayout):

    def __init__(self):
        super(PageLayout, self).__init__()

        btn1 = Button(text='Page 1')

        btn2 = Button(text='Page 2')

        btn3 = Button(text='Page 3')

        self.add_widget(btn1)

        self.add_widget(btn2)

        self.add_widget(btn3)


class LayoutApp(App):

    def build(self):
        return PageLayout()


if __name__ == '__main__':
    LayoutApp().run()
