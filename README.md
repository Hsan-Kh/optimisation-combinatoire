# 🧠 Optimisation Combinatoire - TSP & Ordonnancement

Interface de simulation unifiée pour résoudre le problème du voyageur de commerce (TSP) et le problème d'ordonnancement des tâches avec différentes métaheuristiques.

## 📋 Description du Projet

Ce projet implémente trois algorithmes d'optimisation pour résoudre deux problèmes classiques d'optimisation combinatoire :

### Problèmes Résolus
- **🗺️ Voyageur de Commerce (TSP)** : Trouver le plus court chemin visitant toutes les villes
- **⏰ Ordonnancement des Tâches** : Ordonnancer des tâches avec deadlines et priorités

### Algorithmes Implémentés
- **Recherche Tabou**
- **Recuit Simulé** 
- **Algorithme Génétique**

## 🎯 Problèmes

### 🗺️ Problème du Voyageur de Commerce
Le voyageur de commerce doit visiter un ensemble de villes exactement une fois et revenir à son point de départ, en minimisant la distance totale parcourue.

**Instance du problème :**
- **Nombre de villes** : 10 (configurable)
- **Matrice de distances** : n×n (distances symétriques)

### ⏰ Problème d'Ordonnancement des Tâches
Ordonnancer un ensemble de tâches avec différentes durées, deadlines et priorités pour minimiser le makespan et les retards.

**Fonctions objectif :**
- `calculer_makespan()` : Durée totale de l'ordonnancement
- `calculer_retard_total()` : Somme des retards par rapport aux deadlines
- `calculer_cout()` : Combinaison pondérée des deux critères

## 🚀 Interface de Simulation

### Application Streamlit
Une interface web interactive déployable sur Streamlit Cloud.

**Fonctionnalités :**
- Sélection interactive du problème (TSP ou Ordonnancement)
- Génération aléatoire de données
- Configuration dynamique des paramètres d'algorithmes
- Visualisation des résultats en temps réel

## 🔧 Algorithmes et Paramètres

### Recherche Tabou
**Principe :** Évite les cycles en mémorisant les solutions récentes dans une liste tabou.

**Paramètres :**
- `nombre_iterations` : Nombre d'itérations
- `taille_tabu` : Taille de la liste tabou

### Recuit Simulé
**Principe :** Accepte probabilistiquement des solutions moins bonnes pour échapper aux minima locaux.

**Paramètres :**
- `temperature_initiale` : Niveau d'exploration initial
- `taux_refroidissement` : Vitesse de convergence
- `nombre_iterations` : Nombre d'itérations

### Algorithme Génétique
**Principe :** Évolution d'une population de solutions par sélection, croisement et mutation.

**Paramètres :**
- `taille_population` : Nombre d'individus
- `nombre_generations` : Nombre de générations
- `taux_croisement` : Probabilité de croisement
- `taux_mutation` : Probabilité de mutation

**Méthodes de sélection :**
- `roulette` : Probabilité proportionnelle au fitness
- `rang` : Probabilité basée sur le classement

**Méthodes de croisement :**
- `simple` : Croisement en un point
- `double` : Croisement en deux points
- `barycentrique` : Partially Mapped Crossover
- `uniforme` : Sélection aléatoire par masque

**Méthodes de mutation :**
- `echange` : Swap de deux éléments
- `inversion` : Inversion d'un segment
- `insertion` : Déplacement d'un élément

## 📊 Résultats et Visualisation

### Pour le TSP
- Affichage du chemin optimal
- Distance totale minimale
- Ordre de visite des villes
- Heatmap de la matrice des distances

### Pour l'Ordonnancement
- Diagramme de Gantt des tâches
- Makespan total et retards
- Respect des deadlines et priorités
- Détail de l'ordonnancement

## 🎯 Fonctionnalités Avancées

### Génération de Données
- **Générer aléatoirement** : Crée de nouvelles données complètement différentes
- **Réorganiser aléatoirement** : Mélange l'ordre des données existantes

### Configuration Dynamique
- Slider pour le nombre de villes/tâches (5-20 villes, 5-15 tâches)
- Paramètres spécifiques à chaque algorithme
- Interface adaptative selon le problème choisi

## 📁 Structure du Projet

```
optimisation-combinatoire/
├── 🎯 app.py                          # Interface Streamlit principale
├── 📋 requirements.txt                # Dépendances
├── 🗺️ VoyageurDeCommerce/
│   ├── RechercheParTabou.py
│   ├── RécuitSimulé.py
│   └── AlgorithmeGénétique.py
├── ⏰ OrdonnancementDesTaches/
│   ├── tache.py
│   ├── utils.py
│   ├── tabou.py
│   ├── recuit_simule.py
│   └── algo_genetique.py
└── 📚 README.md
```

## 🚀 Utilisation

### 1. Installation
```bash
git clone https://github.com/Hsan-Kh/optimisation-combinatoire
cd optimisation-combinatoire
pip install -r requirements.txt
```

### 2. Lancement
```bash
streamlit run app.py
```

### 3. Configuration
**Étape 1 : Choix du problème**
- Sélectionner TSP ou Ordonnancement dans la barre latérale

**Étape 2 : Configuration des données**
- Ajuster le nombre de villes (5-20) ou de tâches (5-15)
- Générer de nouvelles données aléatoires
- Ou réorganiser les données existantes

**Étape 3 : Sélection de l'algorithme**
- Choisir parmi Recherche Tabou, Recuit Simulé ou Algorithme Génétique

**Étape 4 : Paramétrage**
- Ajuster les paramètres spécifiques à l'algorithme choisi
- Configurer les méthodes (pour l'algorithme génétique)

**Étape 5 : Exécution**
- Lancer la simulation avec le bouton "Résoudre"
- Observer les résultats et visualisations en temps réel

## 📈 Comparaison des Algorithmes

| Critère | Recherche Tabou | Recuit Simulé | Algo Génétique |
|---------|----------------|---------------|----------------|
| **Approche** | Recherche locale | Recherche stochastique | Évolutionnaire |
| **Mémoire** | Liste tabou | Température | Population |
| **Diversification** | Faible | Moyenne | Forte |
| **Complexité** | Moyenne | Faible | Élevée |
| **Paramètres** | 2 | 3 | 6+ |
| **Vitesse** | Moyenne | Rapide | Lente |

## 🎓 Concepts Clés Implémentés

### Métaheuristiques
- **Recherche locale** : Tabou
- **Recherche stochastique** : Recuit simulé
- **Algorithmes évolutionnaires** : Génétique

### Représentation des Solutions
- **TSP** : Permutation de villes
- **Ordonnancement** : Séquence de tâches

### Fonctions d'Évaluation
- **TSP** : Distance totale du parcours
- **Ordonnancement** : Coût combiné (makespan + retards)

## 🔮 Améliorations Futures
- Ajout de visualisations graphiques avancées
- Comparaison automatique des algorithmes
- Génération de benchmarks
- Export des résultats en PDF/Excel
- Interface en temps réel avec animations

## 👨‍💻 Auteur

**Réalisé par :** Hsan Khecharem

**Filière :** Licence en Sciences de l'Informatique  
**Spécialité :** Génie Logiciel et Systèmes d'Information  
**Faculté :** Faculté des Sciences de Sfax

*Projet académique - Optimisation combinatoire et métaheuristiques*

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---

💡 **Note :** Cette interface permet une étude comparative complète des métaheuristiques sur des problèmes d'optimisation combinatoire classiques, avec une expérience utilisateur intuitive et des visualisations avancées. Le projet démontre l'application pratique des algorithmes d'optimisation sur des problèmes réels de logistique et de planification.
