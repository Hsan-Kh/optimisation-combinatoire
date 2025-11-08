import random
import math
from utils import calculer_cout


def recuit_simule_ordonnancement(taches, nombre_iterations=1000,temp_init=100, temp_final=0.1, alpha=0.995):

    print("\n RECUIT SIMULÉ")
    print("-" * 60)

    ordre_actuel = list(range(len(taches)))
    random.shuffle(ordre_actuel)
    cout_actuel = calculer_cout(ordre_actuel, taches)

    meilleur_ordre = ordre_actuel[:]
    meilleur_cout = cout_actuel

    temperature = temp_init

    print(f"Coût initial: {meilleur_cout:.2f}")

    iteration = 0
    while temperature > temp_final and iteration < nombre_iterations:
        voisin = ordre_actuel[:]
        i, j = random.sample(range(len(voisin)), 2)
        voisin[i], voisin[j] = voisin[j], voisin[i]

        cout_voisin = calculer_cout(voisin, taches)
        delta = cout_voisin - cout_actuel

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            ordre_actuel = voisin
            cout_actuel = cout_voisin

            if cout_actuel < meilleur_cout:
                meilleur_ordre = ordre_actuel[:]
                meilleur_cout = cout_actuel
                print(f"Itération {iteration + 1}: Nouveau meilleur coût = {meilleur_cout:.2f}")

        temperature *= alpha
        iteration += 1

    print(f"\nCoût final: {meilleur_cout:.2f}")
    return meilleur_ordre, meilleur_cout
