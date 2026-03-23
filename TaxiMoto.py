class TaxiMoto:
    
    nom = ""
    diponibilite = False
    lieu = ""
    image = ""
    
    def __init__(self, nom, disponibilite, lieu, description):
        self.nom = nom
        self.disponibilite = disponibilite
        self.lieu = lieu 
        self.description = description
        
    def get_nom(self):
        return self.nom
    
    def get_dictionary(self):
        return {"nom" : self.nom , "disponible" : self.diponibilite, "lieu" : self.lieu, "description : " : self.description}