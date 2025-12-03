🚀 Plan & Execute Agent
Agent autonome capable de :

Décomposer une tâche complexe (Task Planning)

Choisir dynamiquement les bons outils (Tool Selection)

Exécuter étape par étape (Execution Engine)

Accumuler un contexte multi-étapes (Context Memory)

Utiliser le RAG interne pour enrichir l'analyse

Raffiner/mettre à jour son raisonnement

Générer une réponse finale synthétique

Architecture inspirée des approches Anthropic (Claude 3.5) & OpenAI Agents (GPT-4o).

🧠 Fonctionnalités principales
1. Décomposition automatique des tâches (Task Decomposition)

Lorsqu’on donne une tâche complexe comme :

"Analyse le module geometry et compare avec physics"

Le système :

Analyse la demande

Détecte les sous-tâches nécessaires

Génère un plan séquentiel

Forme une liste d’étapes numérotées

Exemples d’étapes générées :

1. Lister les fichiers du module geometry
2. Lire le contenu du fichier principal
3. Lister les fichiers du module physics
4. Comparer les structures des deux modules
5. Produire une synthèse finale


Ce comportement est essentiel pour un agent autonome.

2. Choix intelligent des outils (Tool Selection)

Le LLM reçoit le plan et doit déterminer, pour chaque étape :

quel outil utiliser

avec quel input

Outils disponibles :

Tool	Description
list_files	Explorer un dossier et récupérer ses fichiers
read_file	Lire le contenu d’un fichier
search	Faire un RAG interne sur la base vectorielle