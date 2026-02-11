from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.lang import Builder

Builder.load_file('page.kv')

class PageAcc(GridLayout) :
    
    def on_enter(self):
        print("Démarrage animation...")
        try:
            progressbar = self.ids.my_progressbar
            self.start_progress(progressbar)
        except Exception as e:
            print("Erreur:", e)
        
    def start_progress(self, progressbar):
        print(progressbar)
        anim = Animation(value=100, duration=3)
        anim.start(progressbar)