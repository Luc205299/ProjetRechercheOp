from copy import deepcopy
import numpy as np
from fonction import *

def calculPenalites(cost, demande, offre):
    demande_penalites = []
    offre_penalites = []

    for i in range(len(cost)):
        if offre[i] == 0:
            offre_penalites.append(-1)
        else:
            ligne_copy = deepcopy(cost[i])
            ligne_copy.sort()
            if ligne_copy[1] == float('inf'):
                ligne_copy[1] = ligne_copy[0]
                ligne_copy[0] = 0
            offre_penalites.append(ligne_copy[1] - ligne_copy[0])

    for j in range(len(cost[0])):
        if demande[j] == 0:
            demande_penalites.append(-1)
        else:
            colonne = []
            for i in range(len(cost)):
                colonne.append(cost[i][j])
            colonne.sort()
            if colonne[1] == float('inf'):
                colonne[1] = colonne[0]
                colonne[0] = 0
            demande_penalites.append(colonne[1] - colonne[0])

    return {
        'demande_penalites': demande_penalites,
        'offre_penalites': offre_penalites
    }

def recupMaxPenalites(penalites):
    max = 0
    index = 0
    a_envoyer = True

    for penalite in range(len(penalites['demande_penalites'])):
        value = penalites['demande_penalites'][penalite]
        if value > max:
            index = penalite
            max = value

    for penalite in range(len(penalites['offre_penalites'])):
        value = penalites['offre_penalites'][penalite]
        if value > max:
            index = penalite
            max = value
            a_envoyer = False

    return {
        'max': max,
        'a_envoyer': a_envoyer,
        'index': index
    }

def initMatriceResultat(cost):
    return np.zeros((len(cost), len(cost[0])), dtype=int)

def transportViaPenaliteMax(penaliteMax, matriceCouts, demande, offre, matriceResultat):
    indexPenaliteMax = penaliteMax['index']

    if penaliteMax['a_envoyer']:
        min = matriceCouts[0][indexPenaliteMax]
        indexMin = 0
        for index in range(len(matriceCouts)):
            if min > matriceCouts[index][indexPenaliteMax]:
                min = matriceCouts[index][indexPenaliteMax]
                indexMin = index

        if offre[indexMin] >= demande[indexPenaliteMax]:
            offre[indexMin] -= demande[indexPenaliteMax]
            matriceResultat[indexMin][indexPenaliteMax] = demande[indexPenaliteMax]
            demande[indexPenaliteMax] = 0
            for index in range(len(matriceCouts)):
                matriceCouts[index][indexPenaliteMax] = float("inf")
        else:
            demande[indexPenaliteMax] -= offre[indexMin]
            matriceResultat[indexMin][indexPenaliteMax] = offre[indexMin]
            offre[indexMin] = 0
            for index in range(len(matriceCouts[indexMin])):
                matriceCouts[indexMin][index] = float("inf")

    else:
        min = matriceCouts[indexPenaliteMax][0]
        indexMin = 0
        for index in range(len(matriceCouts[indexPenaliteMax])):
            if min > matriceCouts[indexPenaliteMax][index]:
                min = matriceCouts[indexPenaliteMax][index]
                indexMin = index

        if demande[indexMin] >= offre[indexPenaliteMax]:
            demande[indexMin] -= offre[indexPenaliteMax]
            matriceResultat[indexPenaliteMax][indexMin] = offre[indexPenaliteMax]
            offre[indexPenaliteMax] = 0
            for index in range(len(matriceCouts[indexPenaliteMax])):
                matriceCouts[indexPenaliteMax][index] = float("inf")
        else:
            offre[indexPenaliteMax] -= demande[indexMin]
            matriceResultat[indexPenaliteMax][indexMin] = demande[indexMin]
            demande[indexMin] = 0
            for index in range(len(matriceCouts)):
                matriceCouts[index][indexMin] = float("inf")

def cost_calculation(matriceCouts, matriceResultat):
    coutTotal = 0
    for i in range(len(matriceCouts)):
        for j in range(len(matriceCouts[0])):
            coutTotal += matriceCouts[i][j] * matriceResultat[i][j]
    return coutTotal

def isMatrixFilledWithValue(mat, val):
    for row in mat:
        for item in row:
            if val != item:
                return False
    return True

def transport(matriceCouts, demande, offre):
    penalites = calculPenalites(matriceCouts, demande, offre)
    matriceResultat = initMatriceResultat(matriceCouts)
    couts_copy = deepcopy(matriceCouts)

    while not isMatrixFilledWithValue(couts_copy, float('inf')):
        penaliteMax = recupMaxPenalites(penalites)
        transportViaPenaliteMax(penaliteMax, couts_copy, demande, offre, matriceResultat)
        penalites = calculPenalites(couts_copy, demande, offre)

    return matriceResultat, cost_calculation(matriceCouts, matriceResultat)