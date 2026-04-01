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
from post import PostScreen, ListScreen
from Page_Notification import PageNotification
from kivy.properties import StringProperty, BooleanProperty

# charger le KV
Builder.load_file("Moto.kv") 
Builder.load_file("map2.kv")
Builder.load_file("BarreRetour.kv")
Builder.load_file("bar_de_recherche.kv")
Builder.load_file("post.kv")


class MyScreenManager(NavigationScreenManager):
    pass


class MyApp(MDApp):
    Window.size = (360,640)
    Window.resizable = False
    lieu_recherche = StringProperty("") 
    manager = ObjectProperty(None)
    moto_nom         = StringProperty("")    
    moto_lieu        = StringProperty("")    
    moto_disponibile = BooleanProperty(True)  
    moto_description = StringProperty("")
    
    def on_moto_nom(self, instance, value):      
        print(f"moto_nom reçu : {value}")

    def on_moto_lieu(self, instance, value):     
        print(f"moto_lieu reçu : {value}")
    
    def on_moto_description(self, instance, value):
        print(f"La valeur est {value}")
        

    def build(self):
        try:
            self.posts = []         
            self.edit_index = None
            self.manager = MyScreenManager()
            print("MyScreenManager créé ✅")
            return self.manager
        except Exception as e:
            print(f"Erreur : {e}")            
            import traceback
            traceback.print_exc()
            
    def go_main(self):
        self.manager.pop() 
        
    def go_list(self):
        self.root.current = "list"
        self.root.get_screen("list").load_posts()  

    def go_post(self):
        self.root.current = "postscreen"

    def edit_post(self, index):
        if index < 0 or index >= len(self.posts):
            return
        self.edit_index = index
        post = self.posts[index]
        ids = self.root.get_screen("postscreen").ids
        for key in post:
            if key in ids:
                ids[key].text = post[key]
        self.root.current = "postscreen"


if __name__ == '__main__':
    MyApp().run()