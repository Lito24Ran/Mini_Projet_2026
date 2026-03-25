from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty

Builder.load_file("BarreRetour.kv")

class BarreRetour(BoxLayout):
    titre = StringProperty("Liste Taxi moto")            
    pass
