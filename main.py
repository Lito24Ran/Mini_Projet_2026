from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Navigation_screen_Manager import NavigationScreenManager
from map2 import Mymap
from kivy.uix.boxlayout import BoxLayout
from Progress_bar import ProgressBarWidget
from Container_liste_moto import MainWidget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy_garden.mapview import MapMarker
from barreRetour import BarreRetour

# charger le KV
Builder.load_file("Moto.kv") 
Builder.load_file("map2.kv")
Builder.load_file("BarreRetour.kv")
Builder.load_file("bar_de_recherche.kv")

class MyScreenManager(NavigationScreenManager):
    pass


class MyApp(MDApp):
    Window.size = (360,640)
    Window.resizable = False
    manager = ObjectProperty(None)

    def build(self):
        try:
            self.manager = MyScreenManager()
            print("MyScreenManager créé ✅")
            return self.manager
        except Exception as e:
            print(f"Erreur : {e}")            
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    # def test_recherche(self):
    #     print("Test méthode recherche - OK")
    #     # self.rechercher()
    
    MyApp().run()