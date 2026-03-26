from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList


KV = """
ScreenManager:
    PostScreen:
    ListScreen:

<PostScreen>:
    name: "post"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Publier une course"
            md_bg_color: 0.05,0.1,0.3,1
            specific_text_color: 1,1,1,1
            right_action_items: [["format-list-bulleted", lambda x: app.go_list()]]

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height

                MDTextField:
                    id: zone
                    hint_text: "Zone"

                MDTextField:
                    id: depart
                    hint_text: "Point de départ"

                MDTextField:
                    id: debut
                    hint_text: "Heure début"

                MDTextField:
                    id: fin
                    hint_text: "Heure fin"

                MDTextField:
                    id: tarif
                    hint_text: "Tarif (Ar)"

                MDTextField:
                    id: moto
                    hint_text: "Moto"

                MDTextField:
                    id: contact
                    hint_text: "Contact"

                MDRaisedButton:
                    text: "Publier"
                    md_bg_color: 0.05,0.1,0.3,1
                    on_release: app.publish_post()


<ListScreen>:
    name: "list"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Mes courses publiées"
            md_bg_color: 0.05,0.1,0.3,1
            specific_text_color: 1,1,1,1
            left_action_items: [["arrow-left", lambda x: app.go_post()]]

        ScrollView:
            MDList:
                id: posts_box
"""


class PostScreen(Screen):
    pass


class ListScreen(Screen):
    pass


class TaxiMotoApp(MDApp):

    def build(self):
        self.posts = []
        self.edit_index = None
        return Builder.load_string(KV)

    # ───────── NAVIGATION ─────────
    def go_list(self):
        self.load_posts()
        self.root.current = "list"

    def go_post(self):
        self.root.current = "post"

    # ───────── PUBLIER ─────────
    def publish_post(self):
        ids = self.root.get_screen("post").ids

        data = {
            "zone": ids.zone.text.strip(),
            "depart": ids.depart.text.strip(),
            "debut": ids.debut.text.strip(),
            "fin": ids.fin.text.strip(),
            "tarif": ids.tarif.text.strip(),
            "moto": ids.moto.text.strip(),
            "contact": ids.contact.text.strip(),
        }

        # validation
        if not data["zone"] or not data["depart"]:
            Snackbar(text="Zone et départ obligatoires").open()
            return

        if not data["contact"]:
            Snackbar(text="Contact obligatoire").open()
            return

        # add / edit
        if self.edit_index is not None:
            self.posts[self.edit_index] = data
            self.edit_index = None
            Snackbar(text="Post modifié ✅").open()
        else:
            self.posts.append(data)
            Snackbar(text="Course publiée 🚀").open()

        self.clear_fields()
        self.go_list()

    # ───────── AFFICHAGE ─────────
    def load_posts(self):
        box = self.root.get_screen("list").ids.posts_box
        box.clear_widgets()

        for i, post in enumerate(self.posts):
            card = MDCard(
                orientation="vertical",
                padding=dp(12),
                spacing=dp(6),
                size_hint_y=None,
                height=dp(170),
                radius=[12],
            )

            text = (
                f"📍 Zone: {post['zone']}\n"
                f"🚩 Départ: {post['depart']}\n"
                f"⏰ {post['debut']} - {post['fin']}\n"
                f"💰 {post['tarif']} Ar\n"
                f"🏍️ {post['moto']}\n"
                f"📞 {post['contact']}"
            )

            label = MDLabel(
                text=text,
                halign="left",
            )

            btn = MDFlatButton(
                text="Modifier",
                on_release=lambda x, idx=i: self.edit_post(idx)
            )

            card.add_widget(label)
            card.add_widget(btn)

            box.add_widget(card)

    # ───────── EDIT ─────────
    def edit_post(self, index):
        self.edit_index = index
        post = self.posts[index]
        ids = self.root.get_screen("post").ids

        for key in post:
            ids[key].text = post[key]

        self.root.current = "post"

    # ───────── CLEAR ─────────
    def clear_fields(self):
        ids = self.root.get_screen("post").ids
        for f in ids:
            ids[f].text = ""


TaxiMotoApp().run()