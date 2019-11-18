nb_row = int(input("Nombre de ligne du plateau: "))
nb_col = int(input("Nombre de colonne du plateau: "))

col_display = ''
col_header_display = ' # |'

for y in range(0, nb_row):
    for x in range(0, nb_col):
        if y == 0:
            col_header_display += ' %s ' % x
        if x == 0:
            col_display += ' %s |' % y
        col_display += ' 0 '
    if y == 0:
        print(col_header_display)
        print('---+' + '---' * nb_col)
    print(col_display)
    col_display = ''


