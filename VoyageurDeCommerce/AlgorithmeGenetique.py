import random

def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]
    return distance_totale


def calculer_fitness(solution, matrice_distances):
    distance = calculer_distance_totale(solution, matrice_distances)
    return 1 / distance if distance > 0 else 0




def selection_roulette(population, fitness_list):

    fitness_totale = sum(fitness_list)
    probabilites = [f / fitness_totale for f in fitness_list]

    cumul = []
    somme = 0
    for p in probabilites:
        somme += p
        cumul.append(somme)

    r = random.random()
    for i, c in enumerate(cumul):
        if r <= c:
            return population[i][:]
    return population[-1][:]


def selection_rang(population, fitness_list):
    population_triee = sorted(zip(population, fitness_list),key=lambda x: x[1], reverse=True)

    n = len(population)
    rangs = list(range(n, 0, -1))  # n, n-1, ..., 2, 1
    somme_rangs = sum(rangs)

    r = random.random() * somme_rangs
    cumul = 0
    for i, rang in enumerate(rangs):
        cumul += rang
        if r <= cumul:
            return population_triee[i][0][:]
    return population_triee[-1][0][:]



def croisement_simple(parent1, parent2):
    taille = len(parent1)
    point = random.randint(1, taille - 1)

    enfant = [None] * taille
    enfant[:point] = parent1[:point]

    pos = point
    for ville in parent2:
        if ville not in enfant:
            enfant[pos] = ville
            pos += 1

    return enfant


def croisement_double(parent1, parent2):
    taille = len(parent1)
    point1, point2 = sorted(random.sample(range(1, taille), 2))

    enfant = [None] * taille
    enfant[point1:point2] = parent1[point1:point2]

    pos = 0
    for ville in parent2:
        if ville not in enfant:
            while enfant[pos] is not None:
                pos += 1
            enfant[pos] = ville

    return enfant


def croisement_barycentrique(parent1, parent2):
    taille = len(parent1)
    point1, point2 = sorted(random.sample(range(taille), 2))

    enfant = [-1] * taille
    enfant[point1:point2] = parent1[point1:point2]

    for i in range(point1, point2):
        if parent2[i] not in enfant:
            pos = i
            while point1 <= pos < point2:
                pos = parent2.index(parent1[pos])
            enfant[pos] = parent2[i]

    for i in range(taille):
        if enfant[i] == -1:
            enfant[i] = parent2[i]

    return enfant


def croisement_uniforme(parent1, parent2):

    taille = len(parent1)
    enfant = [None] * taille

    masque = [random.randint(0, 1) for _ in range(taille)]

    for i in range(taille):
        if masque[i] == 1:
            enfant[i] = parent1[i]
    pos = 0
    for ville in parent2:
        if ville not in enfant:
            while enfant[pos] is not None:
                pos += 1
            enfant[pos] = ville

    return enfant



def mutation_echange(individu, taux_mutation):
    if random.random() < taux_mutation:
        i, j = random.sample(range(len(individu)), 2)
        individu[i], individu[j] = individu[j], individu[i]
    return individu


def mutation_inversion(individu, taux_mutation):
    if random.random() < taux_mutation:
        i, j = sorted(random.sample(range(len(individu)), 2))
        individu[i:j + 1] = reversed(individu[i:j + 1])
    return individu


def mutation_insertion(individu, taux_mutation):
    if random.random() < taux_mutation:
        i, j = random.sample(range(len(individu)), 2)
        ville = individu.pop(i)
        individu.insert(j, ville)
    return individu



def algorithme_genetique(matrice_distances,
                         taille_population=50,
                         nombre_generations=100,
                         taux_croisement=0.8,
                         taux_mutation=0.2,
                         type_selection='roulette',
                         type_croisement='simple',
                         type_mutation='echange'):

    nombre_villes = len(matrice_distances)

    population = []
    for _ in range(taille_population):
        individu = list(range(nombre_villes))
        random.shuffle(individu)
        population.append(individu)

    selection = selection_roulette if type_selection == 'roulette' else selection_rang

    croisements = {
        'simple': croisement_simple,
        'double': croisement_double,
        'barycentrique': croisement_barycentrique,
        'uniforme': croisement_uniforme
    }
    croisement = croisements[type_croisement]

    mutations = {
        'echange': mutation_echange,
        'inversion': mutation_inversion,
        'insertion': mutation_insertion
    }
    mutation = mutations[type_mutation]

    meilleure_solution = None
    meilleure_distance = float('inf')

    print(f"Sélection: {type_selection}, Croisement: {type_croisement}, Mutation: {type_mutation}\n")

    for generation in range(nombre_generations):
        fitness_list = [calculer_fitness(ind, matrice_distances) for ind in population]

        for i, ind in enumerate(population):
            distance = calculer_distance_totale(ind, matrice_distances)
            if distance < meilleure_distance:
                meilleure_distance = distance
                meilleure_solution = ind[:]

        nouvelle_population = []

        meilleur_idx = fitness_list.index(max(fitness_list))
        nouvelle_population.append(population[meilleur_idx][:])

        while len(nouvelle_population) < taille_population:
            # Sélection
            parent1 = selection(population, fitness_list)
            parent2 = selection(population, fitness_list)

            if random.random() < taux_croisement:
                enfant = croisement(parent1, parent2)
            else:
                enfant = parent1[:]

            enfant = mutation(enfant, taux_mutation)

            nouvelle_population.append(enfant)

        population = nouvelle_population

        if (generation + 1) % 10 == 0:
            print(f"Génération {generation + 1}: Meilleure distance = {meilleure_distance}")

    print(f"\nDistance finale: {meilleure_distance}")
    return meilleure_solution, meilleure_distance



matrice_distances = [
    [0, 2, 2, 7, 15, 2, 5, 7, 6, 5],
    [2, 0, 10, 4, 7, 3, 7, 15, 8, 2],
    [2, 10, 0, 1, 4, 3, 3, 4, 2, 3],
    [7, 4, 1, 0, 2, 15, 7, 7, 5, 4],
    [7, 10, 4, 2, 0, 7, 3, 2, 2, 7],
    [2, 3, 3, 7, 7, 0, 1, 7, 2, 10],
    [5, 7, 3, 7, 3, 1, 0, 2, 1, 3],
    [7, 7, 4, 7, 2, 7, 2, 0, 1, 10],
    [6, 8, 2, 5, 2, 2, 1, 1, 0, 15],
    [5, 2, 3, 4, 7, 10, 3, 10, 15, 0]
]

print("=== Résolution du TSP avec Algorithme Génétique ===\n")

configurations = [
    ('roulette', 'simple', 'echange'),
    ('rang', 'double', 'inversion'),
    ('roulette', 'barycentrique', 'insertion'),
    ('rang', 'uniforme', 'echange'),
]

print("Test de différentes configurations:\n")
for selection, croisement, mutation in configurations:
    print(f"\n--- Configuration: {selection}/{croisement}/{mutation} ---")
    solution, distance = algorithme_genetique(
        matrice_distances=matrice_distances,
        taille_population=50,
        nombre_generations=100,
        taux_croisement=0.8,
        taux_mutation=0.2,
        type_selection=selection,
        type_croisement=croisement,
        type_mutation=mutation
    )
    print(f"Solution: {solution}")
    print(f"Distance: {distance}\n")