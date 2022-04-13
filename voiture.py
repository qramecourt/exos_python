from vehicule import Vehicule

class Voiture(Vehicule): 
    _speedup  = 20
    def __init__(self,modele: str, marque: str, carburant: str, type: str, vitesse: int, acceleration: float): #ceci est le constructeur python
        super().__init__(modele, marque, carburant, type, vitesse, acceleration)
        self._type = type
        self._acceleration = acceleration#si il y a un underscore _, elles sont vues comme privées. il n'y a pas de définiton public ou privées en Python, ceci est une conventino
        self.set_vitesse(vitesse)
    def __str__(self):
        return super().__str__() + f"{self.type}"

    # getter
    def get_type(self) -> str:

        return self._type


    
    def accelerate(self):
        vitesse = self.get_vitesse()
        vitesse+=10
        self.set_vitesse(vitesse)
    
    def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -=20
        self.set_vitesse(vitesse)