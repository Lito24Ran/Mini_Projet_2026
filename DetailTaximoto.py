from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from Container_liste_moto import MotoWidget as detailmoto
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
Builder.load_file("detail.kv")

class DetailTaximoto(Screen): 
    # ← Screen, pas BoxLayout
    nom         = StringProperty("")
    lieu        = StringProperty("")
    disponibile = BooleanProperty(None)
    description = StringProperty("")
    
    def on_enter(self):  
        app = MDApp.get_running_app()
        
        self.nom = app.moto_nom
        self.lieu = app.lieu_recherche
        self.disponibile = app.moto_disponibile
        self.description = app.moto_description
        print(f"app.moto_nom : {app.moto_nom} , lieu {app.lieu_recherche}, disponibilite: {app.moto_disponibile}, description: {app.moto_description}")
