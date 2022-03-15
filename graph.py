from random import Random
random = Random()

# Renvoie la liste d'adjacence et le dictionnaire
# de poids d'un graphe vide
def empty_graph():
    weights={}
    adjacence = {}
    return adjacence,weights

# Ajoute un nœud dans le graphe
def add_node(adjacence,node):
    if not(node in adjacence.keys()):
        adjacence[node] = []
       
# Ajoute un arc dans le graphe n1 -> n2 
def add_arc(n1,n2,adjacence):
    add_node(adjacence,n1)
    add_node(adjacence,n2)
    if not(n2 in adjacence[n1]):
        adjacence[n1].append(n2)
        
# Ajoute une arête dans le graphe n1 -- n2
# => n1 -> n2 et n2 -> n1   
def add_edge(n1,n2,adjacence):
    add_arc(n1,n2,adjacence)
    add_arc(n2,n1,adjacence)
    
# Vérifie arc entre u et v
def verify_arc(u,v,adjacence):
    return v in adjacence[u]

# Vérifie arête entre u et v
def verify_edge (u,v,adjacence):
    return verify_arc(u,v,adjacence) and verify_arc(v,u,adjacence)

# Renvoie liste des sommets
def nodes_copy(adjacence):
    return list(adjacence.keys())

# Renvoie liste des voisins d'un sommet
def node_successors(n,adjacence):
    return adjacence[n]

# Affecte le poids à un arc
def affect_arc_weight(u,v,adjacence,w,weights):
    if verify_arc(u,v,adjacence)==True:
        if u not in weights:
            weights[u]={}
        weights[u][v]=w

# Affecte le poids à une arête
def affect_edge_weight(u,v,adjacence,w,weights):
    affect_arc_weight(u,v,adjacence,w,weights)
    affect_arc_weight(v,u,adjacence,w,weights)

# Renvoie le poids d'un arc    
def arc_weight(u,v,weights):
    return weights[u][v]

# Ajoute un arc et lui affecte un poids
def edge(u,v,adjacence,w,weights):
    add_edge(u,v,adjacence)
    affect_edge_weight(u,v,adjacence,w,weights)
    
# Renvoie le dictionnaire des poids liés au graphe passé
def weights_from_graph(G):
    weights= dict()
    for node in G.keys():
        weights[node] = dict()
        for node_v in G.keys():
            if node_v in G[node]:
                weights[node][node_v]=1
            else:
                weights[node][node_v]=0
    return weights

# Crée un graphe de dimensions m*n et affecte ou non un biais
# "v" pour vertical, "h" pour horizontal, ou rien
def create_grid(m,n,sens="n"):
    if (m<=0 or n<=0):
        return ({},{})
    h,v=0,0
    if(sens == "v"):
        v=random.uniform(0,1)
    if(sens == "h"):
        h=random.uniform(0,1)
    graph=empty_graph()
    for i in range(m-1):
        for j in range(n-1):
            # Création d'une arête entre un sommet et son voisin au-dessus (poids random)
            edge((i,j),(i,j+1),graph[0],random.uniform(0,1)+h,graph[1])
            # Création d'une arête entre un sommet et son voisin de droite (poids random)
            edge((i,j),(i+1,j),graph[0],random.uniform(0,1)+v,graph[1])
    for i in range(m-1):
        # Création d'une arête entre un sommet de la dernière ligne (en haut) et son voisin de droite
        edge((i,n-1),(i+1,n-1),graph[0],random.uniform(0,1),graph[1])
    for j in range (n-1):
        # Création d'une arête entre un sommet de la dernière colonne (à droite) et son voisin au-dessus
        edge((m-1,j),(m-1,j+1),graph[0],random.uniform(0,1),graph[1])
    return graph


    
    