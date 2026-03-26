from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from Container_liste_moto import MotoWidget as detailmoto
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
Builder.load_file("detail.kv")

class DetailTaximoto(BoxLayout):
    
    nom = StringProperty()
    lieu = StringProperty()
    description = StringProperty()
    
    nom = detailmoto.nom
    detailmoto.description
    detailmoto.disponibile
    
    pass

# class TestApp(MDApp):
#     def build(self):
#         return DetailTaximoto()

# if __name__ == '__main__':
#     TestApp().run()