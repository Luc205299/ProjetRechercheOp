from copy import deepcopy


def initialiser_matrice_résultat(coût):
    lig = len(coût)
    col = len(coût[0])
    solution = [[0] * col for _ in range(lig)]
    return solution



def récupérer_max_pénalités(pénalités):
    max_value = 0
    index = 0
    à_envoyer = True

    for pénalité in range(len(pénalités['pénalités_demande'])):
        value = pénalités['pénalités_demande'][pénalité]
        if value > max_value:
            index = pénalité
            max_value = value

    for pénalité in range(len(pénalités['pénalités_offre'])):
        value = pénalités['pénalités_offre'][pénalité]
        if value > max_value:
            index = pénalité
            max_value = value
            à_envoyer = False

    return {
        'max': max_value,
        'à_envoyer': à_envoyer,
        'index': index
    }

def calculer_pénalités(coût, demande, offre):
    pénalités_demande = []
    pénalités_offre = []

    for i in range(len(coût)):
        if offre[i] == 0:
            pénalités_offre.append(-1)
        else:
            ligne_copie = deepcopy(coût[i])
            ligne_copie.sort()
            if ligne_copie[1] == float('inf'):
                ligne_copie[1] = ligne_copie[0]
                ligne_copie[0] = 0
            pénalités_offre.append(ligne_copie[1] - ligne_copie[0])

    for j in range(len(coût[0])):
        if demande[j] == 0:
            pénalités_demande.append(-1)
        else:
            colonne = []
            for i in range(len(coût)):
                colonne.append(coût[i][j])
            colonne.sort()
            if colonne[1] == float('inf'):
                colonne[1] = colonne[0]
                colonne[0] = 0
            pénalités_demande.append(colonne[1] - colonne[0])

    return {
        'pénalités_demande': pénalités_demande,
        'pénalités_offre': pénalités_offre
    }


def transporter_via_max_pénalité(max_pénalité, matrice_coûts, demande, offre, matrice_résultat):
    index_max_pénalité = max_pénalité['index']

    if max_pénalité['à_envoyer']:
        min_val = matrice_coûts[0][index_max_pénalité]
        index_min = 0
        for index in range(len(matrice_coûts)):
            if min_val > matrice_coûts[index][index_max_pénalité]:
                min_val = matrice_coûts[index][index_max_pénalité]
                index_min = index

        if offre[index_min] >= demande[index_max_pénalité]:
            offre[index_min] -= demande[index_max_pénalité]
            matrice_résultat[index_min][index_max_pénalité] = demande[index_max_pénalité]
            demande[index_max_pénalité] = 0
            for index in range(len(matrice_coûts)):
                matrice_coûts[index][index_max_pénalité] = float("inf")
        else:
            demande[index_max_pénalité] -= offre[index_min]
            matrice_résultat[index_min][index_max_pénalité] = offre[index_min]
            offre[index_min] = 0
            for index in range(len(matrice_coûts[index_min])):
                matrice_coûts[index_min][index] = float("inf")

    else:
        min_val = matrice_coûts[index_max_pénalité][0]
        index_min = 0
        for index in range(len(matrice_coûts[index_max_pénalité])):
            if min_val > matrice_coûts[index_max_pénalité][index]:
                min_val = matrice_coûts[index_max_pénalité][index]
                index_min = index

        if demande[index_min] >= offre[index_max_pénalité]:
            demande[index_min] -= offre[index_max_pénalité]
            matrice_résultat[index_max_pénalité][index_min] = offre[index_max_pénalité]
            offre[index_max_pénalité] = 0
            for index in range(len(matrice_coûts[index_max_pénalité])):
                matrice_coûts[index_max_pénalité][index] = float("inf")
        else:
            offre[index_max_pénalité] -= demande[index_min]
            matrice_résultat[index_max_pénalité][index_min] = demande[index_min]
            demande[index_min] = 0
            for index in range(len(matrice_coûts)):
                matrice_coûts[index][index_min] = float("inf")

def calculer_coût(matrice_coûts, matrice_résultat):
    coût_total = 0
    for i in range(len(matrice_coûts)):
        for j in range(len(matrice_coûts[0])):
            coût_total += matrice_coûts[i][j] * matrice_résultat[i][j]
    return coût_total

def transporter(matrice_coûts, demande, offre):
    pénalités = calculer_pénalités(matrice_coûts, demande, offre)
    matrice_résultat = initialiser_matrice_résultat(matrice_coûts)
    coûts_copie = deepcopy(matrice_coûts)

    while not est_matrice_remplie_avec_valeur(coûts_copie, float('inf')):
        max_pénalité = récupérer_max_pénalités(pénalités)
        transporter_via_max_pénalité(max_pénalité, coûts_copie, demande, offre, matrice_résultat)
        pénalités = calculer_pénalités(coûts_copie, demande, offre)

    return matrice_résultat, calculer_coût(matrice_coûts, matrice_résultat)

def est_matrice_remplie_avec_valeur(mat, val):
    for ligne in mat:
        for item in ligne:
            if val != item:
                return False
    return True

