tasks_list = []  # La liste vide dans laquelle se trouveront toutes nos tâches

def add_task():#fonction pour ajouter une tache avec une priorité
    task = input("Veuillez ajouter la tâche : ")#tache entrer par l'utilisateur
    priority = int(input("Priorité de la tâche (1 pour prioritaire, 2 pour secondaire) : "))#priorité de cette tache
    tasks_list.append((priority, task))#ajout de cette tache en tenant compte de la priorité en allant du  bas vers le haut grace à la fonction append
    print(f'La tâche "{task}" avec priorité {priority} a été ajoutée à la liste')#output utilisateur pour la confirmation d'ajout

def display_tasks():#Affichage de la liste de tache avec les priorités
    if not tasks_list:#s'il n ya pas de liste
        print("Il n'y a pas de liste disponible pour le moment, créez-en une 👍")#Output utilisateur retour au menu
    else:#au cas contraire
        print("Voici votre liste de choses à faire avec priorités :")#Texte à afficher
        for index, (priority, task) in enumerate(tasks_list, start=1):#Pour le nombre d'élément présent dans la liste, effectuer un boucle pour les énumérer
            print(f"{index}. Priorité: {priority} {task}")

def sort_tasks(order="asc"):
    """Trier les tâches par ordre de priorité croissant ou décroissant."""
    tasks_list.sort(key=lambda x: x[0], reverse=(order == "desc"))
    order_str = "décroissant" if order == "desc" else "croissant"
    print(f"Les tâches ont été triées par ordre {order_str}.")

def delete_task():
    """Supprimer une tâche par son nom."""
    task_to_delete = input("Entrer la tâche à supprimer : ")
    for task in tasks_list:
        if task[1] == task_to_delete:
            tasks_list.remove(task)
            print(f'La tâche "{task_to_delete}" a été supprimée')
            return
    print("Cette tâche n'existe pas dans la liste")

def search_task():
    """Rechercher une tâche par son nom."""
    task_to_search = input("Entrer la tâche que vous cherchez : ")
    for priority, task in tasks_list:
        if task == task_to_search:
            print(f'{task_to_search} est présente dans la liste avec priorité {priority}')
            return
    print("L'élément n'est pas présent dans la liste")

while True:  # Boucle qui fait tourner le programme
    print("\nMenu principal")
    print("1 - Ajouter une tâche")
    print("2 - Afficher la liste des tâches")
    print("3 - Trier les tâches")
    print("4 - Supprimer une tâche")
    print("5 - Rechercher une tâche")
    print("6 - Quitter le menu")
    
    option = input("Veuillez choisir une option : ")

    if option == "1":
        add_task()
    elif option == "2":
        display_tasks()
    elif option == "3":
        order = input("Choisissez l'ordre de tri (asc pour croissant, desc pour décroissant) : ")
        sort_tasks(order)
    elif option == "4":
        delete_task()
    elif option == "5":
        search_task()
    elif option == "6":
        print("Bye bye👌👋")
        break
    else:
        print("Option non valide.")
