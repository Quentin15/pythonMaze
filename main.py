import render as R
import prim as P
import graph as G

w = int(input("Entrer une largeur de labyrinthe.\nVotre réponse : "))
h = int(input("Entrer une hauteur de labyrinthe.\nVotre réponse : "))
grid = G.create_grid(w,h)
tree = P.prim(grid[0], grid[1])
maze = P.tree_to_graph(tree)[0]
R.show_cells_maze(maze)
R.show_maze(maze,w,h)