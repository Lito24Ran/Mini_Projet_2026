from turtle import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from Navigation_screen_Manager import NavigationScreenManager
from kivy.uix.screenmanager import Screen

Builder.load_file('progressbar.kv')

class ProgressBarWidget(MDBoxLayout) :  
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.i = 0
        # Démarrer automatiquement après initialisation
        Clock.schedule_once(self.start_loading, 0.5)
        self.push = False
        
    def start_loading(self, dt):
        """Démarre le chargement"""
        self.i = 0
        self.ids.my_progressbar.value = 0
        # self.ids.progress_label.text = "0%"
        Clock.schedule_interval(self.loader, 0.1)
    
    def loader(self, dt):  
        self.i += 10
        self.ids.my_progressbar.value = self.i
        # self.ids.progress_label.text = f"{self.i}%"
        
        if self.i >= 100:
            Clock.unschedule(self.loader)
            print("Chargement terminé!")

            