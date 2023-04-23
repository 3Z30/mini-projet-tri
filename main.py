import sorts
import random
import json

# initialisation des variables
username = input("Quel est votre nom ?\n> ")
randomList = []

# tableau de taille aleatoire contenant des entiers aleatoires
for i in range(random.randint(1, 50)):
    randomList.append(random.randint(0, 100))

# affichage du 'menu' - choix de l'algo.
print(f"Le tableau à trier est:\n\n{randomList}\n")
print("Veuillez trier le tableau en utilisant"
      "le moins de temps possible !")
print("Choisissez l'un des alhorithmes de tri suivant:\n"
      "\n1. Tri à bulles\n"
      "2. Tri par sélection\n"
      "3. Tri par insertion\n"
      "4. Tri rapide\n")

choice = input("\nEntrez votre choix: ")

# restriction de l'utilisateur a un chiffre entre 1 et 4
while not choice.isnumeric() or int(choice) <= 0 or int(choice) > 4:
    print("Choisissez une réponse entre 1 et 4.")
    choice = input("\nEntrez votre choix: ")

# afficher le tableau trie avec l'algo. choisi par l'utilisateur
print("Le tableau trié est:\n")
if choice == 1:
    print(sorts.bubble_sort(randomList))
elif choice == 2:
    print(sorts.selection_sort(randomList))
elif choice == 3:
    print(sorts.insertion_sort(randomList))
else:
    print(sorts.quicksort(randomList))

# attribution du score
if sorts.fastest(randomList) == int(choice):
    print("Félicitations vous avez déterminé le tri le plus rapide !")
    score = 1
else:
    print("Dommage vous n'avez pas réussi...")
    print(f"Le plus rapide était le tri n°{sorts.fastest(randomList)}")
    score = 0

# sauvegarde du score -> .json
try:
    with open("scores.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

if username not in data:
    data[username] = score
else:
    data[username] += score
with open("scores.json", "w") as file:
    json.dump(data, file)
