
scores = [433, 562, 574, 800, 953]
n = len(scores) 

total = 0#j'initialise l'accumulateur. en contexte pro, on utilise totalt = sum(score) mais 

for score in scores:
    total += score
    print(total)#note: penser a enlever les print lors des test

average = total / n
print(average)

def int_average(numbers: list) -> int:
    pass #sert a plein de trucs, c'est notamment un repère pour un autre dev 

