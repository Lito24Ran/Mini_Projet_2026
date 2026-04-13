from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:
    def get_publication(self, lieu, on_complite):
        url = f"http://127.0.0.1:8000/publication/get_search/{lieu}"
                
        def donne_recus(req, result):
            try:
                data = result
                print("Données reçues :", data)

                for item in data:
                    print(item["id"], item["heure_debut"], item["heure_fin"])
                ##Areter ici 
                if on_complite:
                    on_complite()

            except Exception as e:
                print("Erreur : ", e)
                
        req = UrlRequest(url,  on_success=donne_recus)