import os
from openai import OpenAI
from dotenv import load_dotenv
from executor import execute_step
from plan import generate_plan
from interpreter import interpret_step

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class bcolors:
    WHITE = "\033[37m"
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'

def plan_and_execute(task: str):

    if task == "break":
        return
    plan = generate_plan(task)
    context = ""

    for i, step in enumerate(plan, 1):
        print(f"\n---- STEP {i} : {step} ---")
        tool_name, tool_input = interpret_step(step, context)
        print(f"-> Tool choisi : {tool_name}")
        print(f"-> Input : {tool_input}")

        result = execute_step(tool_name, tool_input)

        print("-> Résultat de l'exécution :")
        print(result[:500] + "\n...") if len(str(result)) > 500 else print(result)

        context += f"""

===== ÉTAPE {i} =====
Action : {step}
Tool : {tool_name}
Input : {tool_input}
Résultat :
{result}

"""
    prompt = f"""
Tu es un agent intelligent. Une tâche complexe a été exécutée étape par étape.

Voici tout le contexte accumulé :
{context}

En te basant UNIQUEMENT sur ces informations,
réponds à la question originale :

QUESTION :
{task}

RÉPONSE :

"""
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content

    return response 

if __name__ == "__main__":
    task = input(f"{bcolors.OKGREEN}Entrez une tâche >>{bcolors.WHITE} ")
    result = plan_and_execute(task)
    print(f"{bcolors.OKGREEN}Résultats >>{bcolors.WHITE}\n{result}")