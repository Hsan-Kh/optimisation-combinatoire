import streamlit as st
import random
import sys
import os

# Ajouter le chemin des modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'VoyageurDeCommerce'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OrdonnancementDesTaches'))
sys.path.append(os.path.dirname(__file__))

# Initialiser les variables
Tache = None
recherche_tabou_ordonnancement = None
recuit_simule_ordonnancement = None
algorithme_genetique_ordonnancement = None
tabu_search = None
recuit_simule_tsp = None
algorithme_genetique = None

# Import des problèmes et algorithmes
try:
    from OrdonnancementDesTaches.tache import Tache
    from OrdonnancementDesTaches.utils import afficher_ordonnancement, calculer_cout
    from OrdonnancementDesTaches.tabou import recherche_tabou_ordonnancement
    from OrdonnancementDesTaches.recuit_simule import recuit_simule_ordonnancement
    from OrdonnancementDesTaches.algo_genetique import algorithme_genetique_ordonnancement

    # Pour TSP
    from VoyageurDeCommerce.RechercheParTabou import tabu_search
    from VoyageurDeCommerce.RecuitSimule import recuit_simule as recuit_simule_tsp
    from VoyageurDeCommerce.AlgorithmeGenetique import algorithme_genetique

except ImportError as e:
    st.error(f"Erreur d'importation: {e}")
    st.stop()

# Configuration de la page
st.set_page_config(
    page_title="Optimisation Combinatoire",
    page_icon="🔬",
    layout="wide"
)

