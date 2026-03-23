from kivy.uix.boxlayout import BoxLayout
from TaxiMoto import TaxiMoto
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

from kivy.properties import ListProperty

# Builder.load_file('Moto.kv')

class SelectableLabel(RecycleDataViewBehavior):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
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
    
    # Hauteurs des sections


    def on_touch_down(self, touch):
        DETAIL_H = dp(100)   # titre dp(20) + texte dp(60) + padding/spacing
        ACTION_H = dp(50)
        HEADER_H = dp(80)
        if self.collide_point(*touch.pos):
            detail = self.ids.detail_box
            action = self.ids.action_box

            if detail.height == 0:
                anim_detail = Animation(height=DETAIL_H, opacity=1, duration=0.3)
                # anim_action = Animation(height=ACTION_H, opacity=1, duration=0.3)
                # anim_self   = Animation(height=HEADER_H + DETAIL_H + ACTION_H, duration=0.3)
            else:
                # ── Fermer ──────────────────────────────────────
                anim_detail = Animation(height=0, opacity=0, duration=0.3)
                anim_action = Animation(height=0, opacity=0, duration=0.3)
                anim_self   = Animation(height=HEADER_H, duration=0.3)

            anim_detail.start(detail)
            # anim_action.start(action)
            # anim_self.start(self)      # ← le widget lui-même grandit/rétrécit

            return True
        return super().on_touch_down(touch)
    

        
class MainWidget(BoxLayout) :
    
    recycleViews = ObjectProperty(None)
    expanded = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.motos = [
            TaxiMoto("moto1", False, "Analakely", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),
            TaxiMoto("moto2", True, "Ambojanahary", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),
            TaxiMoto("moto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),   
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte."),    
            TaxiMoto("Tojomoto3", False, "Analamahitsy", "Le Lorem Ipsum est un texte de remplissage utilisé dans le secteur de l'imprimerie et de la composition. Depuis le XVIe siècle, il sert de texte factice standard, lorsqu'un imprimeur anonyme a mélangé des caractères pour créer un livre d'exemples typographiques. Il a traversé les siècles, s'adaptant même à la composition électronique, sans subir de modifications majeures. Sa popularité a explosé dans les années 1960 avec la commercialisation des feuilles Letraset contenant des extraits de Lorem Ipsum, puis plus récemment avec les logiciels de PAO comme Aldus PageMaker, qui intègrent des versions de ce texte.")    
            
        ]
        
    
        
    def on_parent(self, widget, parent):
        self.recycleViews.data = [moto.get_dictionary() for moto in self.motos ]

class MotoApp(App):
    pass

if __name__ == '__main__':
    MotoApp().run()
    