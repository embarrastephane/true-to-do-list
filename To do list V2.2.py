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
            print(f"{index}- Priorité: {priority} {task}")#afficher l'index de l'élément suivi de sa priorité puis de la tache en elle meme ex: 1- priorité:1 Reviser

def delete_task():#Supprimer une tâche par son nom.
    task_to_delete = input("Entrer la tâche à supprimer : ")#l'utilisateur saisi la tache à supprimer
    for task in tasks_list:#En considérant toutes les taches de la liste
        if task[1] == task_to_delete:#Si une tache correspond à la tache à supprimer
            tasks_list.remove(task)#Retiter cet élément de la liste de tache
            print(f'La tâche "{task_to_delete}" a été supprimée')#affichage texte
            return#au cas contraire
    print("Cette tâche n'existe pas dans la liste")#affichage ceci

def search_task():#fonction pour rechercher une tache par son nom
    task_to_search = input("Entrer la tâche que vous cherchez : ")#l'utilisateur dois saisir le nom de la tache à supprimer
    for priority, task in tasks_list:#pour toutes les tache qu'importe leur priorité
        if task == task_to_search:#Si la tache est présente dans la liste
            print(f'{task_to_search} est présente dans la liste avec priorité {priority}')#Alors confirme sa présence et done sa priorité
            return#Sinon
    print("L'élément n'est pas présent dans la liste")#Elément non présent dans la liste

while True:  # Boucle qui fait tourner le programme
    print("\nMenu principal")
    print("1 - Ajouter une tâche")#Option du menu principale
    print("2 - Afficher la liste des tâches")#Option du menu principale
    print("3 - Supprimer une tâche")#Option du menu principale
    print("4 - Rechercher une tâche")#Option du menu principale
    print("5 - Quitter le menu")#Option du menu principale
    
    option = input("Veuillez choisir une option : ")#option choisie par l'utilisateur

    if option == "1":#Si l'utilisateur saisi 1
        add_task()#executer la fonction add_task
    elif option == "2":#Si l'utilisateur saisi 2
        display_tasks()#executer la fonction display_task
    elif option == "3":#Si l'utilisateur saisi 4
        delete_task()#executer la fonction delete_task
    elif option == "4":#Si l'utilisateur saisi 5
        search_task()#executer la fonction search_task
    elif option == "5":#Si l'utilisateur saisi 6
        print("Bye bye👌👋")#afficher ce message
        break#casser la boucle
    else:#Si l'utilisateur saisi une autre option
        print("Option non valide.")#afficher ce message
