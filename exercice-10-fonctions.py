# exercice-10-fonctions.py

# exo 10.1
# Créer une fonction nommée `my_sum()` qui :
# - prend deux paramètres
# - additionne ces deux paramètres
# - renvoit le résultat
# Appelez la fonction et affichez le résultat

# réponse 10.1
def my_sum(a, b):
    return a +b
print(my_sum(1, 1))

# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait `b` de `a`
# - renvoit le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2
def my_diff(a, b):
    return b - a
# exo 10.3

# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoit `oui` si le booléen est égal à True
# - renvoit `non` si le booléen est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3
def oui_non():
    bool = True
    if bool == True:
        return 'oui'
    else:
        return 'non'
# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit True si `a` est plus grand que `b`
# - renvoit False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
def is_greater():
    a = 1
    b = 2
    if (a > b): 
        return True
    else: 
        return False
# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit 1 si `a` est plus grand que `b`
# - renvoit -1 si `a` est plus petit que `b`
# - renvoit 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare():
    a = 1.5
    b = 1.6
    if (a > b):
        return 1
    elif(a < b):
        return -1
    else:
        return 0

print(compare())

# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
def miles_to_meters():
    a= 10
    return a * 1609.344

def meters_to_miles():
    a = 1
    return a / 1609.344

print(meters_to_miles)
print(miles_to_meters)
# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoit le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7
def compute_tax(price, tax_type):
    if (tax_type == 1):
        return 1.021 * price
    elif (tax_type == 2):
        return 1.055 * price
    elif (tax_type == 3):
        return 1.1 * price
    else :
        return 1.2 * price


tax1 = compute_tax(100, 1)
tax2 = compute_tax(100, 2)
tax3 = compute_tax(100, 3)
tax4 = compute_tax(100, 4)
print(tax1, tax2, tax3, tax4)