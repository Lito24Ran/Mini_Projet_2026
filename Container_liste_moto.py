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
    
    def _get_recycle_view(self):
        parent = self.parent
        while parent:
            if parent.__class__.__name__ == 'RecycleView':
                return parent
            parent = parent.parent
        return None
            
class MainWidget(Screen) :
    
    recycleViews = ObjectProperty(None)
    expanded = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.motos = [
            TaxiMoto("moto1", False, "Analakely", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),
            TaxiMoto("moto2", True, "Ambojanahary", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),
            TaxiMoto("moto3", True, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),   
            TaxiMoto("KotoZafy", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),   
            TaxiMoto("Lexis", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),   
            TaxiMoto("Rakoto", True, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),   
        ]
        Clock.schedule_once(self.charger_donnees, 0)
    
        
    def charger_donnees(self, dt):
        if 'recycleViews' in self.ids:
            data = [moto.get_dictionary() for moto in self.motos]
            print(f"Nombre de motos : {len(data)}")   
            print(f"Données : {data}")                 
            self.ids['recycleViews'].data = data