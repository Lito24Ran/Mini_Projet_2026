from kivy .lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout  import GridLayout
from http_client import HttpClient

Builder.load_file('navigation_bar.kv')

class NavigationBar(FloatLayout) :
    pass
