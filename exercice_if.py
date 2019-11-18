from random import randint


print("Trouver un nombre entre 0 et 10")

proposition = int(input("Quelle est votre proposition de chiffre ?"))

chiffre_a_trouver = randint(0, 10)
print(chiffre_a_trouver)
rejouer = True

# 1ere chance
if proposition == chiffre_a_trouver:
    print("Bien joué ! Le chiffre à trouvé était ", chiffre_a_trouver)
    rejouer = False

elif proposition < chiffre_a_trouver:
    print("Le chiffre à trouvé est supérieur à ", proposition)

else:
    print("Le chiffre à trouvé est inférieur à ", proposition)


if rejouer:
    # 2nde chance
    proposition = int(input("2ème chance, quelle est votre proposition de chiffre ?"))

    if proposition == chiffre_a_trouver:
        print("Bien joué ! Le chiffre à trouvé était ", chiffre_a_trouver)
        rejouer = False

    elif proposition < chiffre_a_trouver:
        print("Le chiffre à trouvé est supérieur à ", proposition)

    else:
        print("Le chiffre à trouvé est inférieur à ", proposition)



if rejouer:
    # 3eme chance
    proposition = int(input("Dernière chance !! Quelle est votre proposition de chiffre ?"))

    if proposition == chiffre_a_trouver:
        print("Bien joué ! Le chiffre à trouvé était ", chiffre_a_trouver)

    else:
        print("Perdu !", chiffre_a_trouver)

print("Le chiffre à trouvé était ", chiffre_a_trouver)


