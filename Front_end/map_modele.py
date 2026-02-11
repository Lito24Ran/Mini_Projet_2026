from kivymd.app import MDApp
from kivy_garden.mapview import MapView

class Map_modele(MDApp) :
    
    def build(self):
        Mamap = MapView(zoom = 10, lat = 30,lon = -115)
        return Mamap
    

Map_modele().run()