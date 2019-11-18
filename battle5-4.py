nb_row = nb_col = 10

# Bateau [x, y, length, orientation]
boat = [[2, 3], [3, 3], [4, 3]]

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

for coord in boat:
    grid[coord[1]][coord[0]] = 'B'

for y in range(0, nb_row):
    row_number = ' %s | ' % y
    print(row_number + '  '.join(grid[y]))





