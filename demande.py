from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from plyer import filechooser
##Il faut installer pyler avec : pip install plyer

Builder.load_file('demande.kv')

class DemandePublication(Screen):

    def choisir_fichier_1(self):
        filechooser.open_file(
            on_selection=lambda x: self.charger_fichier(x, "1"),
            filters=["*.png", "*.jpg", "*.pdf"]
        )

    def choisir_fichier_2(self):
        filechooser.open_file(
            on_selection=lambda x: self.charger_fichier(x, "2"),
            filters=["*.png", "*.jpg", "*.pdf"]
        )

    def charger_fichier(self, selection, numero):
        if selection:
            nom = selection[0].split("\\")[-1]  
            if numero == "1":
                self.ids.nom_fichier_1.text = nom
            else:
                self.ids.nom_fichier_2.text = nom

    def demander(self):
        fichier_1 = self.ids.nom_fichier_1.text
        fichier_2 = self.ids.nom_fichier_2.text

        if fichier_1 == "Aucun fichier choisi":
            print("❌ Fichier 1 manquant")
            return

        if fichier_2 == "Aucun fichier choisi":
            print("❌ Fichier 2 manquant")
            return

        print(f"✅ Demande envoyée : {fichier_1}, {fichier_2}")