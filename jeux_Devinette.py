import random

petit =1
grand = 15

nombre = random.randint(petit, grand)

print(" ASSURER VOUS DENTRE UN NOMBRE VALABLE jai pense a un chiffre entre {} et{}".format(petit,grand))
x=0
while x!= nombre :
    x = int(input("deviner le chiffre"))
    if x< nombre:
        print("TROP PETIT")
    elif x > nombre:
        print("TROP GRAND")
    else:
        print("tu a gagner felicitation va sur le site pour la recompance")
