from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy_garden.mapview import MapView
from Bar_de_recherche import Bar_de_recherche

Builder.load_file('map2.kv')

class Mymap(FloatLayout):
    mapview = ObjectProperty(None)
    bar_recherche = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_mapview(self, instance, value):
        """Appelé quand mapview est assigné"""
        print(f"✅ MapView assignée: {value}")
    
    def on_bar_recherche(self, instance, value):
        """Appelé quand bar_recherche est assignée"""
        print(f"✅ Barre de recherche assignée: {value}")
        if value and self.mapview:
            print(f"🔗 Liaison vérifiée: bar_recherche.mapview = {value.mapview}")