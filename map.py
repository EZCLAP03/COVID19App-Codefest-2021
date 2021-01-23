from kivy_garden.mapview import MapView
from kivymd.app import MDApp


class MapApp(MDApp):
    def build(self):
        mapview = MapView(zoom=10, lat=12.97, lon=77.59)
        return mapview


MapApp().run()
