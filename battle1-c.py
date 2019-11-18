# On demande la grandeur du plateau
nb_row = int(input("Nombre de ligne du plateau: "))
nb_col = int(input("Nombre de colonne du plateau: "))

# Creation du bateau 1
ship_1_length = 5
ship_1_x = 3
ship_1_y = 3
ship_1_xi = ship_1_x
ship_1_yi = ship_1_y
ship_1_length_i = 1
ship_1_orientation = 'h' # h = horizontal / v = vertical

# On test si le bateau peut tenir sur le plateau
msg_error_length = "Le bateau est trop grand pour tenir sur le plateau (ou le plateau est trop petit) !"
ship_error = False
if ship_1_orientation == 'h':
    if ship_1_length + ship_1_x > nb_col + 1:
        print(msg_error_length)
        ship_error = True

if ship_1_orientation == 'v':
    if ship_1_length + ship_1_y > nb_col + 1:
        print(msg_error_length)
        ship_error = True

# On créé le plateau
if not ship_error:
    col_display = col_header_display = ''

    print(' # | A  B  C  D  E  F  G  H  I  J')
    print('---+' + '---' * nb_col)

    for y in range(0, nb_row):
        for x in range(0, nb_col):

            # Préparation des en-tetes de lignes
            if x == 0:
                col_display = ' %s |' % y

            # on place le bateau sur le plateau
            if ship_1_xi - 1 == x and ship_1_yi - 1 == y:
                col_display += ' B '
                if ship_1_length_i < ship_1_length:
                    ship_1_xi += 1
                    ship_1_length_i += 1
            else:
                col_display += ' 0 '

        # on affiche les case du plateau (dont les entêtes de ligne)
        print(col_display)
