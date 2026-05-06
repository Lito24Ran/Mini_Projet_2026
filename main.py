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
from demande import DemandePublication
from http_client import HttpClient
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
        
    def _format_time(self, field, text):
        digits = ''.join(filter(str.isdigit, text))
        
        if len(digits) >= 3:
            formatted = digits[:2] + ':' + digits[2:4]
        else:
            formatted = digits
        
        if field.text != formatted:
            field.text = formatted
            
    def edit_post(self, index):
        # 1. On mémorise l'index qu'on modifie
        self.edit_index = index
        
        # 2. On récupère les données du post
        post_data = self.posts[index]
        
        # 3. On accède à l'écran 'post' (PostScreen)
        post_screen = self.root.get_screen("post")
        
        # 4. On remplit les champs avec les données existantes
        post_screen.ids.nom_personne.text = post_data.get('nom_personne', '')
        post_screen.ids.tarif.text = str(post_data.get('tarif', ''))
        post_screen.ids.contact.text = post_data.get('contact', '')
        post_screen.ids.description.text = post_data.get('description', '')
        
        # 5. On change d'écran vers le formulaire
        self.root.current = "post"
        
    def valider(self):
        tarif_text = self.root.ids.tarif.text
        
        if not tarif_text:
            print("Tarif vide")
            return
        
        try:
            tarif = float(tarif_text)
            if tarif < 0:
                self.root.ids.tarif.error = True
                self.root.ids.tarif.helper_text = "Le tarif ne peut pas être négatif"
            else:
                print(f"Tarif valide : {tarif} Ar")
        except ValueError:
            self.root.ids.tarif.error = True
            
    def _format_contact(self, field, text):
        digits = ''.join(filter(str.isdigit, text))
    
        digits = digits[:10]

        operateurs_valides = ('032', '033', '034', '038')
        if len(digits) >= 3:
            if not digits.startswith(operateurs_valides):
                field.error = True
                field.helper_text = "Numéro invalide — commence par 032, 033, 034 ou 038"
            else:
                field.error = False
                field.helper_text = "Doit commencer par 032, 033, 034, 038"

        if len(digits) >= 8:
            formatted = f"{digits[:3]} {digits[3:5]} {digits[5:8]} {digits[8:10]}"
        elif len(digits) >= 5:
            formatted = f"{digits[:3]} {digits[3:5]} {digits[5:]}"
        elif len(digits) >= 3:
            formatted = f"{digits[:3]} {digits[3:]}"
        else:
            formatted = digits

        if field.text != formatted:
            field.text = formatted

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
    
    def naviguer_demande(self):
        HttpClient().demande_approuver(self.aller_page)
    
    def aller_page(self, approuvee):    
        if approuvee:
            self.root.push("postscreen")
        else:
            self.root.push("Demande")


if __name__ == '__main__':
    MyApp().run()