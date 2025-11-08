import random
from OrdonnancementDesTaches.utils import calculer_cout


def calculer_fitness_ordonnancement(ordre, taches):
    cout = calculer_cout(ordre, taches)
    return 1 / (cout + 1)


def croisement_ordre(parent1, parent2):
    taille = len(parent1)
    point1, point2 = sorted(random.sample(range(taille), 2))

    enfant = [None] * taille
    enfant[point1:point2] = parent1[point1:point2]

    pos = point2
    for tache in parent2[point2:] + parent2[:point2]:
        if tache not in enfant:
            enfant[pos % taille] = tache
            pos += 1

    return enfant


def mutation_ordonnancement(ordre, taux_mutation):
    if random.random() < taux_mutation:
        i, j = random.sample(range(len(ordre)), 2)
        ordre[i], ordre[j] = ordre[j], ordre[i]
    return ordre


def algorithme_genetique_ordonnancement(taches, taille_population=50,nombre_generations=100,taux_croisement=0.8,taux_mutation=0.2):

    print("\n ALGORITHME GÉNÉTIQUE")
    print("-" * 60)

    n_taches = len(taches)

    population = []
    for _ in range(taille_population):
        individu = list(range(n_taches))
        random.shuffle(individu)
        population.append(individu)

    meilleur_ordre = None
    meilleur_cout = float('inf')

    print(f"Population initiale: {taille_population} individus")

    for generation in range(nombre_generations):
        fitness_list = [calculer_fitness_ordonnancement(ind, taches) for ind in population]

        for ind in population:
            cout = calculer_cout(ind, taches)
            if cout < meilleur_cout:
                meilleur_cout = cout
                meilleur_ordre = ind[:]

        nouvelle_population = []

        meilleur_idx = fitness_list.index(max(fitness_list))
        nouvelle_population.append(population[meilleur_idx][:])

        while len(nouvelle_population) < taille_population:
            fitness_totale = sum(fitness_list)
            proba = [f / fitness_totale for f in fitness_list]

            parent1 = random.choices(population, weights=proba)[0]
            parent2 = random.choices(population, weights=proba)[0]

            if random.random() < taux_croisement:
                enfant = croisement_ordre(parent1, parent2)
            else:
                enfant = parent1[:]

            enfant = mutation_ordonnancement(enfant, taux_mutation)
            nouvelle_population.append(enfant)

        population = nouvelle_population

        if (generation + 1) % 20 == 0:
            print(f"Génération {generation + 1}: Meilleur coût = {meilleur_cout:.2f}")

    print(f"\nCoût final: {meilleur_cout:.2f}")
    return meilleur_ordre, meilleur_cout
