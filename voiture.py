
class Voiture: 
    def __init__(self,modele: str, marque: str, carburant: str, type: str, vitesse: int, acceleration: float): #ceci est le constructeur python
        self._marque = marque
        self._modele = modele
        self._carburant = carburant
        self._vitesse = vitesse
        self._type = type
        self._acceleration = acceleration#si il y a un underscore _, elles sont vues comme privées. il n'y a pas de définiton public ou privées en Python, ceci est une conventino
        self.set_vitesse(vitesse)
def __str__(self):
    return f"{self.marque} {self.modele} {self.carburant} {self.vitesse} {self.type} {self.acceleration}"

# getter
def get_vitesse(self) -> int:
    return self._vitesse

def get_marque(self) -> str:
    return self._marque

def get_type(self) -> str:

    return self._type

def get_acceleration(self)-> int:
    return self._acceleration

#setter
def set_vitesse(self, vitesse : int):
    if  type(vitesse) is not int:# on peut rajouter le type de valeur en mettant le type en paramètre
        raise Exception("ceci n'est pas le bon type de data!!!")
    elif vitesse > 500: 
        raise Exception("c est trop rapide!!!")
    self.vitesse = vitesse


    def accelerate(self):
        vitesse = self.get_vitesse()
        vitesse+=10
        self.set_vitesse(vitesse)
    
    def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -=20
        self.set_vitesse(vitesse)