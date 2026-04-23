from kivy.network.urlrequest import UrlRequest
import json
import urllib

class HttpClient:
    
    def get_publication(self, lieu, on_complite):
        url = f"http://127.0.0.1:8000/publication/get_search/{lieu}"
                
        def donne_recus(req, result):
            try:
                data = result
                print("Données reçues :", data)
                container_de_donne = []
                
                for item in data:
                    print(item["id"], item["heure_debut"])
                    container_de_donne.append(item)
                print("tableau container de donne : " , container_de_donne)
                ##Areter ici 
                if on_complite:
                    on_complite(container_de_donne)

            except Exception as e:
                print("Erreur : ", e)
                
        req = UrlRequest(url,  on_success=donne_recus)
        
    def creation_publication(self, heure_depart, heure_fin, tarif, moto, contacte, lieu):

        url = "http://127.0.0.1:8000/publication/createpub/"

        params = {
                'heure_debut': heure_depart,
                'heure_fin': heure_fin,
                'tarif': tarif,
                'moto': moto,
                'contacte': contacte,
                'lieu': lieu
        }

        headers = {
                'Content-type': 'application/json'
        }

        def success(req, result):
            print("✅ Données envoyées avec succès")
            print(result)

        def failure(req, result):
            print("❌ Échec de l'envoi")
            print(result)

        UrlRequest(
            url,
            on_success=success,
            on_failure=failure,
            req_body=json.dumps(params),
            req_headers=headers,
            method='POST'
        )
        
    def demande_de_publication(self):
        pass