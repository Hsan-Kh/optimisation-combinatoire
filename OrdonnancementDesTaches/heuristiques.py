from OrdonnancementDesTaches.utils import calculer_cout


def ordonnancement_spt(taches):
#Shortest Processing Time - Ordre croissant des durées.

    ordre = sorted(range(len(taches)), key=lambda i: taches[i].duree)
    cout = calculer_cout(ordre, taches)
    print(f"\n SPT (Shortest Processing Time)")
    print(f"Coût: {cout:.2f}")
    return ordre, cout


def ordonnancement_edd(taches):
#Earliest Due Date - Ordre croissant des deadlines.

    ordre = sorted(range(len(taches)),
                   key=lambda i: taches[i].deadline if taches[i].deadline else float('inf'))
    cout = calculer_cout(ordre, taches)
    print(f"\n EDD (Earliest Due Date)")
    print(f"Coût: {cout:.2f}")
    return ordre, cout


def ordonnancement_priorite(taches):
#Ordonnancement par priorité décroissante.

    ordre = sorted(range(len(taches)), key=lambda i: taches[i].priorite, reverse=True)
    cout = calculer_cout(ordre, taches)
    print(f"\n Priorité (Ordre décroissant)")
    print(f"Coût: {cout:.2f}")
    return ordre, cout
