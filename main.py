from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Navigation_screen_Manager import NavigationScreenManager
from map2 import Mymap 
from Progress_bar import ProgressBarWidget
from kivy.properties import ObjectProperty

class MyScreenManager(NavigationScreenManager) :
    pass

class MyApp(MDApp) :
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager() #ity d afaka mi conserver bcp de type de screen
        return self.manager
    
if __name__ == '__main__' :
    MyApp().run()