# Données par défaut
MATRICE_DISTANCES = [
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

TACHES = [
    Tache(0, duree=5, deadline=20, priorite=3),
    Tache(1, duree=3, deadline=10, priorite=5),
    Tache(2, duree=8, deadline=25, priorite=2),
    Tache(3, duree=4, deadline=15, priorite=4),
    Tache(4, duree=6, deadline=30, priorite=1),
    Tache(5, duree=2, deadline=8, priorite=5),
    Tache(6, duree=7, deadline=35, priorite=3),
    Tache(7, duree=5, deadline=18, priorite=4),
]


def calculer_retard_total(ordre, taches):
    temps_actuel = 0
    retard_total = 0
    for i in ordre:
        temps_actuel += taches[i].duree
        if taches[i].deadline is not None:
            retard = max(0, temps_actuel - taches[i].deadline)
            retard_total += retard
    return retard_total


def main():
    st.title("🔬 Interface de Simulation - Optimisation Combinatoire")

    # Sidebar pour la configuration
    st.sidebar.header("Configuration")

    # Sélection du problème
    probleme = st.sidebar.selectbox(
        "Sélection du Problème",
        ["Voyageur de Commerce", "Ordonnancement des Tâches"]
    )

    # Sélection de l'algorithme
    algorithme = st.sidebar.selectbox(
        "Algorithme",
        ["Recuit Simulé", "Recherche Tabou", "Algorithme Génétique"]
    )

    # Paramètres généraux
    st.sidebar.subheader("Paramètres Généraux")

    if algorithme == "Algorithme Génétique":
        iterations = st.sidebar.number_input("Nombre de générations", 10, 10000, 100)
    else:
        iterations = st.sidebar.number_input("Nombre d'itérations", 10, 10000, 1000)

    # Paramètres spécifiques selon l'algorithme
    st.sidebar.subheader("Paramètres Spécifiques")

    if algorithme == "Recuit Simulé":
        temperature = st.sidebar.number_input("Température initiale", 1, 1000, 100)
        taux_refroidissement = st.sidebar.slider("Taux de refroidissement", 0.900, 0.999, 0.995)

    elif algorithme == "Recherche Tabou":
        taille_tabou = st.sidebar.number_input("Taille liste tabou", 5, 200, 50)

    elif algorithme == "Algorithme Génétique":
        col1, col2 = st.sidebar.columns(2)
        with col1:
            taille_population = st.number_input("Taille population", 10, 500, 50)
            taux_croisement = st.slider("Taux croisement", 0.1, 1.0, 0.8)
        with col2:
            taux_mutation = st.slider("Taux mutation", 0.01, 0.5, 0.2)
            selection = st.selectbox("Sélection", ["roulette", "rang"])
            croisement = st.selectbox("Croisement", ["simple", "double", "barycentrique", "uniforme"])
            mutation = st.selectbox("Mutation", ["echange", "inversion", "insertion"])

    # Bouton d'exécution
    if st.sidebar.button("🚀 Lancer la Simulation", type="primary"):
        executer_simulation(probleme, algorithme, iterations, locals())

    # Affichage des données du problème
    st.header("Données du Problème")

    if probleme == "Voyageur de Commerce":
        st.subheader("Matrice des Distances")
        st.dataframe(MATRICE_DISTANCES, use_container_width=True)
        st.write(f"**Nombre de villes :** {len(MATRICE_DISTANCES)}")

    else:
        st.subheader("Liste des Tâches")
        for tache in TACHES:
            st.write(f"**{tache}** - Deadline: {tache.deadline}, Priorité: {tache.priorite}")


def executer_simulation(probleme, algorithme, iterations, params):
    st.header("Résultats de la Simulation")

    with st.spinner("Simulation en cours..."):
        try:
            if probleme == "Voyageur de Commerce":
                resultats = executer_tsp(algorithme, iterations, params)
                afficher_resultats_tsp(resultats, algorithme)
            else:
                resultats = executer_ordonnancement(algorithme, iterations, params)
                afficher_resultats_ordonnancement(resultats, algorithme)

        except Exception as e:
            st.error(f"Erreur lors de la simulation: {str(e)}")


def executer_tsp(algorithme, iterations, params):
    if algorithme == "Recuit Simulé":
        return recuit_simule_tsp(
            MATRICE_DISTANCES,
            iterations,
            params['temperature'],
            params['taux_refroidissement']
        )

    elif algorithme == "Recherche Tabou":
        return tabu_search(
            MATRICE_DISTANCES,
            iterations,
            params['taille_tabou']
        )

    elif algorithme == "Algorithme Génétique":
        return algorithme_genetique(
            MATRICE_DISTANCES,
            params['taille_population'],
            iterations,
            params['taux_croisement'],
            params['taux_mutation'],
            params['selection'],
            params['croisement'],
            params['mutation']
        )


def executer_ordonnancement(algorithme, iterations, params):
    if algorithme == "Recuit Simulé":
        return recuit_simule_ordonnancement(
            TACHES, iterations, params['temperature'], 0.1, params['taux_refroidissement']
        )

    elif algorithme == "Recherche Tabou":
        return recherche_tabou_ordonnancement(
            TACHES, iterations, params['taille_tabou']
        )

    elif algorithme == "Algorithme Génétique":
        return algorithme_genetique_ordonnancement(
            TACHES, params['taille_population'], iterations,
            params['taux_croisement'], params['taux_mutation']
        )


def afficher_resultats_tsp(resultats, algorithme):
    solution, distance = resultats

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Algorithme", algorithme)
    with col2:
        st.metric("Distance minimale", f"{distance:.2f}")
    with col3:
        st.metric("Nombre de villes", len(solution))

    st.subheader("Meilleure Solution")
    st.write(solution)

    # Visualisation simple du chemin
    st.subheader("Visualisation du Chemin")
    chemin = " → ".join([f"V{i}" for i in solution]) + f" → V{solution[0]}"
    st.info(chemin)


def afficher_resultats_ordonnancement(resultats, algorithme):
    solution, cout = resultats

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Algorithme", algorithme)
    with col2:
        st.metric("Coût total", f"{cout:.2f}")

    st.subheader("Meilleur Ordre d'Ordonnancement")
    st.write(solution)

    # Affichage détaillé de l'ordonnancement
    st.subheader("Détail de l'Ordonnancement")

    temps_actuel = 0
    for idx, tache_id in enumerate(solution):
        tache = TACHES[tache_id]
        temps_fin = temps_actuel + tache.duree

        col1, col2, col3, col4 = st.columns([1, 2, 2, 3])
        with col1:
            st.write(f"**Position {idx + 1}**")
        with col2:
            st.write(f"**{tache}**")
        with col3:
            st.write(f"Début: {temps_actuel} | Fin: {temps_fin}")
        with col4:
            if tache.deadline is not None:
                retard = max(0, temps_fin - tache.deadline)
                if retard > 0:
                    st.error(f"⚠ Retard: {retard} (deadline: {tache.deadline})")
                else:
                    st.success("✓ Dans les temps")

        # Barre de progression pour la durée
        duree_normalisee = (tache.duree / 40) * 100  # Normalisation pour l'affichage
        st.progress(min(duree_normalisee, 100), text=f"Durée: {tache.duree} unités")

        temps_actuel = temps_fin
        st.divider()

    # Résumé final
    makespan = temps_actuel
    retard_total = calculer_retard_total(solution, TACHES)

    st.subheader("Résumé Final")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Makespan total", makespan)
    with col2:
        st.metric("Retard total", retard_total)


if __name__ == "__main__":
    main()