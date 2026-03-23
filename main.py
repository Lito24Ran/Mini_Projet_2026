from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Navigation_screen_Manager import NavigationScreenManager
from map2 import Mymap
from kivy.uix.boxlayout import BoxLayout
from Progress_bar import ProgressBarWidget
from kivy.properties import ObjectProperty

from kivy_garden.mapview import MapMarker
import requests

# charger le KV
Builder.load_file("map2.kv")
Builder.load_file("Bar_de_recherche.kv")






class MyScreenManager(NavigationScreenManager):
    pass


class MyApp(MDApp):

    manager = ObjectProperty(None)

    def build(self):

        self.manager = MyScreenManager()

        return self.manager


if __name__ == '__main__':
    def test_recherche(self):
     print("Test méthode recherche - OK")
     self.rechercher()
    
    MyApp().run()