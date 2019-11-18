nb_row = int(input("Nombre de ligne du plateau: "))
nb_col = int(input("Nombre de colonne du plateau: "))

# en-tête du tableau qui affiche le nom des colonnes
print(' # | A  B  C  D  E  F  G  H  I  J')
print('---+' + '---' * nb_col)

for y in range(0, nb_row):
    for x in range(0, nb_col):
        # On affiche le numéro de ligne dans la première colonne
        if x == 0:
            col_display = ' %s |' % y
        col_display += ' 0 '

    print(col_display)






