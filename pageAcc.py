from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.lang import Builder
import time
from kivy.clock import Clock
Builder.load_file('page.kv')
class PageAcc(GridLayout) :
        def on_slider_active(self, widget):
            print("Slider active:", widget.value)
        
            