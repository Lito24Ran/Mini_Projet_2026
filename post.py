from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from datetime import datetime, timezone, timedelta
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import MDSnackbar
from http_client import HttpClient
from geopy.geocoders import Nominatim
import requests
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import threading
from plyer import gps
class PostScreen(Screen):
    lat = 0.0
    lon = 0.0
    adresse = ""
    
    def on_enter(self):
        self.get_precise_ip_location()

    def get_precise_ip_location(self):
        access_token = '02cf4d44d62a79'
        url = f"https://ipinfo.io/json?token={access_token}"
        
        try:
            res = requests.get(url, timeout=5).json()
            location = res.get('loc', '0,0').split(',')
            self.lat = location[0]
            self.lon = location[1]
            print(f"Lieu estimé (ipinfo) : {res.get('city')}, {res.get('region')}")
            print(f"{self.lat},  {self.lon}")
            # self.reverse_geocode_free(self.lat, self.lon)
        except:
            return None, None
            
    def reverse_geocode_free(self, lat, lon):
        try:
            geolocator = Nominatim(user_agent="Taxi_moto")
            
            location = geolocator.reverse(f"{lat}, {lon}", timeout=10)
            
            if location and "address" in location.raw:
                address = location.raw['address']
                
                # On cherche la ville dans l'ordre de précision décroissant
                quartier = address.get('suburb', address.get('neighbourhood', 'Quartier non répertorié'))
                
                return quartier
            
            return "Ville introuvable"
                
        except Exception as e:
            print(f"Erreur de géocodage : {e}")
            return "Erreur de localisation"
        
        
    def publish_post(self):
        ids = self.ids
        app = MDApp.get_running_app()
        heure_utc = datetime.now(timezone.utc)
        print("Heure UTC :", heure_utc.strftime("%H:%M:%S"))
        print("lat:", self.lat)
        print("lon:", self.lon)
        print("adresse:", self.adresse)
        print("nom:", self.ids.nom_personne.text.strip())
        print("tarif:", self.ids.tarif.text.strip())
        print("contact:", self.ids.contact.text.strip())
        print("description:", self.ids.description.text.strip())
        print("Cartier exacte:", self.reverse_geocode_free(self.lat, self.lon))
        
        HttpClient().creation_publication(
            self.ids.nom_personne.text.strip(),  
            self.reverse_geocode_free(self.lat, self.lon),
            self.lat,                           
            self.lon,                           
            heure_utc,                           
            self.ids.tarif.text.strip(),         
            self.ids.contact.text.strip(),       
            self.ids.description.text.strip()   
        )
        
    def clear_fields(self):
        for f in self.ids:
            self.ids[f].text = ""
            
    

class ListScreen(Screen):
    def on_enter(self):
        """Charger les posts dès qu'on arrive sur l'écran"""
        self.load_posts()

    def load_posts(self):
        app = MDApp.get_running_app()
    
    # 2. On vérifie si l'ID existe dans cet écran (ListScreen)
        if "posts_box" in self.ids:
            box = self.ids.posts_box
            box.clear_widgets() # On vide la liste avant de la recréer
            
            # 3. On boucle sur les données pour créer les cartes
            for i, post in enumerate(app.posts):
                # Création de ta carte (MDCard)
                card = MDCard(
                    orientation="vertical",
                    padding=dp(15),
                    size_hint_y=None,
                    height=dp(180),
                    radius=[15],
                )   
            card = MDCard(
                orientation="vertical",
                padding=dp(15),
                spacing=dp(10),
                size_hint_y=None,
                height=dp(200), # Augmenté un peu pour le confort
                radius=[15],
                elevation=2,
            )

            # Titre avec le Nom et le Tarif
            title = MDLabel(
                text=f"nom • 15000 Ar",
                font_style="H6",
                bold=True,
                size_hint_y=None,
                height=dp(30)
            )

            # Détails (Adresse et Contact)
            details = MDLabel(
                text=(
                    f"📍 da;ljf\n"
                    f"💬 adjkfa\n"
                    f"📞 adjka"
                ),
                theme_text_color="Secondary",
                halign="left",
            )

            # btn = MDRaisedButton( # Un bouton plus visible
            #     text="Modifier",
            #     on_release=lambda x, idx=i: app.edit_post(idx),
            #     pos_hint={"right": 1}
            # )

            card.add_widget(title)
            card.add_widget(details)
            # card.add_widget(btn)
            box.add_widget(card)