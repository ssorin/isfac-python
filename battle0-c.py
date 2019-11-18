nb_row = int(input("Nombre de ligne du plateau: "))
nb_col = int(input("Nombre de colonne du plateau: "))

col_display = ''
col_header_display = ' # |'

for y in range(0, nb_row):
    for x in range(0, nb_col):

        # Préparation des en-tetes de lignes
        if x == 0:
            col_display += ' %s |' % y

        # Préparation des cases du plateau
        col_display += ' 0 '

    # Si on est sur la 1ere iteration, on affiche l'entête de colonne + le separateur de ligne en dessous
    if y == 0:
        print(' # | A  B  C  D  E  F  G  H  I  J')
        print('---+' + '---' * nb_col)

    # on affiche les case du plateau (dont les entêtes de ligne)
    print(col_display)
    col_display = ''


