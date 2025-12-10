# Programme de calcul de moyenne et attribution de mention
# Développé par Amina Eddaoudi

print("=== Programme Calcul de Moyenne ===\n")

# Informations de l'étudiant
prenom = input("Entrez le prénom de l'étudiant : ")
nom = input("Entrez le nom de l'étudiant : ")

# Nombre de matières
nb_matieres = int(input("Entrez le nombre de matières : "))

total = 0

# Saisie des notes
for i in range(1, nb_matieres + 1):
    note = float(input(f"Note pour la matière {i} : "))
    total += note

# Calcul de la moyenne
moyenne = total / nb_matieres

# Attribution de la mention
if moyenne >= 16:
    mention = "Très Bien"
elif moyenne >= 14:
    mention = "Bien"
elif moyenne >= 12:
    mention = "Assez Bien"
elif moyenne >= 10:
    mention = "Passable"
else:
    mention = "Insuffisant"

# Affichage des résultats
print("\n=== Résultat ===")
print("Nom :", prenom, nom)
print("Moyenne générale :", round(moyenne, 2))
print("Mention :", mention)

print("\nMerci d'avoir utilisé le programme !")
