import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_plan(task: str) -> list[str]:

    prompt = f"""
Tu travailles UNIQUEMENT avec les fichiers présents dans mon corpus local.

Ton environnement contient :
- Un outil list_files(path) qui liste les fichiers d’un dossier
- Un outil read_file(path) qui lit un fichier texte
- Un outil search(query) qui effectue une recherche vectorielle sur MON corpus

NE PROPOSE PAS :
- d’installer un module
- de lire une documentation externe
- d’utiliser des fichiers qui n’existent pas
- de mentionner internet ou des données externes

Pour cela, tu vas décomposer la tâche donnée en étapes numérotées et séparées par **UN SEUL** \n.
Chaque étape doit être EXPLICITE et utiliser un OUTIL parmi :

1. list_files
2. read_file
3. search

Tâche :
{task}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt }]
    ).choices[0].message.content


    tasks_list = []
    for resp in response.split("\n"):
        tasks_list.append(resp)

    return tasks_list
