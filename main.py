
from fonction import *
from Hammer import *
import sys
#sys.stderr = open('errors.txt', 'w')

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
    solution, cout_total=North_Ouest1(file_path)
    print(solution)
    print('cout total : ',cout_total)
    Affichage_North_Ouest(matrice,solution,colonne,ligne)
    mes_lignes, mes_colonnes, tpmmatrice = read_constraints('file1.txt')
    matrice2, offre, demande = extraction_mat(tpmmatrice)
    penalites = calculPenalites(matrice2, demande, offre)
    res_matrix = initMatriceResultat(matrice2)
    print('Balas Hammer')
    mat_sol,cout = transport(matrice2, demande, offre)
    print('cout = ',cout)
    Affichage_North_Ouest(matrice, mat_sol, colonne, ligne)
