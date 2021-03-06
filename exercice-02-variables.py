# exercice-02-variables.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
number = 42
my_float = 1.61
my_name = "quentin Ramecourt"
is_morning = True
my_level = None

print("my " + my_name+ " and this a boolean with a golden number and my level in Python (for me) " + is_morning + " " + my_level)
# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez le valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
int = 2

my_float = 1.62
convert_in_into_float = float(int)
convert_float_into_integer = int(my_float)
round_int = int(round(my_float, 0))
round_float = round(my_float, 0)
print(int, my_float, convert_float_into_integer, convert_in_into_float, round_float, round_float)