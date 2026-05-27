from kivy.uix.boxlayout import BoxLayout
from TaxiMoto import TaxiMoto
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivymd.app import MDApp
from barreRetour import BarreRetour
from http_client import HttpClient
# Builder.load_file('Moto.kv')

class SelectableLabel(RecycleDataViewBehavior):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)


    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))
            

class MotoWidget(BoxLayout):
    nom = StringProperty()
    lieu = StringProperty()
    disponibile = BooleanProperty()
    expanded = BooleanProperty(False)
    bg_color = ListProperty([0.96, 0.96, 0.96, 1]) 
    description = StringProperty()
    
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            app = MDApp.get_running_app()
            app.manager.push("detailMoto")  
            app = MDApp.get_running_app()

            app.moto_nom         = self.nom
            app.moto_lieu        = self.lieu
            app.moto_disponibile = self.disponibile
            app.moto_description = self.description
            
            print(f"le nom est {self.nom}")
        return super().on_touch_up(touch)
    
    def _get_recycle_view(self):
        parent = self.parent
        while parent:
            if parent.__class__.__name__ == 'RecycleView':
                return parent
            parent = parent.parent
        return None
            
class MainWidget(Screen) :
    BarreRetour
    
    recycleViews = ObjectProperty(None)
    expanded = BooleanProperty(False)
    app = MDApp.get_running_app()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        app = MDApp.get_running_app() 
        self.lieu = getattr(app, "lieu_recherche", "")
        
    def on_server_data(self, liste_moto):
        if 'recycleViews' in self.ids:
            data = []
            for moto in liste_moto:
                data.append({
                    "nom":          moto.get("nom_personne", ""),
                    "lieu":         moto.get("lieu_nom", ""),
                    "disponibile":  moto.get("disponibile", True),
                    "description":  moto.get("description", ""),
                })
            self.ids['recycleViews'].data = data
    
    def on_enter(self):                        
        app = MDApp.get_running_app()           
        self.lieu = app.lieu_recherche
        print(f"Lieu reçu : {self.lieu}")
        HttpClient().get_publication(self.lieu, self.on_server_data)
        