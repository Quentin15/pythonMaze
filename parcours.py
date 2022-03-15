def resolution(adjacence,depart,arrivee):
    chemins = [] # Chemin reliant le point de départ au point d'arrivée
    if not(depart in adjacence.keys()) or not(arrivee in adjacence.keys()):
        return None
    pile = [(depart,[depart])] # Pile LIFO, dernier ajouté, premier retiré
    chemin = [] # Chemin reliant le point de départ au point en cours
    while len(pile) != 0:
        sommet,chemin = pile.pop() # Retire le dernier élément de la pile et le renvoie (tuple d'un sommet et d'un chemin)
        # Donc sommet = sommet en cours et chemin = chemin associé
        
        # Liste des sommets voisins avec la construction:
            # Pour chaque voisin du sommet, s'il ne se trouve pas dans le chemin, ajouté à la liste
        liste_nouveaux_sommets_voisins = [voisin for voisin in adjacence[sommet] if not(voisin in chemin)]
        
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                # L'un des voisins est le chemin d'arrivée, alors on arrête la boucle et on retourne le chemin complet
                chemins.append(chemin + [arrivee])
                return chemins
            # L'arrivée ne fait pas partie des voisins, donc on ajoute le voisin en question
            # ainsi que le chemin qui mène à lui
            pile.append((voisin,chemin + [voisin]))