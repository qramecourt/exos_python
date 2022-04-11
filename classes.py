from voiture import Voiture


v1 = Voiture("regera", "koenigsegg", "essence", "hypercar", 450, 1.8 )
print(v1._marque,v1._modele, v1._carburant, v1._type, v1._vitesse, v1._acceleration)
print(v1._vitesse)
v1.vitesse = 451
print(v1._vitesse)
#v1 affiche le chemin pour accéder a la classe par défaut.
v2 = Voiture("laFerrari", "fearraari", "essence", "supercar", "très vite", 2.0)
print(v2._vitesse)

