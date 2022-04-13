from vehicule import Vehicule

class Camion(Vehicule):
    def __init__(self,modele: str, marque: str, carburant: str, type: str, vitesse: int, acceleration: float, ptac: float): #ceci est le constructeur python
        super().__init__(modele, marque, carburant, type, vitesse, acceleration)
        self.set_ptac(ptac)#il faut utiliser le setter si on doit vérifier 
    def __str__(self):
        return super().__str__() + f"{self._ptac}"

    def get_ptac(self) -> float:
        return self._ptac
    
        

    def set_ptac(self, ptac: float):
        if type(ptac) != float:
            raise Exception("le ptac est un poids à virgule")
        self._ptac = ptac


