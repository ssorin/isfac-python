nb_row = nb_col = 10

# en-tête du tableau qui affiche le nom des colonnes
header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
header_separator = '\n---+' + '---' * nb_col

print(' # | ' + '  '.join(header) + header_separator)


grid_col = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

grid = []
for y in range(0, nb_row):
    grid.insert(y, grid_col)

print(grid)





