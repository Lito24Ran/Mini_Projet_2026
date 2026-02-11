from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.lang import Builder



class MyApp(MDApp) :
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('my.kv')

if __name__ == '__main__' :
    MyApp().run()