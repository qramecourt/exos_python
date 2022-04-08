import random

# counter = 0
# limit = 10
# while counter <= limit:  
#      print("tour:", counter)
#      counter += 1
        
# # ceci est une boucle while, 

# #reproduction d'une boucle do while
# counter = 0
# limit = 10
# while True:
#     #cette action se répète
#     print('do while', counter)
# #tirage de 3 nombres différents parmi 5
#     counter += 1 
#     if not (counter < limit):
#         break

#boucle for

# for counter in range(0, 10):
#     print('for python', counter)
# #boucle for avec une liste selon une méthode "sale"
# mots = ['bibi', 'bobo', 'bibu']
# for i in range(0, len(mots)):
#     print('mot:', mots[i])
# #la meme boucle mais selon une méthode recommandée
# for mot in mots:
#     print('mot(reco): ', mot)
# #version si l'on veur recuperer les index
# for i, mot in enumerate(mots):
#     print(f"mot(reco) {i}", mot)




# tirgae de 2 nombres parmi 5
numbers = []
#tirage 1
n = random.randint(1, 5)
# numbers.append(n)
# #second tirage

# while n in numbers:
#     n = random.randint(1, 5)

#     if n not in numbers:
#         break
# numbers.append(n)
#tirage 3
for i in range(0, 3):
    while True:
        n = random.randint(1, 5)
        if n not in numbers:
            numbers.append(n)
            break
    print(numbers)
    #ne renvoie pas les infos demandées, à corriger.


# print(numbers)
# print(n in numbers)

# for number in range (100, 1000):
#     print("number: ", number)

# #affichage de 0 a 10 uniquement multiple de 3 

# for multiple in range (0, 21, 3):
#     print("multiple of 3:", multiple)

# for decrement in range (10, 0, -1):
#     print("decrement: ", decrement)
