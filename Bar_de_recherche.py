from kivy.lang import Builder
import time
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapMarkerPopup
from kivy.properties import ObjectProperty
from kivymd.app import MDApp   
import requests

Builder.load_file("bar_de_recherche.kv")


class Bar_de_recherche(FloatLayout):

    # liaison avec MapView dans le KV
    mapview = ObjectProperty(None)
    derniere_requete = 0  
    marqueurs_existants = [] 

    def rechercher(self):

        self.texte = self.ids.search_input.text.strip()

        if not self.texte:
            print("Champ vide")
            return
        try:

            # supprimer anciens marqueurs
            for child in self.mapview.children[:]:
                if isinstance(child, MapMarkerPopup):
                    self.mapview.remove_widget(child)
                    
            VIEWBOX_ANTANANARIVO = "47.4,-18.8,47.7,-19.0"
            
            # requête vers OpenStreetMap
            url = f"https://nominatim.openstreetmap.org/search?q={self.texte}&format=json&limit=1&countrycodes=mg&viewbox={VIEWBOX_ANTANANARIVO}&bounded=1"

            headers = {
                "User-Agent": "MiniProjetKivyMap/1.0"
            }

            response = requests.get(url, headers=headers, timeout=5)

            data = response.json()
            
            app = MDApp.get_running_app()
            # app.manager.push("liste_moto") 
            app.lieu_recherche = self.texte  
            
            if data:

                lat = float(data[0]["lat"])
                lon = float(data[0]["lon"])

                # création marqueur
                marker = MapMarkerPopup(lat=lat, lon=lon)

                self.mapview.add_widget(marker)

                # déplacer la carte
                self.mapview.center_on(lat, lon)

                print("Lieu trouvé :", self.texte)

            else:
                print("Aucun résultat pour :", self.texte)

        except Exception as e:
            print("Erreur recherche :", e)

    def effacer(self):
        self.ids.search_input.text = ""

    def on_search_button(self):
        self.rechercher()  
        
        
    def centrer(self):

        if self.mapview:
            self.mapview.center_on(-18.8792, 47.5079)

    
    def test_input(self):
        texte = self.ids.search_input.text
        print("=== TEST ===")
        print("Texte:", texte)
        print("Longueur:", len(texte))
        print("Vide?", texte == "")
        print("===========")

    
