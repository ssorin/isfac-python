from random import randint

print("Trouver un nombre entre 0 et 10")

chiffre_a_trouver = randint(0, 10)
nb_chance = 5

# debug
print(chiffre_a_trouver)


# for i in range(nb_chance):
#     print("\n======================================================")
#     print(f"Il vous reste {nb_chance-i} chance(s) sur {nb_chance}")
#     proposition = int(input("Quelle est votre proposition de chiffre ?"))
#
#     if proposition == chiffre_a_trouver:
#         print(">>>> Bien joué ! Le chiffre à trouvé était ", chiffre_a_trouver)
#         break
#
#     elif proposition < chiffre_a_trouver:
#         print(">>>> Le chiffre à trouvé est supérieur à ", proposition)
#
#     elif proposition > chiffre_a_trouver:
#         print(">>>> Le chiffre à trouvé est inférieur à ", proposition)
#
#     if nb_chance == i+1:
#         print("Perdu !!")
#
# print("\nLe chiffre à trouvé était ", chiffre_a_trouver)


i = 0
while i < 5:
    print("\n======================================================")
    print(f"Il vous reste {nb_chance-i} chance(s) sur {nb_chance}")
    proposition = int(input("Quelle est votre proposition de chiffre ?"))

    if proposition == chiffre_a_trouver:
        print("\x1b[6;30;42m" + ">>>> Bien joué ! Le chiffre à trouvé était " + "\x1b[0m", chiffre_a_trouver)
        break

    elif proposition < chiffre_a_trouver:
        print("\x1b[6;30;42m" + ">>>> Le chiffre à trouvé est supérieur à " + "\x1b[0m", proposition)

    elif proposition > chiffre_a_trouver:
        print("\x1b[6;30;42m" + ">>>> Le chiffre à trouvé est inférieur à " + "\x1b[0m", proposition)

    if nb_chance == i+1:
        print("\x1b[6;30;42m" + f"Perdu !!" + "\x1b[0m")

    i += 1

print("\nLe chiffre à trouvé était ", chiffre_a_trouver)