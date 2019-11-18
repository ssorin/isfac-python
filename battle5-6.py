import os

nb_row = nb_col = 10

# Bateau [x, y, length, orientation]
boats = []
boats.insert(0, [[2, 3], [3, 3], [4, 3]])
boats.insert(1, [[0, 2], [0, 3], [0, 4], [0, 5]])
boats.insert(2, [[8, 9], [9, 9]])

boats_touche = []
boats_touche.insert(0, [3, 0])
boats_touche.insert(1, [4, 0])
boats_touche.insert(2, [2, 0])
player_alive = 9

boats[2] = [[7, 8], [8, 8]]
boats[2].append([6, 8])

# en-tête du tableau qui affiche le nom des colonnes
header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
header_separator = '\n---+' + '---' * nb_col



# on construit une ligne de 10 colonnes
grid_col = []
for x in range(0, nb_col):
    grid_col.append('0')

# on construit tout le tableau, ligne par ligne
grid = []
for y in range(0, nb_row):
    grid.insert(y, grid_col[:])

for boat in boats:
    for coord in boat:
        grid[coord[1]][coord[0]] = 'B'


# test tir
tirs = []

    
tir_n = i = 0
while i < 1:
    x = int(input("tir x :"))
    y = int(input("tir y :"))

    tirs.insert(tir_n, [x, y])

    print(' # | ' + '  '.join(header) + header_separator)

    for tir in tirs:
        if not grid[tir[1]][tir[0]] in ('T', 'X'):
            if grid[tir[1]][tir[0]] == 'B':
                grid[tir[1]][tir[0]] = 'T'
                for boat in boats:
                    for coord in boat:
                        if coord[0] == tir[0] and coord[1] == tir[1]:
                            touche_boat_id = boats.index(boat)
            else:
                grid[tir[1]][tir[0]] = 'X'

    # Affichage du plateau
    for y in range(0, nb_row):
        row_number = ' %s | ' % y
        print(row_number + '  '.join(grid[y]))

    tir_n += 1

    # calcul si un bateau est touché / coulé
    print(touche_boat_id)
    if touche_boat_id is not None:
        boats_touche[touche_boat_id][1] += 1
        player_alive -= 1
        if boats_touche[touche_boat_id][0] == boats_touche[touche_boat_id][1]:
            print("Le bateau %s a été coulé !!" % touche_boat_id)
        else:
            print("Le bateau %s a été touché" % touche_boat_id)

        if player_alive == 0:
            print("fin de partie !")
            i = 2

    touche_boat_id = None
    os.system('clear')
