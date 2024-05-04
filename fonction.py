import os

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
    temp_mat=matrice
    nouvelle_ligne = []
    nouvelle_ligne = [0] * (colonnes)
    for j in range(ligne+4):
        if j%2==1:
            temp_mat.insert(j,nouvelle_ligne)
    mes_lignes = [f'P{i}' for i in range(1, ligne + 1)]
    mes_lignes_intercalees = [ligne for ligne in mes_lignes for _ in range(2)]
    mes_lignes_intercalees.append('Commandes')

    # Les libellés de colonnes
    mes_colonnes = [f'C{i}' for i in range(1, colonnes + 1)] + ['ProvisionsPi']
    afficher_matrice_transport(temp_mat,mes_lignes_intercalees,mes_colonnes)


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


def North_Ouest1(file):
    mes_lignes,mes_colonnes,matrice= read_constraints(file)
    offre= []
    demande = matrice[-1]
    solution = [[0] * mes_colonnes for _ in range(mes_lignes)]
    for i in range(mes_lignes):
        offre.append(matrice[i][mes_colonnes])
    print('offre : ', offre)
    print('demande : ', demande)
    l,c =0,0
    while l < mes_lignes and c < mes_colonnes:  # Correction de la condition de la boucle while
        quantite = min(offre[l], demande[c])
        solution[l][c] = quantite
        # Mettre à jour les contraintes d'offre et de demande
        offre[l] -= quantite
        demande[c] -= quantite
        # Passer à la prochaine cellule
        if offre[l] == 0:
            l += 1
        if demande[c] == 0:
            c += 1

        # Calculer le coût total
    cout_total = sum(matrice[l][c] * solution[l][c] for l in range(mes_lignes) for c in range(mes_colonnes))  # Correction du calcul du coût total

    return solution, cout_total

def Affichage_North_Ouest(matrice,solution,colonnes,lignes):
    ind=0
    for i in range(lignes*2):
        if i%2 !=0:
            matrice[i]=solution[ind]
            ind+=1
    mes_lignes = [f'P{i}' for i in range(1, lignes + 1)]
    mes_lignes_intercalees = [lignes for lignes in mes_lignes for _ in range(2)]
    mes_lignes_intercalees.append('Commandes')

    # Les libellés de colonnes
    mes_colonnes = [f'C{i}' for i in range(1, colonnes + 1)] + ['ProvisionsPi']
    afficher_matrice_transport(matrice, mes_lignes_intercalees, mes_colonnes)


def Ballas_Hammer(file):
    mes_lignes, mes_colonnes, matrice = read_constraints(file)
    offre = []
    demande = matrice[-1]
    solution = [[0] * mes_colonnes for _ in range(mes_lignes)]
    for i in range(mes_lignes):
        offre.append(matrice[i][mes_colonnes])
    print('offre : ', offre)
    print('demande : ', demande)
    indice_ligne=[]
    indice_colonne= []
    col= []
    j=0
    l=0
    #while offre != [] or demande != []:
    for o in range(2):
        for i in range(mes_lignes):
            liste_triee = sorted(matrice[i])
            delta = liste_triee[:2]
            indice_ligne.append(delta[1]-delta[0])
        print('ind ligne = ',indice_ligne)

        for j in range(mes_colonnes):
            col = []
            for l in range(mes_lignes):
                col.append(matrice[l][j])
            col = sorted(col)
            delta2 = col[:2]
            indice_colonne.append(delta2[1] - delta2[0])
        print('indice colonne = ',indice_colonne)
        delta_plus_faible_ligne= indice_ligne.index(min(indice_ligne))
        delta_plus_faible_col= indice_colonne.index(min(indice_colonne))
        indice_ligne = []
        indice_colonne = []
        cellule_choisie = [delta_plus_faible_ligne,delta_plus_faible_col]
        print('cellule chosie = ',cellule_choisie)
        if offre[cellule_choisie[0]] == 0:

            matrice[cellule_choisie[0]]= [0]*mes_colonnes
            print(matrice)
        if offre[cellule_choisie[0]] > demande[cellule_choisie[1]]:
            calcul = offre - demande
            print(calcul)
            demande[cellule_choisie[1]]= 0
        else:
            solution[cellule_choisie[0]][cellule_choisie[1]]= offre[cellule_choisie[0]]
            print('solution : \n',solution)
            offre[cellule_choisie[0]]=0

