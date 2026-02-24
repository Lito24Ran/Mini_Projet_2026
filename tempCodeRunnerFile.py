        
        if self.i >= 100:
            Clock.unschedule(self.loader)
            print("Chargement terminé!")
            