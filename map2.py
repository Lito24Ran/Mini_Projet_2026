from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy_garden.mapview import MapView
from Bar_de_recherche import Bar_de_recherche
from http_client import HttpClient
from kivy_garden.mapview import MapMarker
from kivy.clock import Clock
Builder.load_file('map2.kv')

class Mymap(FloatLayout):
    mapview = ObjectProperty(None)
    bar_recherche = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_server(self, all_pub):
        # On demande à Kivy de gérer l'affichage sur son thread principal
        Clock.schedule_once(lambda dt: self.ajouter_les_marqueurs(all_pub))

    def ajouter_les_marqueurs(self, all_pub):
        for moto in all_pub:
            # Vérifiez bien si c'est "latitude" ou "lat" ici selon votre print !
            lat_str = moto.get("latitude", "") 
            lon_str = moto.get("longitude", "")
            
            if lat_str and lon_str:
                try:
                    lat = float(lat_str)
                    lon = float(lon_str)
                    
                    marker = MapMarker(lat=lat, lon=lon)
                    self.ids.mapview_widget.add_marker(marker)
                    print(f"📍 Marqueur ajouté avec succès à : {lat}, {lon}")
                except ValueError:
                    pass
    
    def on_mapviews(self, value):
        HttpClient().all_publication(self.on_server)
        print(f"✅ MapView assignée: {value}")
    
    def on_bar_recherche(self, instance, value):
        print(f"✅ Barre de recherche assignée: {value}")
        if value and self.mapview:
            print(f"🔗 Liaison vérifiée: bar_recherche.mapview = {value.mapview}")