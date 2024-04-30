import os

# Function to read constraints from a given file path
def read_constraints(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        return "File not found"

    matrix = []
    # Open the file
    with open(file_path, "r") as file:
        # Read the first line
        first_line = file.readline().strip().split()
        # Process the first line to get dimensions of the matrix
        ligne, colonne = map(int, first_line)

        # Read the remaining lines to construct the matrix
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)

    return ligne, colonne, matrix

def matrice_cout(ligne, colonne, matrice):
    # Affichage des dimensions de la matrice
    print("Ligne:", ligne)
    print("Colonne:", colonne)

    # Affichage de la matrice avec les libellés de lignes et de colonnes
    print("\nMatrice :")
    # Les libellés de lignes
    mes_lignes = [f'P{i}' for i in range(1, ligne + 1)] + ['Commandes']
    # Les libellés de colonnes
    mes_colonnes = [f'C{i}' for i in range(1, colonne + 1)] + ['ProvisionsPi']
    # Affichage de la matrice
    afficher_matrice_cout(matrice, mes_lignes, mes_colonnes)

def afficher_matrice_cout(matrice, mes_lignes, mes_colonnes):
    # Longueur maximale des libellés de colonnes
    max_len_colonne = max([len(col) for col in mes_colonnes])

    # Affichage des libellés de colonnes
    print(" " * (max_len_colonne + 1), end="")
    for col in mes_colonnes:
        print("{:^{width}}".format(col, width=max_len_colonne), end="")
    print()

    # Affichage des lignes
    for i, ligne in enumerate(mes_lignes):
        print("{:<{width}} |".format(ligne, width=max_len_colonne), end=" ")
        for element in matrice[i]:
            print("{:>{width}}".format(element, width=max_len_colonne), end="")
        print()


def matrice_transport(ligne, colonnes, matrice):
    nouvelle_ligne = []
    nouvelle_ligne = [0] * (colonnes)
    for j in range(ligne+4):
        if j%2==1:
            matrice.insert(j,nouvelle_ligne)
    mes_lignes = [f'P{i}' for i in range(1, ligne + 1)]
    mes_lignes_intercalees = [ligne for ligne in mes_lignes for _ in range(2)]
    mes_lignes_intercalees.append('Commandes')

    # Les libellés de colonnes
    mes_colonnes = [f'C{i}' for i in range(1, colonne + 1)] + ['ProvisionsPi']
    afficher_matrice_transport(matrice,mes_lignes_intercalees,mes_colonnes)


def afficher_matrice_transport(matrice, mes_lignes, mes_colonnes):
    # Longueur maximale des libellés de colonnes
    max_len_colonne = max([len(col) for col in mes_colonnes])

    # Affichage des libellés de colonnes
    print(" " * (max_len_colonne + 1), end="")
    for col in mes_colonnes:
        print("{:^{width}}".format(col, width=8), end="")
    print()

    # Affichage des lignes
    for i, ligne in enumerate(mes_lignes):
        print("{:<{width}} |".format(ligne, width=max_len_colonne), end=" ")


        for element in matrice[i]:
            print("{:8}".format(element), end="")

        print()

choice = 0
while choice != 1:

    table = input("Enter the table number (between 1 and 14) :")

    match table:
        case "1":
            file_path = 'file1.txt'
        case "2":
            file_path = 'file2.txt'
        case "3":
            file_path = 'file3.txt'
        case "4":
            file_path = 'file4.txt'
        case "5":
            file_path = 'file5.txt'
        case "6":
            file_path = 'file6.txt'
        case "7":
            file_path = 'file7.txt'
        case "8":
            file_path = 'file8.txt'
        case "9":
            file_path = 'file9.txt'
        case "10":
            file_path = 'src/table 10.txt'
        case "11":
            file_path = 'src/table 11.txt'
        case "12":
            file_path = 'src/table 12.txt'
        case "13":
            file_path = 'src/table 13.txt'
        case "14":
            file_path = 'src/table 14.txt'
        case "test":
            file_path = 'test.txt'
    ligne, colonne, matrice = read_constraints(file_path)
    print(ligne,colonne, matrice)
    matrice_cout(ligne, colonne,matrice)
    print('\n')
    matrice_transport(ligne, colonne,matrice)
