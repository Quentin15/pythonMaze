import graph


def prim(adjacence,weights): 
    Cost={}
    Parent={}
    for v in adjacence:
        Cost[v]=float("inf")
        Parent[v]=None
    Q = graph.nodes_copy(adjacence)
    while Q != []:
        print(Cost)
        node_min = minimal_cost(Q,Cost)
        Q.remove(node_min)
        for v in graph.node_successors(node_min,adjacence):
            if v in Q and weights[node_min][v]<Cost[v]:
                Cost[v] = weights[node_min][v]
                Parent[v] = node_min
    print(Parent)
    return Parent

def minimal_cost(Q,Cost):
    # Parcourir Q et renvoyer le noeud avec C minimal
    node_min = Q[0]
    cost_min = Cost[node_min]
    for node in Q:
        print("node",node,"coût",Cost[node])
        if Cost[node]==float("inf"):
            break
        if Cost[node]<= cost_min:
            node_min = node
            cost_min = Cost[node_min]
    print(node_min)
    return node_min


def tree_to_graph(T):
    G = graph.empty_graph()
    for v in T.keys():
        # Parcours de chaque sommet
        if(T[v]!=None):
            # Si le sommet a un parent alors on ajoute une arête
            # entre le sommet et son parent
            u = T[v]
            graph.edge(v,u,G[0],1,G[1])
    return G



