def calculer_makespan(ordre, taches):

    return sum(taches[i].duree for i in ordre)


def calculer_retard_total(ordre, taches):

    temps_actuel = 0
    retard_total = 0

    for i in ordre:
        temps_actuel += taches[i].duree
        if taches[i].deadline is not None:
            retard = max(0, temps_actuel - taches[i].deadline)
            retard_total += retard

    return retard_total


def calculer_cout(ordre, taches, poids_makespan=0.5, poids_retard=0.5):

    makespan = calculer_makespan(ordre, taches)
    retard = calculer_retard_total(ordre, taches)
    return poids_makespan * makespan + poids_retard * retard


def afficher_ordonnancement(ordre, taches):

    print("\n" + "=" * 60)
    print("ORDONNANCEMENT DES TÂCHES")
    print("=" * 60)

    temps_actuel = 0
    for idx, i in enumerate(ordre):
        tache = taches[i]
        temps_fin = temps_actuel + tache.duree

        barre = "█" * (tache.duree * 2)

        print(f"Position {idx + 1}: {tache} | Début: {temps_actuel:3d} | Fin: {temps_fin:3d} | {barre}")

        if tache.deadline is not None:
            retard = max(0, temps_fin - tache.deadline)
            if retard > 0:
                print(f"           ⚠  RETARD de {retard} unités (deadline: {tache.deadline})")

        temps_actuel = temps_fin

    print("=" * 60)
    print(f"Makespan total: {temps_actuel}")
    print(f"Retard total: {calculer_retard_total(ordre, taches)}")
    print("=" * 60 + "\n")