def extraction_mat(matrice):
    last_row = matrice[-1]  # Extraire la dernière ligne
    last_column = []  # Liste pour stocker la dernière colonne extraite
    new_matrice = []  # Nouvelle matrice après avoir retiré la dernière colonne

    for ligne in matrice[:-1]:  # Parcourir toutes les lignes sauf la dernière
        new_ligne = ligne[:-1]  # Retirer la dernière valeur de la ligne
        last_value = ligne[-1]  # Récupérer la dernière valeur retirée
        last_column.append(last_value)  # Ajouter la dernière valeur à la liste des valeurs de la dernière colonne
        new_matrice.append(new_ligne)  # Ajouter la ligne modifiée à la nouvelle matrice

    return new_matrice, last_row, last_column

def Ballas_Hammer1(file):
    indice_ligne = []
    indice_colonne = []
    # Fonction pour lire les contraintes du fichier
    mes_lignes, mes_colonnes, matrice = read_constraints(file)
    offre = [matrice[i][-1] for i in range(mes_lignes)]  # Dernière colonne de la matrice est l'offre
    demande = matrice[-1]  # Dernière ligne de la matrice est la demande
    solution = [[0] * mes_colonnes for _ in range(mes_lignes)]

    # Initialisation des pénalités
    penalites_lignes = []
    penalites_colonnes = []
    print(solution,mes_lignes,mes_colonnes,offre,demande)

    for p in range(2):
    #while any(demande) > 0:  # Tant qu'il y a de la demande non satisfaite
        print(matrice)
        print("Pénalités avant la mise à jour :", penalites_lignes, penalites_colonnes)
        for i in range(mes_lignes):
            liste_triee = sorted(matrice[i])
            delta = liste_triee[:2]
            indice_ligne.append(delta[1] - delta[0])
        print('ind ligne = ', indice_ligne)

        for j in range(mes_colonnes):
            col = []
            for l in range(mes_lignes):
                col.append(matrice[l][j])
            col = sorted(col)
            delta2 = col[:2]
            indice_colonne.append(delta2[1] - delta2[0])
        print('indice colonne = ', indice_colonne)
        delta_plus_faible_ligne = indice_ligne.index(min(indice_ligne))
        delta_plus_faible_col = indice_colonne.index(min(indice_colonne))
        print('offre   =' , offre )
        if offre[delta_plus_faible_ligne] == 0:  # Si l'offre est épuisée
            matrice[delta_plus_faible_ligne] = [float("inf")] * mes_colonnes  # Mettre à l'infini toute la ligne

        elif offre[delta_plus_faible_ligne] >= demande[
            delta_plus_faible_col]:  # Si l'offre est suffisante pour la demande
            solution[delta_plus_faible_ligne][delta_plus_faible_col] = demande[
                delta_plus_faible_col]  # Mettre la quantité de demande dans la solution
            offre[delta_plus_faible_ligne] -= demande[delta_plus_faible_col]  # Mettre à jour l'offre
            demande[delta_plus_faible_col] = float("inf")  # Marquer la demande comme satisfaite

        else:  # Si la demande dépasse l'offre
            solution[delta_plus_faible_ligne][delta_plus_faible_col] = offre[
                delta_plus_faible_ligne]  # Mettre la quantité d'offre dans la solution
            demande[delta_plus_faible_col] -= offre[delta_plus_faible_ligne]  # Mettre à jour la demande
            offre[delta_plus_faible_ligne] = float("inf")  # Marquer l'offre comme épuisée
        print("Pénalités après la mise à jour :", penalites_lignes, penalites_colonnes)
        print('solution :',solution)

    return solution


