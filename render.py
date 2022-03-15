# Imports
import matplotlib.pyplot as plot
from random import Random
import graph
import prim as p
import parcours
random = Random()


# Ajoute un segment entre deux points t1 et t2
def add_segment(t1,t2,color):
    (x1,y1)=t1
    (x2,y2)=t2
    plot.gca().add_line(plot.Line2D((x1,x2),(y1,y2),color = color,linewidth=1))

# Permet d'être sûrs de bien cadrer notre diagramme
def show_diagramme():
    plot.axis('scaled')
    plot.show()

# Affiche graphiquement la grille (contour)
def show_graph(adjacence):
    corners = graph.nodes_copy(adjacence) # Récupère les coins de la grille
    for corner in corners: # Element clé composé d'un tuple de coordonnées de deux points
        for successor in graph.node_successors(corner, adjacence): # Chaque successeur du sommet
            add_segment(corner,successor,"blue")
    show_diagramme()

# Retourne le graph des coins de la grille
def grid(width, height):
    w,h = width-0.5,height-0.5
    G = graph.empty_graph() # Graphe vide
    adjacence = G[0]
    # Coordonnées des coins de la grille
    bg = (-0.5,-0.5) # Bas gauche
    hg = (-0.5,h) # Haut gauche
    bd = (w,-0.5) # Bas droit
    hd = (w,h) # Haut droit
    corners = [bg,bd,hd,hg,bg]
    # Ajout des nœuds et arêtes dans le graphe et des poids
    for i in range(len(corners)-1):
        c1,c2 = corners[i],corners[i+1]
        # Crée l'arête et affecte le poids
        graph.add_edge(c1, c2, adjacence)  
    return(adjacence)
    
# Ajoute un segment entre deux cases (deux coordonnées)
def show_wall_between_tuples(t1,t2):
    # Coordonnées des points t1 et t2
    (x1,y1)=t1
    (x2,y2)=t2
    # Coordonnées moyennes en x et y
    x_diff = (x1 + x2)/2
    y_diff = (y1 + y2)/2
    if(y1==y2): # Deux cellules ont même ordonnée (à côté)
        add_segment((x_diff,y1-0.5),(x_diff,y1+0.5), "blue")
    elif(x1==x2): # Deux cellules ont même abscisse (l'une sous l'autre)
        add_segment((x1-0.5,y_diff),(x1+0.5,y_diff), "blue")

        
# Renvoie la liste des points adjacents du point passé en paramètre séparés par un "mur"
def list_tuples_wall(t1, adjacence):
    list_tuples=[]
    # Condition pour avoir un mur
    def wall_condition(t1,t2):
        condition = (
            t2 != t1 and # t1 != t2
            (
                #t1 et t2 doivent avoir la même coordonnée x et doivent être adjacents en y
                t1[0]==t2[0] and (t1[1]==t2[1]+1 or t1[1]==t2[1]-1)
                or 
                #t1 et t2 doivent avoir la même coordonnée y et doivent être adjacents en x
                t1[1]==t2[1] and (t1[0]==t2[0]+1 or t1[0]==t2[0]-1)
            )
        )
        return(condition)
    
    for t2 in graph.nodes_copy(adjacence): # Parcours des clés du graphe
        if(t2 not in adjacence[t1] and wall_condition(t1, t2)):
            # Liste des tuples différents de t1 et qui ne sont pas voisins
            list_tuples.append(t2)
    return(list_tuples) # Liste des sommets adjacents qui ne sont pas voisins

# Affiche graphiquement la cellule d'un tuple
def show_cell_tuple(adjacence,t1):
    # Pour chaque sommet adjacent qui n'est pas voisin avec t1
    for t2 in list_tuples_wall(t1,adjacence):
        show_wall_between_tuples(t1,t2)

# Affiche graphiquement les cellules du graphe
def show_cells_maze(adjacence):
    for t in graph.nodes_copy(adjacence):
        show_cell_tuple(adjacence, t)
    # Récupère le sommet de coordonnées max (celui en haut à droite)
    max_node = (max(adjacence)[0],max(adjacence)[1])
    show_graph(grid(max_node[0]+1,max_node[1]+1))
    
# Affiche le labyrinthe et sa résolution
def show_maze(adjacence,w,h):
    if adjacence == {}:
        print("Dimensions du graphe invalides.")
        return()
    chemin = parcours.resolution(adjacence, (w-1,h-1), (0,0))
    # Parcourt de chaque sommet composant le chemin de solution
    for i in range(len(chemin[0])-1):
        add_segment(chemin[0][i+1], chemin[0][i], "red")
    show_cells_maze(adjacence)
