from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import MDSnackbar


#Builder.load_file("post.kv")

class PostScreen(Screen):
    
    def publish_post(self):
        app = MDApp.get_running_app() 
        ids = self.ids                 

        data = {
            "zone":    ids.zone.text.strip(),
            "depart":  ids.depart.text.strip(),
            "debut":   ids.debut.text.strip(),
            "fin":     ids.fin.text.strip(),
            "tarif":   ids.tarif.text.strip(),
            "moto":    ids.moto.text.strip(),
            "contact": ids.contact.text.strip(),
        }

        champs_obligatoires = {
            "zone":    "Zone obligatoire",
            "depart":  "Point de départ obligatoire",
            "contact": "Contact obligatoire",
        }
        for champ, message in champs_obligatoires.items():
            if not data[champ]:
                MDSnackbar(MDLabel(text=message)).open()
                return

        if app.edit_index is not None:          
            app.posts[app.edit_index] = data   
            app.edit_index = None
            MDSnackbar(MDLabel(text="Post modifé")).open()
        else:
            app.posts.append(data)             
            MDSnackbar(MDLabel(text="course publier")).open()

        self.clear_fields()
        app.go_list()                           

    def clear_fields(self):
        for f in self.ids:
            self.ids[f].text = ""
            
    

class ListScreen(Screen):

    def load_posts(self):
        app = MDApp.get_running_app()
        box = self.ids.posts_box
        box.clear_widgets()

        for i, post in enumerate(app.posts):    
            card = MDCard(
                orientation="vertical",
                padding=dp(12),
                spacing=dp(6),
                size_hint_y=None,
                height=dp(180),
                radius=[12],
            )
            label = MDLabel(
                text=(
                    f"📍 Zone : {post['zone']}\n"
                    f"🚩 Départ : {post['depart']}\n"
                    f"⏰ {post['debut']} → {post['fin']}\n"
                    f"💰 {post['tarif']} Ar\n"
                    f"🏍️ {post['moto']}\n"
                    f"📞 {post['contact']}"
                ),
                halign="left",
            )
            btn = MDFlatButton(
                text="Modifier",
                on_release=lambda x, idx=i: app.edit_post(idx)
            )
            card.add_widget(label)
            card.add_widget(btn)
            box.add_widget(card)
            
