high_task = []
casual_task = []
tasks_list = high_task + casual_task # La liste vide dans laquelle se trouvera toutes nos taches

def update_tasks_list():
    global tasks_list
    tasks_list = high_task + casual_task

print("Liste de choses à faire")

def add_task():
    print("1-Important")
    print("2-Secondaire")
    importance=int(input("Priorité de la tache 1/2:"))
    if importance==1:
        task = input("Veuillez entrer une tâche prioritaire : ")
        high_task.append(task)
        print(f'La tâche "{task}" a été ajoutée à la liste')
        update_tasks_list()
    elif importance==2:
        task = input("Veuillez entrer une tâche secondaire : ")
        casual_task.append(task)
        print(f'La tâche "{task}" a été ajoutée à la liste')
        update_tasks_list()
    else:
        print("Option non valide")
def delete_task():
    task_to_delete = input("Entrer la tâche à supprimer : ")
    try:
        if task_to_delete in high_task:
            high_task.remove(task_to_delete)
        elif task_to_delete in casual_task:
            casual_task.remove(task_to_delete)
        else:
            raise ValueError
        print(f'La tâche "{task_to_delete}" a été supprimée')
        update_tasks_list()
    except ValueError:
        print("Cette tâche n'existe pas")

def research_task():
    task_to_research = input("Entrer la tâche que vous cherchez : ")
    if task_to_research in tasks_list:
        print(f'{task_to_research} est présent dans la liste')
    else:
        print("L'élément n'est pas présent dans la liste")

def list_of_tasks():
    if not tasks_list:
        print("Il n'y a pas de liste disponible pour le moment, créez-en une 👍")
    else:
        print("Voici votre liste de choses à faire :")
        for index, task in enumerate(tasks_list, start=1):
            print(f"{index} - {task}")

while True: # Boucle qui fait tourner le programme
    print("Menu principal")
    print()
    print("1 - Ajouter une tâche") # Différentes options
    print("2 - Afficher la liste") # Différentes options
    print("3 - Supprimer une tâche") # Différentes options
    print("4 - Recherche de tâche") # Différentes options
    print("5 - Quitter le menu") # Différentes options
    option = input("Veuillez choisir une option : ") # Choix de l'utilisateur

    if option == "1":
        add_task()
    elif option == "2":
        list_of_tasks()
    elif option == "3":
        delete_task()
    elif option == "4":
        research_task()
    elif option == "5":
        print("Bye bye👌👋")
        break
    else:
        print("Option non valide.")