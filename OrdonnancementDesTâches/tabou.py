import random
from collections import deque
from utils import calculer_cout


def generer_voisins_ordonnancement(ordre):
    voisins = []
    for i in range(len(ordre) - 1):
        voisin = ordre[:]
        voisin[i], voisin[i + 1] = voisin[i + 1], voisin[i]
        voisins.append(voisin)
    return voisins


def recherche_tabou_ordonnancement(taches, nombre_iterations=100, taille_tabu=20):

    print("\n RECHERCHE TABOU")
    print("-" * 60)

    ordre_actuel = list(range(len(taches)))
    random.shuffle(ordre_actuel)

    meilleur_ordre = ordre_actuel[:]
    meilleur_cout = calculer_cout(meilleur_ordre, taches)

    liste_tabu = deque(maxlen=taille_tabu)

    print(f"Coût initial: {meilleur_cout:.2f}")

    for iteration in range(nombre_iterations):
        voisins = generer_voisins_ordonnancement(ordre_actuel)
        voisins = [v for v in voisins if tuple(v) not in liste_tabu]

        if not voisins:
            break

        meilleur_voisin = min(voisins, key=lambda x: calculer_cout(x, taches))
        ordre_actuel = meilleur_voisin
        liste_tabu.append(tuple(ordre_actuel))

        cout_actuel = calculer_cout(ordre_actuel, taches)

        if cout_actuel < meilleur_cout:
            meilleur_ordre = ordre_actuel[:]
            meilleur_cout = cout_actuel
            print(f"Itération {iteration + 1}: Nouveau meilleur coût = {meilleur_cout:.2f}")

    print(f"\nCoût final: {meilleur_cout:.2f}")
    return meilleur_ordre, meilleur_cout