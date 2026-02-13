from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.lang import Builder
import time
from kivy.clock import Clock
Builder.load_file('page.kv')
class PageAcc(GridLayout) :
        i = 0
        valeur_pour_progressbar = 0
        
        
        def on_slider_active(self, widget):
            print("Slider active:", widget.value)
        
        def loader(self, *args):
            try:
                self.i += 10
                self.ids.progress.value = self.i
            except:
                Clock.unschedule(self.loader)
        
            