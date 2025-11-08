from OrdonnancementDesTaches.tache import Tache
from OrdonnancementDesTaches.utils import afficher_ordonnancement
from tabou import recherche_tabou_ordonnancement
from recuit_simule import recuit_simule_ordonnancement
from algo_genetique import algorithme_genetique_ordonnancement
from heuristiques import ordonnancement_spt, ordonnancement_edd, ordonnancement_priorite


def main():

    taches = [
        Tache(0, duree=5, deadline=20, priorite=3),
        Tache(1, duree=3, deadline=10, priorite=5),
        Tache(2, duree=8, deadline=25, priorite=2),
        Tache(3, duree=4, deadline=15, priorite=4),
        Tache(4, duree=6, deadline=30, priorite=1),
        Tache(5, duree=2, deadline=8, priorite=5),
        Tache(6, duree=7, deadline=35, priorite=3),
        Tache(7, duree=5, deadline=18, priorite=4),
    ]

    print("\n" + "=" * 60)
    print("PROBLÈME D'ORDONNANCEMENT DES TÂCHES")
    print("=" * 60)
    print(f"Nombre de tâches: {len(taches)}")
    print("\nTâches:")
    for t in taches:
        print(f"  {t} - Deadline: {t.deadline}, Priorité: {t.priorite}")

    # Heuristiques classiques
    ordre_spt, cout_spt = ordonnancement_spt(taches)
    ordre_edd, cout_edd = ordonnancement_edd(taches)
    ordre_priorite, cout_priorite = ordonnancement_priorite(taches)

    # Métaheuristiques
    ordre_tabou, cout_tabou = recherche_tabou_ordonnancement(taches, nombre_iterations=200)
    ordre_recuit, cout_recuit = recuit_simule_ordonnancement(taches, nombre_iterations=1000)
    ordre_genetique, cout_genetique = algorithme_genetique_ordonnancement(taches, nombre_generations=100)

    print("\n" + "=" * 60)
    print("COMPARAISON DES ALGORITHMES")
    print("=" * 60)
    resultats = [
        ("SPT (Heuristique)", cout_spt, ordre_spt),
        ("EDD (Heuristique)", cout_edd, ordre_edd),
        ("Priorité (Heuristique)", cout_priorite, ordre_priorite),
        ("Recherche Tabou", cout_tabou, ordre_tabou),
        ("Recuit Simulé", cout_recuit, ordre_recuit),
        ("Algorithme Voyageur", cout_genetique, ordre_genetique),
    ]

    resultats.sort(key=lambda x: x[1])

    for i, (nom, cout, ordre) in enumerate(resultats, 1):
        print(f"{i}. {nom:25s} | Coût: {cout:8.2f}")

    meilleur_nom, meilleur_cout, meilleur_ordre = resultats[0]
    print(f"\n MEILLEUR ALGORITHME: {meilleur_nom}")
    afficher_ordonnancement(meilleur_ordre, taches)


if __name__ == "__main__":
    main()