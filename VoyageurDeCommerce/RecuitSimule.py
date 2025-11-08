import random
import math


def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]
    return distance_totale


def generer_ville(solution):
    ville = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    ville[i], ville[j] = ville[j], ville[i]
    return ville


def recuit_simule(matrice_distances, nombre_iterations, temperature_initiale, taux_refroidissement):

    nombre_villes = len(matrice_distances)

    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)

    meilleure_solution = solution_actuelle[:]
    meilleure_distance = calculer_distance_totale(solution_actuelle, matrice_distances)

    distance_actuelle = meilleure_distance

    temperature = temperature_initiale

    print(f"Distance initiale: {distance_actuelle}")

    for iteration in range(nombre_iterations):

        ville = generer_ville(solution_actuelle)
        distance_ville = calculer_distance_totale(ville, matrice_distances)

        delta = distance_ville - distance_actuelle

        if delta < 0:
            solution_actuelle = ville
            distance_actuelle = distance_ville

            if distance_actuelle < meilleure_distance:
                meilleure_solution = solution_actuelle[:]
                meilleure_distance = distance_actuelle
        else:
            probabilite = math.exp(-delta / temperature)
            if random.random() < probabilite:
                solution_actuelle = ville
                distance_actuelle = distance_ville

        temperature *= taux_refroidissement

        if (iteration + 1) % 100 == 0:
            print(f"Itération {iteration + 1}, Température: {temperature:.4f}, "
                  f"Distance actuelle: {distance_actuelle}, "
                  f"Meilleure distance: {meilleure_distance}")

    print(f"\nDistance minimale trouvée: {meilleure_distance}")
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

print("=== Résolution du TSP avec Recuit Simulé ===\n")

meilleure_solution, meilleure_distance = recuit_simule(
    matrice_distances=matrice_distances,
    nombre_iterations=1000,
    temperature_initiale=50,
    taux_refroidissement=0.995
)

print(f"\nMeilleure solution trouvée (Recuit Simulé): {meilleure_solution}")
print(f"Distance minimale: {meilleure_distance}")