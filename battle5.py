nb_row = nb_col = 10

# en-tête du tableau qui affiche le nom des colonnes
header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
header_separator = '\n---+' + '---' * nb_col

print(' # | ' + '  '.join(header) + header_separator)


for y in range(0, nb_row):
    for x in range(0, nb_col):
        # On affiche le numéro de ligne dans la première colonne
        if x == 0:
            col_display = ' %s |' % y
        col_display += ' 0 '

    print(col_display)









