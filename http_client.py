from kivy.network.urlrequest import UrlRequest
import json
import urllib
import base64

class HttpClient:
    
    def get_publication(self, lieu, on_complite):
        url = f"http://127.0.0.1:8000/publication/get_search/{lieu}"
                
        def donne_recus(req, result):
            try:
                data = result
                print("Données reçues :", data)
                container_de_donne = []
                
                for item in data:
                    print(item["id"], item["nom_personne"])
                    container_de_donne.append(item)
                print("tableau container de donne : " , container_de_donne)
                ##Areter ici 
                if on_complite:
                    on_complite(container_de_donne)

            except Exception as e:
                print("Erreur : ", e)
                
        req = UrlRequest(url,  on_success=donne_recus)
        
    def creation_publication(self, nom, lieu, lat, lon, heure_pub, tarif, contact, description):

        url = "http://127.0.0.1:8000/publication/createpub/"

        params = {
            "nom_personne": nom,
            "lieu_nom": lieu,   
            "latitude": float(lat) if lat else 0.0,   # ✅ conversion sûre
            "longitude": float(lon) if lon else 0.0,  # ✅ conversion sûre
            "heure_publication": str(heure_pub), 
            "tarif": tarif,
            "contacte": contact,
            "description": description
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
            
        # print("params:", params)
        # print("types:", {k: type(v) for k, v in params.items()})
        
        UrlRequest(
            url,
            on_success=success,
            on_failure=failure,
            req_body=json.dumps(params),
            req_headers=headers,
            method='POST'
        )
        

    def demande_de_publication(self, photo_facture, photo_assurance):
        url = "http://127.0.0.1:8000/demande/demande/"

        # Lire et encoder les fichiers
        with open(photo_facture, 'rb') as f1:
            data_facture = base64.b64encode(f1.read()).decode('utf-8')
        
        with open(photo_assurance, 'rb') as f2:
            data_assurance = base64.b64encode(f2.read()).decode('utf-8')

        # Construire le body en multipart/form-data (boundary)
        boundary = '----FormBoundary7MA4YWxkTrZu0gW'
        
        def encode_file(name, filepath, data_b64):
            filename = filepath.split('\\')[-1]
            ext = filename.split('.')[-1]
            mime = f'image/{ext}'
            file_bytes = base64.b64decode(data_b64)
            part = (
                f'--{boundary}\r\n'
                f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'
                f'Content-Type: {mime}\r\n\r\n'
            ).encode('utf-8') + file_bytes + b'\r\n'
            return part

        body = (
            encode_file('file', photo_facture, data_facture) +
            encode_file('file2', photo_assurance, data_assurance) +
            f'--{boundary}--\r\n'.encode('utf-8')
        )

        headers = {
            'Content-Type': f'multipart/form-data; boundary={boundary}',
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
            req_body=body,
            req_headers=headers,
            method='POST'
        )
        
    def demande_approuver(self, callback):
        url = "http://127.0.0.1:8000/demande/demandeApprouver"

        def success(req, result):
            print("✅ Données reçues avec succès")
            print(result)
            approuvee = len(result) > 0
            callback(approuvee)

        def failure(req, result):
            print("❌ Échec de la récupération")
            print(result)
            callback(False)

        UrlRequest(
            url,
            on_success=success,
            on_failure=failure,
            method='GET'
        )
        