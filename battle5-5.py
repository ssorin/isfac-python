nb_row = nb_col = 10

# Bateau [x, y, length, orientation]
boats = []
boats.insert(0, [[2, 3], [3, 3], [4, 3]])
boats.insert(1, [[0, 2], [0, 3], [0, 4], [0, 5]])
boats.insert(2, [[8, 9], [9, 9]])

boats[2] = [[7, 8], [8, 8]]
boats[2].append([6, 8])

# en-tête du tableau qui affiche le nom des colonnes
header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
header_separator = '\n---+' + '---' * nb_col

print(' # | ' + '  '.join(header) + header_separator)

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
tirs.insert(0, [0, 0])
tirs.insert(1, [2, 3])
tirs.insert(2, [3, 3])

for tir in tirs:
    if grid[tir[1]][tir[0]] == 'B':
        grid[tir[1]][tir[0]] = 'T'
    else:
        grid[tir[1]][tir[0]] = 'X'

# Affichage du plateau
for y in range(0, nb_row):
    row_number = ' %s | ' % y
    print(row_number + '  '.join(grid[y]))