def Ballas_Hammer3(file):
    indice_ligne = []
    indice_colonne = []
    # Fonction pour lire les contraintes du fichier
    mes_lignes, mes_colonnes, tpmmatrice = read_constraints(file)
    matrice,offre,demande=extraction_mat(tpmmatrice)

    solution = [[0] * mes_colonnes for _ in range(mes_lignes)]

    # Initialisation des pénalités
    penalites_lignes = []
    penalites_colonnes = []
    print(solution, mes_lignes, mes_colonnes, offre, demande)

    for b in range(3):
        # Initialisation des pénalités
        penalites_lignes = []
        penalites_colonnes = []

        for i in range(mes_lignes - 1):  # Exclure la dernière ligne
            liste_triee = sorted(matrice[i])
            delta = liste_triee[:2]
            penalites_lignes.append(delta[1] - delta[0])  # Calcul des pénalités pour les lignes

        for j in range(mes_colonnes - 1):  # Exclure la dernière colonne
            col = [matrice[l][j] for l in range(mes_lignes)]
            col = sorted(col)
            delta2 = col[:2]
            penalites_colonnes.append(delta2[1] - delta2[0])  # Calcul des pénalités pour les colonnes

        print("Pénalités avant la mise à jour :", penalites_lignes, penalites_colonnes)

        delta_plus_faible_ligne = penalites_lignes.index(min(penalites_lignes))
        print('delta ligne :', delta_plus_faible_ligne)
        delta_plus_faible_col = penalites_colonnes.index(min(penalites_colonnes))
        print('delta colonne :', delta_plus_faible_col)
        print(matrice)

        if offre[delta_plus_faible_ligne] > demande[
            delta_plus_faible_col]:  # Si l'offre est strictement supérieure à la demande
            solution[delta_plus_faible_ligne][delta_plus_faible_col] = demande[
                delta_plus_faible_col]  # Mettre la quantité de demande dans la solution
            offre[delta_plus_faible_ligne] -= demande[delta_plus_faible_col]  # Mettre à jour l'offre
            demande[delta_plus_faible_col] = float("inf")  # Marquer la demande comme satisfaite
            # Parcourir chaque ligne de la matrice et marquer la colonne correspondante comme "inf"
            for i in range(mes_lignes):
                matrice[i][delta_plus_faible_col] = float("inf")
            # Remplacer la valeur dans la matrice par inf pour marquer la demande comme satisfaite
            matrice[delta_plus_faible_ligne][delta_plus_faible_col] = float("inf")
            print("Offre suffisante pour la demande. Demande marquée comme satisfaite.", matrice)
        elif offre[delta_plus_faible_ligne] == demande[delta_plus_faible_col]:  # Si l'offre est égale à la demande
            solution[delta_plus_faible_ligne][delta_plus_faible_col] = demande[
                delta_plus_faible_col]  # Mettre la quantité de demande dans la solution
            offre[delta_plus_faible_ligne] = float("inf")  # Marquer l'offre comme satisfaite
            demande[delta_plus_faible_col] = float("inf")  # Marquer la demande comme satisfaite
            # Parcourir chaque ligne de la matrice et marquer la colonne correspondante comme "inf"
            for i in range(mes_lignes):
                matrice[i][delta_plus_faible_col] = float("inf")
            # Remplacer la valeur dans la matrice par inf pour marquer la demande comme satisfaite
            matrice[delta_plus_faible_ligne][delta_plus_faible_col] = float("inf")
            print("Offre égale à la demande. Demande et offre marquées comme satisfaites.", matrice)
        else:  # Si la demande dépasse l'offre
            print('hello')
            solution[delta_plus_faible_ligne][delta_plus_faible_col] = offre[
                delta_plus_faible_ligne]  # Mettre la quantité d'offre dans la solution
            demande[delta_plus_faible_col] -= offre[delta_plus_faible_ligne]  # Mettre à jour la demande
            offre[delta_plus_faible_ligne] = float("inf")  # Marquer l'offre comme épuisée
            # Remplacer chaque élément de la ligne par inf pour marquer l'offre comme épuisée
            for j in range(mes_colonnes - 1):  # Exclure la dernière colonne
                matrice[delta_plus_faible_ligne][j] = float("inf")
            print("Offre insuffisante pour la demande. Ligne remplie de 'inf'.", matrice)

        print("Pénalités après la mise à jour :", penalites_lignes, penalites_colonnes)
        print('solution :', solution)
        print(demande)
        print(offre)

    return solution









