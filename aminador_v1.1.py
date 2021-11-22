import numpy as np

a_matrix = np.loadtxt("Atoms.txt")
b_matrix = np.loadtxt("Bonds.txt")
an_matrix = np.loadtxt("Angles.txt")
d_matrix = np.loadtxt("Dihedrals.txt")
i_matrix = np.loadtxt("Impropers.txt")

########################################################################################################################
#                  ETAPA DE CAMBIO DE ETIQUETAS DE ENLACES, ANGULOS Y DIEDROS A UN FORMATO UNIFICADO                   #
########################################################################################################################

i = 0
while i <= len(b_matrix) - 1:   # ENLACES
    l = 0
    j = int(b_matrix[i][2]) - 1
    k = int(b_matrix[i][3]) - 1

    while l <= len(a_matrix) - 1:
        if a_matrix[j][2] == 3 and a_matrix[k][2] == 3:
            b_matrix[i][1] = 1
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3:
            b_matrix[i][1] = 2
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 1 and a_matrix[j][2] == 3:
            b_matrix[i][1] = 2
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3:     # NUEVO
            b_matrix[i][1] = 2
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 11 and a_matrix[j][2] == 3:     # NUEVO
            b_matrix[i][1] = 2
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 4:
            b_matrix[i][1] = 3
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[j][2] == 4:
            b_matrix[i][1] = 3
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 6:
            b_matrix[i][1] = 3
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[j][2] == 6:
            b_matrix[i][1] = 3
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 2:
            b_matrix[i][1] = 4
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 1 and a_matrix[j][2] == 2:
            b_matrix[i][1] = 4
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 8:
            b_matrix[i][1] = 5
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 11 and a_matrix[j][2] == 8:
            b_matrix[i][1] = 5
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 7:
            b_matrix[i][1] = 6
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 11 and a_matrix[j][2] == 7:
            b_matrix[i][1] = 6
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 10:
            b_matrix[i][1] = 6
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 8 and a_matrix[j][2] == 10:
            b_matrix[i][1] = 6
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 1:
            b_matrix[i][1] = 7
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11:
            b_matrix[i][1] = 7
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11:
            b_matrix[i][1] = 7
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 1 and a_matrix[j][2] == 11:
            b_matrix[i][1] = 7
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 10:
            b_matrix[i][1] = 8
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 5 and a_matrix[j][2] == 10:
            b_matrix[i][1] = 8
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 7:
            b_matrix[i][1] = 8
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 5 and a_matrix[j][2] == 7:
            b_matrix[i][1] = 8
            l = len(a_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 4:
            b_matrix[i][1] = 8
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 5 and a_matrix[j][2] == 4:
            b_matrix[i][1] = 8
            l = len(a_matrix) - 1

        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 9:
            b_matrix[i][1] = 9
            l = len(a_matrix) - 1
        elif a_matrix[k][2] == 8 and a_matrix[j][2] == 9:
            b_matrix[i][1] = 9
            l = len(a_matrix) - 1

        l += 1
    i += 1

i = 0
while i <= len(an_matrix) - 1:   # ANGULOS
    m = 0
    j = int(an_matrix[i][2]) - 1
    k = int(an_matrix[i][3]) - 1
    l = int(an_matrix[i][4]) - 1

    while m <= len(a_matrix) - 1:
        if a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 1
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 1
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 1
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 1
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 6:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 6:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 4:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 4:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 6:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 4:
            an_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 2
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 7 and a_matrix[l][2] == 5:
            an_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 7 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 3
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 10 and a_matrix[l][2] == 8:
            an_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 10 and a_matrix[l][2] == 5:
            an_matrix[i][1] = 3
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 4
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 4
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 4
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 4
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 1 and a_matrix[l][2] == 2:
            an_matrix[i][1] = 5
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 5
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 1 and a_matrix[l][2] == 2:
            an_matrix[i][1] = 5
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 5
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 1 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 1 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 1 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 6
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 1 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 6
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 7:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 7:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 10 and a_matrix[k][2] == 8 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 8 and a_matrix[l][2] == 10:
            an_matrix[i][1] = 7
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 8:
            an_matrix[i][1] = 8
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 11 and a_matrix[l][2] == 1:
            an_matrix[i][1] = 8
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 8:
            an_matrix[i][1] = 8
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 11 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 8
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 9
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 9
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 6 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 10
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 11
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 2:
            an_matrix[i][1] = 12
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 12
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 8:
            an_matrix[i][1] = 13
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 13
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 8 and a_matrix[l][2] == 9:
            an_matrix[i][1] = 14
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 9 and a_matrix[k][2] == 8 and a_matrix[l][2] == 11:
            an_matrix[i][1] = 14
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 10 and a_matrix[k][2] == 8 and a_matrix[l][2] == 9:
            an_matrix[i][1] = 15
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 9 and a_matrix[k][2] == 8 and a_matrix[l][2] == 10:
            an_matrix[i][1] = 15
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 7:
            an_matrix[i][1] = 16
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 16
            m = len(an_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 4 and a_matrix[l][2] == 5:
            an_matrix[i][1] = 17
            m = len(an_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 4 and a_matrix[l][2] == 3:
            an_matrix[i][1] = 17
            m = len(an_matrix) - 1

        m += 1
    i += 1

i = 0
while i <= len(d_matrix) - 1:   # DIEDROS
    n = 0
    j = int(d_matrix[i][2]) - 1
    k = int(d_matrix[i][3]) - 1
    l = int(d_matrix[i][4]) - 1
    m = int(d_matrix[i][5]) - 1

    while n <= len(a_matrix) - 1:
        if a_matrix[k][2] == 1 and a_matrix[l][2] == 1:
            d_matrix[i][1] = 1
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 1 and a_matrix[l][2] == 11:
            d_matrix[i][1] = 1
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 11 and a_matrix[l][2] == 1:
            d_matrix[i][1] = 1
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 11 and a_matrix[l][2] == 11:
            d_matrix[i][1] = 1
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 2
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 2:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 2:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 2:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 7:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 7:
            d_matrix[i][1] = 3
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 2:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 2:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 2 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 7:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11: # NUEVO
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 7: # NUEVO
            d_matrix[i][1] = 4
            n = len(d_matrix) - 1

        elif a_matrix[k][2] == 11 and a_matrix[l][2] == 8:
            d_matrix[i][1] = 5
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 8 and a_matrix[l][2] == 11:
            d_matrix[i][1] = 5
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 8 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3:
            d_matrix[i][1] = 6
            n = len(d_matrix) - 1
        elif a_matrix[k][2] == 3 and a_matrix[l][2] ==11 and a_matrix[m][2] == 8:
            d_matrix[i][1] = 6
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 7
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 3:
            d_matrix[i][1] =8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 8
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 7 and a_matrix[l][2] == 11 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 9
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 11 and a_matrix[l][2] == 7 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 9
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 7 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 9
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 7 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 9
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 7 and a_matrix[l][2] == 11 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 9
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 11 and a_matrix[l][2] == 7 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 9
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 10
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 10
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 10
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 10
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 11
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 11
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 11
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 8 and a_matrix[m][2] == 9:
            d_matrix[i][1] = 12
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 9 and a_matrix[k][2] == 8 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 12
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 8 and a_matrix[m][2] == 10:
            d_matrix[i][1] = 12
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 10 and a_matrix[k][2] == 8 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 12
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 6 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 13
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 6 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 13
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 6 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 13
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 6 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 13
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 1 and a_matrix[k][2] == 3 and a_matrix[l][2] == 4 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 14
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 4 and a_matrix[l][2] == 3 and a_matrix[m][2] == 1:
            d_matrix[i][1] = 14
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 3 and a_matrix[l][2] == 4 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 14
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 4 and a_matrix[l][2] == 3 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 14
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 1 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 15
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 1 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 15
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 15
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 15
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 16
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 6 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 17
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 6:
            d_matrix[i][1] = 17
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 18
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 18
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 19
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 4 and a_matrix[k][2] == 3 and a_matrix[l][2] == 11 and a_matrix[m][2] == 7:
            d_matrix[i][1] = 20
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 7 and a_matrix[k][2] == 11 and a_matrix[l][2] == 3 and a_matrix[m][2] == 4:
            d_matrix[i][1] = 20
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 9 and a_matrix[k][2] == 8 and a_matrix[l][2] == 10 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 21
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 10 and a_matrix[l][2] == 8 and a_matrix[m][2] == 9:
            d_matrix[i][1] = 21
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 11 and a_matrix[k][2] == 8 and a_matrix[l][2] == 10 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 22
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 10 and a_matrix[l][2] == 8 and a_matrix[m][2] == 11:
            d_matrix[i][1] = 22
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 6 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 23
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 6 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 23
            n = len(d_matrix) - 1

        elif a_matrix[j][2] == 3 and a_matrix[k][2] == 3 and a_matrix[l][2] == 4 and a_matrix[m][2] == 5:
            d_matrix[i][1] = 24
            n = len(d_matrix) - 1
        elif a_matrix[j][2] == 5 and a_matrix[k][2] == 4 and a_matrix[l][2] == 3 and a_matrix[m][2] == 3:
            d_matrix[i][1] = 24
            n = len(d_matrix) - 1

        n += 1
    i += 1

i = 0
while i <= len(i_matrix) - 1:   # IMPROPIOS
    n = 0
    j = int(i_matrix[i][2]) - 1
    k = int(i_matrix[i][3]) - 1
    l = int(i_matrix[i][4]) - 1
    m = int(i_matrix[i][5]) - 1

    while n <= len(a_matrix) - 1:
        if a_matrix[k][2] == 9 or a_matrix[l][2] == 9 or a_matrix[l][2] == 9:
            i_matrix[i][1] = 2
        elif a_matrix[k][2] == 14 or a_matrix[l][2] == 14 or a_matrix[l][2] == 14:
            i_matrix[i][1] = 2

        else:
            i_matrix[i][1] = 1

        n += 1
    i += 1

########################################################################################################################
#         INICIO DE LA EJECUCION DEL CODIGO DE ADICION DE ALQUIL-AMINAS A OXIDO DE GRAFENO, DANDO ORIGEN               #
#              A LA FORMACION DE GRUPOS AMIDA EN LOS BORDES, Y AMINAS SECUNDARIAS EN AL PLANO BASAL                    #
########################################################################################################################

# CREACION DE MATRIZ XYZ PARA GUARDAR
#  ESTRUCTURA Y MATRIZ DE CONTADORES

xyz_matrix = [[0 for i in range(4)] for j in range(100000)]
cont_matrix = [0, 0, 0, 0, 0, 0, 0]

# CONTEO DE GRUPOS EPOXIDOS Y ACIDOS

c_e = 0
c_a = 0
i = 0
while i <= len(a_matrix)-1:
    xyz_matrix[i][1] = a_matrix[i][4]
    xyz_matrix[i][2] = a_matrix[i][5]
    xyz_matrix[i][3] = a_matrix[i][6]
    if a_matrix[i][2] == 6:
        c_e = c_e + 1
        xyz_matrix[i][0] = "O"
    elif a_matrix[i][2] == 10:
        c_a = c_a + 1
        xyz_matrix[i][0] = "O"
    elif a_matrix[i][2] == 2 or a_matrix[i][2] == 5:
        xyz_matrix[i][0] = "H"
    elif a_matrix[i][2] == 1 or a_matrix[i][2] == 3 or a_matrix[i][2] == 8 or a_matrix[i][2] == 11:
        xyz_matrix[i][0] = "C"
    else:
        xyz_matrix[i][0] = "O"
    i += 1

# REEMPLAZO DE ATOMOS DE O POR N CON
#  BASE EN LA FRACCION DE REACCION

fraccion_reaccion = float(input("Rendimiento de reacción (0 - 1): "))
longitud_cadena = float(input("Longitud de cadena carbonada (1 - n): "))

fraccion_epoxido = fraccion_reaccion * c_e
fraccion_acido = fraccion_reaccion * c_a
i = 0
j = 0
k = 0
m = 0
l = 0
while i <= len(a_matrix) - 1:
    if a_matrix[i][2] == 6:
        if j <= int(fraccion_epoxido)-1:
            if m == 0:
                a_matrix[i][2] = 88         # N de amina
                a_matrix[i][3] = -0.778
                xyz_matrix[i][0] = "N"
                j += 1
                m += 1
            elif m == 1:
                print('Saltar al siguiente átomo O')
                m = 0
    elif a_matrix[i][2] == 10:
        if k <= int(fraccion_acido)-1:
            if l == 0:
                a_matrix[i][2] = 89         # N de amida
                a_matrix[i][3] = -0.500
                xyz_matrix[i][0] = "N"
                k += 1
                l += 1
            elif l == 1:
                print('Saltar al siguiente átomo O')
                l = 0
    i += 1

cont_matrix[4] = longitud_cadena
cont_matrix[5] = fraccion_epoxido
cont_matrix[6] = fraccion_acido

# INICIALIZACION DE MATRIZ QUE CONTENDRA ATOMOS NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

if int(longitud_cadena) > 1:
    j = (7 + 3*(int(longitud_cadena) - 1))*int(fraccion_epoxido) + (4 + 3*(int(longitud_cadena - 1)))*int(fraccion_acido)
    a_new = [[0 for i in range(7)] for j in range(j)]
elif int(longitud_cadena) == 1:
    a_new = [[0 for i in range(7)] for j in range(int(10*fraccion_epoxido) + int(8*fraccion_acido) - 2)]

# INICIALIZACION DE MATRIZ QUE CONTENDRA ENLACES NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

j = (7 + 3*(int(longitud_cadena) - 1))*int(fraccion_epoxido) + (4 + 3*(int(longitud_cadena) - 1))*int(fraccion_acido)
b_new = [[0 for i in range(4)] for j in range(j)]

# INICIALIZACION DE MATRIZ QUE CONTENDRA ANGULOS NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

j = (9 + 6*(int(longitud_cadena) - 1))*int(fraccion_epoxido) + (8 + 9*(int(longitud_cadena)-1))*int(fraccion_acido)
an_new = [[0 for i in range(5)] for j in range(j)]

# INICIALIZACION DE MATRIZ QUE CONTENDRA DIEDROS NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

j = (12 + 9*(int(longitud_cadena) - 1))*int(fraccion_epoxido) + (8 + 20*(int(longitud_cadena) - 1))*int(fraccion_acido)
d_new = [[0 for i in range(6)] for j in range(j)]
if longitud_cadena == 1:
    d_new = [[0 for i in range(6)] for j in range(int(15*fraccion_epoxido) + int(12*fraccion_acido) - 4)]

###########################################
# FUNCION PARA ADICION DE H Y C1 DE AMINA #
###########################################

def ch3_gen(a_matrix, b_matrix, an_matrix, d_matrix, a_new, b_new, an_new, d_new, cont_matrix, xyz_matrix):
    new_atoms = -1
    new_bonds = -1
    new_angles = -1
    new_dihedrals = -1
    cont_amina = 0
    cont_enlaces = 0
    i = 0
    j = 0
    while i <= len(a_matrix) - 1:
        if a_matrix[i][2] == 88 and cont_amina <= int(fraccion_epoxido):
            cont_enlaces += 1
            cont_amina += 1
            while j <= len(b_matrix)-1:
                if b_matrix[j][3] == a_matrix[i][0] and cont_enlaces == 1:
                    cont_enlaces += 1
                    a_matrix[i][2] = 16                 # Atom type N amine
                    k = b_matrix[j][2]
                    a_matrix[int(k) - 1][3] = 0.183
                    b_matrix[j][1] = 12                 # Bond type N-C
                    b_tmp = b_matrix[j][2]

                    a_matrix[i][4] = a_matrix[int(k) - 1][4]
                    a_matrix[i][5] = a_matrix[int(k) - 1][5]
                    xyz_matrix[i][1] = a_matrix[i][4]
                    xyz_matrix[i][2] = a_matrix[i][5]
                    if a_matrix[i][6] < 0:
                        a_matrix[i][6] = a_matrix[int(k) - 1][6] - 1.7
                        xyz_matrix[i][3] = a_matrix[i][6]
                    elif a_matrix[i][6] > 0:
                        a_matrix[i][6] = a_matrix[int(k) - 1][6] + 1.7
                        xyz_matrix[i][3] = a_matrix[i][6]

                        # GENERACION DE ATOMOS H Y C1a Y ENLACES,
                        #  ANGULOS Y DIEDROSASOCIADOS TALES ATOMOS

                    new_atoms += 1
                    a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                    h_amina = a_new[new_atoms][0]
                    constante = a_new[new_atoms][0]
                    a_new[new_atoms][1] = 1
                    a_new[new_atoms][2] = 5                                     # Type H amine
                    a_new[new_atoms][3] = 0.383                                 # H charge
                    a_new[new_atoms][4] = a_matrix[int(k) - 1][4] + 1.0
                    a_new[new_atoms][5] = a_matrix[int(k) - 1][5]
                    a_new[new_atoms][6] = a_matrix[i][6]
                    xyz_matrix[constante][0] = "H"
                    xyz_matrix[constante][1] = a_new[new_atoms][4]
                    xyz_matrix[constante][2] = a_new[new_atoms][5]
                    xyz_matrix[constante][3] = a_new[new_atoms][6]

                    new_atoms += 1
                    a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                    constante = a_new[new_atoms][0]
                    a_new[new_atoms][1] = 1
                    a_new[new_atoms][2] = 17                                    # C amine
                    a_new[new_atoms][3] = 0.023                                 # C charge

                    a_new[new_atoms][4] = a_matrix[int(k) - 1][4]
                    a_new[new_atoms][5] = a_matrix[int(k) - 1][5]
                    if a_matrix[i][6] < 0:
                        a_new[new_atoms][6] = a_matrix[i][6] - 1.4
                    elif a_matrix[i][6] > 0:
                        a_new[new_atoms][6] = a_matrix[i][6] + 1.4
                    xyz_matrix[constante][0] = "C"
                    xyz_matrix[constante][1] = a_new[new_atoms][4]
                    xyz_matrix[constante][2] = a_new[new_atoms][5]
                    xyz_matrix[constante][3] = a_new[new_atoms][6]

                    new_bonds += 1
                    b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                    b_new[new_bonds][1] = 11                                    # H-N
                    b_new[new_bonds][2] = a_matrix[i][0]                        # N
                    b_new[new_bonds][3] = a_new[new_atoms - 1][0]               # H

                    new_bonds += 1
                    b_new[new_bonds][0] = len(b_matrix) + new_bonds
                    b_new[new_bonds][1] = 12                                    # C-N
                    b_new[new_bonds][2] = a_matrix[i][0]                        # N
                    b_new[new_bonds][3] = a_new[new_atoms][0]                   # C

                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 23                                  # H-N-C
                    an_new[new_angles][2] = a_new[new_atoms - 1][0]             # H amina
                    an_new[new_angles][3] = a_matrix[i][0]                      # N
                    an_new[new_angles][4] = a_new[new_atoms][0]                 # C amina

                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 25                                  # C_go-N-C
                    an_new[new_angles][2] = b_tmp                               # C_go
                    an_new[new_angles][3] = a_matrix[i][0]                      # N
                    an_new[new_angles][4] = a_new[new_atoms][0]                 # C

                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 23                                                   # H-N-C_go
                    an_new[new_angles][2] = b_tmp                                               # C_go
                    an_new[new_angles][3] = a_matrix[i][0]                                      # N
                    an_new[new_angles][4] = a_new[new_atoms - 1][0]                             # H amina

                    k = 1
                    l = 0
                    while k <= 3:
                        while l <= len(b_matrix) - 1:
                            if b_matrix[l][2] == b_tmp and b_matrix[l][3] != a_matrix[i][0]:
                                d_tmp = b_matrix[l][3]
                                k += 1
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 30                                    # C-C-N-C
                                d_new[new_dihedrals][2] = d_tmp                                 # C
                                d_new[new_dihedrals][3] = b_tmp                                 # C_go
                                d_new[new_dihedrals][4] = a_matrix[i][0]                        # N
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # C

                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 29
                                d_new[new_dihedrals][2] = d_tmp                                 # C
                                d_new[new_dihedrals][3] = b_tmp                                 # C_go
                                d_new[new_dihedrals][4] = a_matrix[i][0]                        # N
                                d_new[new_dihedrals][5] = a_new[new_atoms - 1][0]               # H

                            elif b_matrix[l][3] == b_tmp and b_matrix[l][2] != a_matrix[i][0]:
                                d_tmp = b_matrix[l][2]
                                k += 1
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 30                                   # C-C-N-C
                                d_new[new_dihedrals][2] = d_tmp                                 # C
                                d_new[new_dihedrals][3] = b_tmp                                 # C_go
                                d_new[new_dihedrals][4] = a_matrix[i][0]                        # N
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # C1a

                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 29
                                d_new[new_dihedrals][2] = d_tmp                                 # C
                                d_new[new_dihedrals][3] = b_tmp                                 # C_go
                                d_new[new_dihedrals][4] = a_matrix[i][0]                        # N
                                d_new[new_dihedrals][5] = a_new[new_atoms - 1][0]               # H
                            l += 1
                        l = 0
                        k += 1

                    # EXTENSION DE CADENA CARBONADA INICIANDO
                    #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

                    cont_carbono = 1
                    cont_hidrogeno = 0
                    l = 1
                    while l <= 3:
                        cont_hidrogeno += 1
                        cont_carbono += 1

                        new_atoms += 1
                        a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                        constante = a_new[new_atoms][0]
                        xyz_matrix[constante][0] = "H"
                        a_new[new_atoms][1] = 1
                        a_new[new_atoms][2] = 18
                        a_new[new_atoms][3] = 0.063
                        a_new[new_atoms][4] = a_new[new_atoms - l][4]
                        a_new[new_atoms][5] = a_new[new_atoms - l][5]

                        if cont_hidrogeno == 1:
                            a_new[new_atoms][4] = a_new[new_atoms - l][4] + 1.0
                            a_new[new_atoms][5] = a_new[new_atoms - l][5] + 1.0
                            if a_new[new_atoms - l][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] + 0.5
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] - 0.5
                        elif cont_hidrogeno == 2:
                            a_new[new_atoms][4] = a_new[new_atoms - l][4] - 1.0
                            a_new[new_atoms][5] = a_new[new_atoms - l][5] + 1.0
                            if a_new[new_atoms - l][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] + 0.5
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] - 0.5
                        else:
                            a_new[new_atoms][5] = a_new[new_atoms - l][5] - 1.0
                            if a_new[new_atoms - l][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] + 0.5
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] - 0.5

                        if longitud_cadena > 1 and cont_hidrogeno == 3:
                            a_new[new_atoms - 3][3] = 0.086
                            a_new[new_atoms][2] = 77
                            xyz_matrix[constante][0] = "C"
                            a_new[new_atoms][3] = -0.180
                            a_new[new_atoms][5] = a_new[new_atoms - l][5] - 1.0
                            if a_new[new_atoms - l][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] + 1.0
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - l][6] - 1.0

                        xyz_matrix[constante][1] = a_new[new_atoms][4]
                        xyz_matrix[constante][2] = a_new[new_atoms][5]
                        xyz_matrix[constante][3] = a_new[new_atoms][6]

                        #  ADICION DE ENLACES, ANGULOS Y
                        #  DIEDROS DE LA CADENA CARBONADA

                        # 1) Adicion de enlaces y angulos

                        if cont_hidrogeno <= 3:
                            new_bonds += 1
                            b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                            b_new[new_bonds][1] = 13                                            # H-C
                            b_new[new_bonds][2] = a_new[new_atoms - l][0]                       # C
                            b_new[new_bonds][3] = a_new[new_atoms][0]                           # H
                            new_angles += 1

                            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                            an_new[new_angles][1] = 23                                          # H-C-N
                            an_new[new_angles][2] = a_matrix[i][0]                              # N
                            an_new[new_angles][3] = a_new[new_atoms - l][0]                     # C
                            an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                            if cont_hidrogeno > 1:
                                new_angles += 1
                                an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                                an_new[new_angles][1] = 24                                      # H-C-H
                                an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                                an_new[new_angles][3] = a_new[new_atoms - l][0]                 # C
                                an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                                if cont_hidrogeno == 3:
                                    new_angles += 1
                                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                                    an_new[new_angles][1] = 24                                      # H-C-H
                                    an_new[new_angles][2] = a_new[new_atoms - 2][0]                 # H
                                    an_new[new_angles][3] = a_new[new_atoms - l][0]                 # C
                                    an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                                    if longitud_cadena > 1:
                                        b_new[new_bonds][1] = 14                                    # C-C
                                        an_new[new_angles - 2][1] = 27                              # C-C-N
                                        an_new[new_angles - 1][1] = 26                              # C-C-H
                                        an_new[new_angles][1] = 26                                  # C-C-H


                        # 2) Adicion de diedros

                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 32                                                # H-N-C-H
                        d_new[new_dihedrals][2] = h_amina                                           # H
                        d_new[new_dihedrals][3] = a_matrix[i][0]                                    # N
                        d_new[new_dihedrals][4] = a_new[new_atoms - l][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                               # H

                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 31                                                # C-N-C-H
                        d_new[new_dihedrals][2] = b_tmp                                             # C_go
                        d_new[new_dihedrals][3] = a_matrix[i][0]                                    # N
                        d_new[new_dihedrals][4] = a_new[new_atoms - l][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                               # H

                        if longitud_cadena > 1:
                            d_new[new_dihedrals - 1][1] = 29                                        # C-C-N-H
                            d_new[new_dihedrals][1] = 30                                            # C-C-N-C

                        l += 1

                    # MODIFICACION DE ANGULOS Y DIEDROS
                    #   QUE INVOLUCRAN A N DE AMINA

                    k = 0
                    while k <= len(an_matrix) - 1:
                        if an_matrix[k][2] == a_matrix[i][0] or an_matrix[k][3] == b_tmp:
                            if an_matrix[k][1] == 2:
                                an_matrix[k][1] = 18
                            #elif an_matrix[k][1] == 18:
                            #    an_matrix[k][1] = 49

                        elif an_matrix[k][4] == a_matrix[i][0] or an_matrix[k][3] == b_tmp:
                            if an_matrix[k][1] == 2:
                                an_matrix[k][1] = 18
                            #elif an_matrix[k][1] == 18:
                            #    an_matrix[k][1] = 49
                        k +=1

                    k = 0
                    while k <= len(d_matrix) - 1:
                        if d_matrix[k][2] == a_matrix[i][0] and d_matrix[k][3] == b_tmp:
                            d_matrix[k][1] = 37                                                 # N-Cgo-C-C
                        elif d_matrix[k][5] == a_matrix[i][0] and d_matrix[k][4] == b_tmp:
                            d_matrix[k][1] = 37                                                 # N-Cgo-C-C
                        elif d_matrix[k][3] == a_matrix[i][0] and d_matrix[k][4] == b_tmp:
                            d_matrix[k][1] = 29
                            d_matrix[k][2] = d_matrix[k][5]          # C
                            d_matrix[k][3] = b_tmp                   # C_go
                            d_matrix[k][4] = a_matrix[i][0]          # N
                            d_matrix[k][5] = h_amina                 # H
                        elif d_matrix[k][4] == a_matrix[i][0] and d_matrix[k][3] == b_tmp:
                            d_matrix[k][1] = 29
                            d_matrix[k][2] = d_matrix[k][2]
                            d_matrix[k][3] = b_tmp
                            d_matrix[k][4] = a_matrix[i][0]
                            d_matrix[k][5] = h_amina
                        k += 1

                elif b_matrix[j][3] == a_matrix[i][0] and cont_enlaces == 2:
                    b_matrix[j][1] = 88
                    cont_enlaces = 0

                j += 1
        j = 0
        i += 1

    cont_matrix[0] = new_atoms
    cont_matrix[1] = new_bonds
    cont_matrix[2] = new_angles
    cont_matrix[3] = new_dihedrals

    return


ch3_gen(a_matrix, b_matrix, an_matrix, d_matrix, a_new, b_new, an_new, d_new, cont_matrix, xyz_matrix)

##############################################
# ADICION DE -OH SOBRE C2 DE GRUPOS EPOXIDOS #
##############################################

new_atoms = cont_matrix[0]
new_bonds = cont_matrix[1]
new_angles = cont_matrix[2]
new_dihedrals = cont_matrix[3]
b_new = b_new
b_matrix = b_matrix
an_matrix = an_matrix
d_matrix = d_matrix

i = 0
while i <= len(a_matrix) - 1:
    if a_matrix[i][2] == 16:
        while j <= len(b_matrix)-1:
            if b_matrix[j][3] == a_matrix[i][0] and b_matrix[j][1] == 88:
                b_matrix[j][1] = 6                                          # C-O(H)
                k = b_matrix[j][2]                                          # Cgo index
                a_matrix[int(k) - 1][3] = 0.265

                new_atoms += 1
                a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                b_matrix[j][3] = a_new[new_atoms][0]
                constante = a_new[new_atoms][0]
                a_new[new_atoms][1] = 1
                a_new[new_atoms][2] = 4
                a_new[new_atoms][3] = -0.683
                xyz_matrix[constante][0] = "O"
                a_new[new_atoms][4] = a_matrix[int(k) - 1][4]
                a_new[new_atoms][5] = a_matrix[int(k) - 1][5]
                if a_matrix[i][6] > 0:
                    a_new[new_atoms][6] = a_matrix[int(k) - 1][6] - 1.4
                else:
                    a_new[new_atoms][6] = a_matrix[int(k) - 1][6] + 1.4

                xyz_matrix[constante][1] = a_new[new_atoms][4]
                xyz_matrix[constante][2] = a_new[new_atoms][5]
                xyz_matrix[constante][3] = a_new[new_atoms][6]

                new_atoms += 1
                a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                constante = a_new[new_atoms][0]
                a_new[new_atoms][1] = 1
                a_new[new_atoms][2] = 5
                a_new[new_atoms][3] = 0.418
                xyz_matrix[constante][0] = "H"
                a_new[new_atoms][4] = a_matrix[int(k) - 1][4]
                a_new[new_atoms][5] = a_matrix[int(k) - 1][5]
                if a_matrix[i][6] > 0:
                    a_new[new_atoms][6] = a_new[new_atoms - 1][6] - 1.0
                else:
                    a_new[new_atoms][6] = a_new[new_atoms - 1][6] + 1.0

                xyz_matrix[constante][1] = a_new[new_atoms][4]
                xyz_matrix[constante][2] = a_new[new_atoms][5]
                xyz_matrix[constante][3] = a_new[new_atoms][6]

                new_bonds += 1
                b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                b_new[new_bonds][1] = 8
                b_new[new_bonds][2] = a_new[new_atoms - 1][0]
                b_new[new_bonds][3] = a_new[new_atoms][0]

                k = 0
                while k <= len(an_matrix) - 1:
                    if an_matrix[k][2] == a_matrix[i][0] and an_matrix[k][3] == b_matrix[j][2]:
                        if an_matrix[k][1] == 18:
                            an_matrix[k][1] = 2                                 # N-Cgo-C
                        elif an_matrix[k][1] == 27:
                            an_matrix[k][1] = 2                                 # N-Cgo-C
                    elif an_matrix[k][4] == a_matrix[i][0] and an_matrix[k][3] == b_matrix[j][2]:
                        if an_matrix[k][1] == 18:
                            an_matrix[k][1] = 2                                 # N-Cgo-C
                        elif an_matrix[k][1] == 27:
                            an_matrix[k][1] = 2                                 # N-Cgo-C
                    elif an_matrix[k][3] == a_matrix[i][0]:
                        an_matrix[k][1] = 8                                     # Cgo-O-H
                        an_matrix[k][2] = b_matrix[j][2]                        # Cgo
                        an_matrix[k][3] = a_new[new_atoms - 1][0]               # O
                        an_matrix[k][4] = a_new[new_atoms][0]                   # H
                    k += 1

                k = 0
                while k <= len(d_matrix) - 1:
                    if d_matrix[k][2] == a_matrix[i][0] and d_matrix[k][3] == b_matrix[j][2]:
                        if d_matrix[k][1] == 11:
                            d_matrix[k][1] = 18
                        elif d_matrix[k][1] == 7:
                            d_matrix[k][1] = 10
                        elif d_matrix[k][1] == 16:
                            d_matrix[k][1] = 17
                        elif d_matrix[k][1] == 8:
                            d_matrix[k][1] = 8
                        elif d_matrix[k][1] == 17:
                            d_matrix[k][1] = 19
                    elif d_matrix[k][5] == a_matrix[i][0] and d_matrix[k][4] == b_matrix[j][2]:
                        if d_matrix[k][1] == 11:
                            d_matrix[k][1] = 18
                        elif d_matrix[k][1] == 7:
                            d_matrix[k][1] = 10
                        elif d_matrix[k][1] == 16:
                            d_matrix[k][1] = 17
                        elif d_matrix[k][1] == 8:
                            d_matrix[k][1] = 8
                        elif d_matrix[k][1] == 17:
                            d_matrix[k][1] = 19
                    elif d_matrix[k][3] == a_matrix[i][0] and d_matrix[k][4] == b_matrix[j][2]:
                        d_matrix[k][2] = a_new[new_atoms][0]
                        if d_matrix[k][1] == 23:
                            d_matrix[k][1] = 24
                        elif d_matrix[k][1] == 13:
                            d_matrix[k][1] = 14
                    elif d_matrix[k][4] == a_matrix[i][0] and d_matrix[k][3] == b_matrix[j][2]:
                        d_matrix[k][5] = a_new[new_atoms][0]
                        if d_matrix[k][1] == 23:
                            d_matrix[k][1] = 24
                        elif d_matrix[k][1] == 13:
                            d_matrix[k][1] = 14
                    k += 1
            j += 1
    j = 0
    i += 1

###########################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE ETILO #
###########################################

i = 0
while i <= len(a_new) - 1:
    if a_new[i][2] == 77:
        a_new[i][2] = 17

        # EXTENSION DE CADENA CARBONADA INICIANDO
        #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

        cont_carbono = 1
        cont_hidrogeno = 0
        l = 1
        while l <= 3:
            cont_hidrogeno += 1
            cont_carbono += 1

            new_atoms += 1
            a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
            constante = a_new[new_atoms][0]
            xyz_matrix[constante][0] = "H"
            a_new[new_atoms][1] = 1
            a_new[new_atoms][2] = 18
            a_new[new_atoms][3] = 0.060
            a_new[new_atoms][4] = a_new[i][4]
            a_new[new_atoms][5] = a_new[i][5]

            if cont_hidrogeno == 1:
                a_new[new_atoms][4] = a_new[i][4] - 1.0
                a_new[new_atoms][5] = a_new[i][5] - 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 0.5
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 0.5
            elif cont_hidrogeno == 2:
                a_new[new_atoms][4] = a_new[i][4] + 1.0
                a_new[new_atoms][5] = a_new[i][5] - 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 0.5
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 0.5
            else:
                a_new[new_atoms][5] = a_new[i][5] + 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 0.5
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 0.5

            if longitud_cadena > 2 and cont_hidrogeno == 3:
                a_new[i][3] = -0.120
                a_new[new_atoms][2] = 66
                xyz_matrix[constante][0] = "C"
                a_new[new_atoms][3] = -0.180
                a_new[new_atoms][5] = a_new[i][5] + 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 1.3
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 1.3

            xyz_matrix[constante][1] = a_new[new_atoms][4]
            xyz_matrix[constante][2] = a_new[new_atoms][5]
            xyz_matrix[constante][3] = a_new[new_atoms][6]

            #  ADICION DE ENLACES, ANGULOS Y
            #  DIEDROS DE LA CADENA CARBONADA

            # 1) Adicion de enlaces y angulos

            if cont_hidrogeno <= 3:
                new_bonds += 1
                b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                b_new[new_bonds][1] = 13                                            # C-H
                b_new[new_bonds][2] = a_new[i][0]                                   # C
                b_new[new_bonds][3] = a_new[new_atoms][0]                           # H
                new_angles += 1

                an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                an_new[new_angles][1] = 26                                          # H-C-C
                k = 0
                while k <= len(b_new) - 1:
                    if b_new[k][3] == a_new[i][0]:
                        an_new[new_angles][2] = b_new[k][2]                         # C
                        c_1 = b_new[k][2]
                    k += 1
                an_new[new_angles][3] = a_new[i][0]                                 # C
                an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                if cont_hidrogeno > 1:
                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 24                                      # H-C-H
                    an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                    an_new[new_angles][3] = a_new[i][0]                             # C
                    an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                    if cont_hidrogeno == 3:
                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 24                                  # H-C-H
                        an_new[new_angles][2] = a_new[new_atoms - 2][0]             # H
                        an_new[new_angles][3] = a_new[i][0]                         # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                 # H

                        if longitud_cadena > 2:
                            b_new[new_bonds][1] = 14  # C-C
                            an_new[new_angles - 2][1] = 11  # C-C-C
                            an_new[new_angles - 1][1] = 26  # C-C-H
                            an_new[new_angles][1] = 26  # C-C-H

            # 2) Adicion de diedros

            k = 0
            while k <= len(b_new) - 1:
                if b_new[k][1] == 12 and b_new[k][2] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 35                                    # N-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][3]                           # N
                    d_new[new_dihedrals][3] = c_1                                   # C
                    d_new[new_dihedrals][4] = a_new[i][0]                           # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                elif b_new[k][1] == 12 and b_new[k][3] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 35                                    # N-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][2]                           # N
                    d_new[new_dihedrals][3] = c_1                                   # C
                    d_new[new_dihedrals][4] = a_new[i][0]                           # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                elif b_new[k][1] == 13 and b_new[k][2] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 34                                    # H-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][3]                           # H
                    d_new[new_dihedrals][3] = c_1                                   # C
                    d_new[new_dihedrals][4] = a_new[i][0]                           # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                elif b_new[k][1] == 13 and b_new[k][3] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 34                                    # H-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][2]                           # H
                    d_new[new_dihedrals][3] = c_1                                   # C
                    d_new[new_dihedrals][4] = a_new[i][0]                           # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H
                k += 1

            if int(longitud_cadena) > 2:
                if d_new[new_dihedrals - 1][1] == 35:
                    d_new[new_dihedrals - 1][1] = 37                                # N-C-C-C

                elif d_new[new_dihedrals - 1][1] == 34:
                    d_new[new_dihedrals - 1][1] = 36                                # H-C-C-C

                elif d_new[new_dihedrals][1] == 35:
                    d_new[new_dihedrals][1] = 37                                    # N-C-C-C

                elif d_new[new_dihedrals][1] == 34:
                    d_new[new_dihedrals][1] = 36                                    # H-C-C-C
            l += 1
    i += 1

#############################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE PROPILO #
#############################################
if longitud_cadena >= 3:
    i = 0
    while i <= len(a_new) - 1:
        if a_new[i][2] == 66:
            a_new[i][2] = 17

            # EXTENSION DE CADENA CARBONADA INICIANDO
            #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

            cont_carbono = 1
            cont_hidrogeno = 0
            l = 1
            while l <= 3:
                cont_hidrogeno += 1
                cont_carbono += 1

                new_atoms += 1
                a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                constante = a_new[new_atoms][0]
                xyz_matrix[constante][0] = "H"
                a_new[new_atoms][1] = 1
                a_new[new_atoms][2] = 18
                a_new[new_atoms][3] = 0.060
                a_new[new_atoms][4] = a_new[i][4]
                a_new[new_atoms][5] = a_new[i][5]

                if cont_hidrogeno == 1:
                    a_new[new_atoms][4] = a_new[i][4] + 1.0
                    a_new[new_atoms][5] = a_new[i][5] + 1.0
                    if a_new[i][6] > 0:
                        a_new[new_atoms][6] = a_new[i][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[i][6] - 0.5
                elif cont_hidrogeno == 2:
                    a_new[new_atoms][4] = a_new[i][4] - 1.0
                    a_new[new_atoms][5] = a_new[i][5] + 1.0
                    if a_new[i][6] > 0:
                        a_new[new_atoms][6] = a_new[i][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[i][6] - 0.5
                else:
                    a_new[new_atoms][5] = a_new[i][5] - 1.0
                    if longitud_cadena == 3:
                        if a_new[i][6] > 0:
                            a_new[new_atoms][6] = a_new[i][6] + 0.5
                        else:
                            a_new[new_atoms][6] = a_new[i][6] - 0.5
                    else:
                        a_new[new_atoms][2] = 17
                        xyz_matrix[constante][0] = "C"
                        a_new[new_atoms][3] = -0.180

                        a_new[new_atoms][4] = a_new[i][4]
                        if a_new[i][6] > 0:
                            a_new[new_atoms][6] = a_new[i][6] + 1.3
                        else:
                            a_new[new_atoms][6] = a_new[i][6] - 1.3

                        if cont_carbono < longitud_cadena:
                            a_new[new_atoms][3] = -0.120
                            a_new[i][3] = -0.120
                        elif cont_carbono == longitud_cadena:
                            a_new[new_atoms][3] = -0.180
                            a_new[i][3] = -0.120

                xyz_matrix[constante][1] = a_new[new_atoms][4]
                xyz_matrix[constante][2] = a_new[new_atoms][5]
                xyz_matrix[constante][3] = a_new[new_atoms][6]

                #  ADICION DE ENLACES, ANGULOS Y
                #  DIEDROS DE LA CADENA CARBONADA

                # 1) Adicion de enlaces y angulos

                if cont_hidrogeno <= 3:
                    new_bonds += 1
                    b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                    b_new[new_bonds][1] = 13                                            # C-H
                    b_new[new_bonds][2] = a_new[i][0]                                   # C
                    b_new[new_bonds][3] = a_new[new_atoms][0]                           # H

                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 26                                          # H-C-C
                    k = 0
                    while k <= len(b_new) - 1:
                        if b_new[k][3] == a_new[i][0]:
                            an_new[new_angles][2] = b_new[k][2]                         # C
                            c_1 = b_new[k][2]
                        k += 1
                    an_new[new_angles][3] = a_new[i][0]                                 # C
                    an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                    if cont_hidrogeno > 1:
                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 24                                      # H-C-H
                        an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                        an_new[new_angles][3] = a_new[i][0]                             # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                        if cont_hidrogeno == 3:
                            new_angles += 1
                            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                            an_new[new_angles][1] = 24                                  # H-C-H
                            an_new[new_angles][2] = a_new[new_atoms - 2][0]             # H
                            an_new[new_angles][3] = a_new[i][0]                         # C
                            an_new[new_angles][4] = a_new[new_atoms][0]                 # H

                            if longitud_cadena > 3:
                                b_new[new_bonds][1] = 14                                # C-C
                                an_new[new_angles - 2][1] = 11                          # C-C-C
                                an_new[new_angles - 1][1] = 26                          # C-C-H
                                an_new[new_angles][1] = 26                              # C-C-H

                # 2) Adicion de diedros

                k = 0
                while k <= len(b_new) - 1:
                    if b_new[k][1] == 12 and b_new[k][2] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 36                                    # C-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][3]                           # C
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                    elif b_new[k][1] == 12 and b_new[k][3] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 36                                    # C-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][2]                           # C
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                    elif b_new[k][1] == 13 and b_new[k][2] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 34                                    # H-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][3]                           # H
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                    elif b_new[k][1] == 13 and b_new[k][3] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 34                                    # H-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][2]                           # H
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H
                    k += 1

                if longitud_cadena > 3 and cont_carbono <= longitud_cadena:
                    if d_new[new_dihedrals - 1][1] == 36:
                        d_new[new_dihedrals - 1][1] = 38                                # C-C-C-C

                    elif d_new[new_dihedrals - 1][1] == 34:
                        d_new[new_dihedrals - 1][1] = 36                                # H-C-C-C

                    elif d_new[new_dihedrals][1] == 36:
                        d_new[new_dihedrals][1] = 38                                    # C-C-C-C

                    elif d_new[new_dihedrals][1] == 34:
                        d_new[new_dihedrals][1] = 36                                    # H-C-C-C
                l += 1

            if longitud_cadena > 3:
                cont_carbono = 3
                cont_hidrogeno = 0
                k = 1
                while k <= 3:
                    cont_hidrogeno += 1

                    new_atoms += 1
                    a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                    constante = a_new[new_atoms][0]
                    xyz_matrix[constante][0] = "H"
                    a_new[new_atoms][1] = 1
                    a_new[new_atoms][2] = 18
                    a_new[new_atoms][3] = 0.060
                    a_new[new_atoms][4] = a_new[new_atoms - k][4]
                    a_new[new_atoms][5] = a_new[new_atoms - k][5]

                    if cont_hidrogeno == 1:
                        z = k
                        a_new[new_atoms][4] = a_new[new_atoms - k][4] + 1.0
                        a_new[new_atoms][5] = a_new[new_atoms - k][5] + 1.0
                        if a_new[new_atoms - k][6] > 0:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.5
                        else:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.5
                    elif cont_hidrogeno == 2:
                        z = k
                        a_new[new_atoms][4] = a_new[new_atoms - k][4] - 1.0
                        a_new[new_atoms][5] = a_new[new_atoms - k][5] + 1.0
                        if a_new[new_atoms - k][6] > 0:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.5
                        else:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.5
                    else:
                        cont_carbono += 1
                        a_new[new_atoms][5] = a_new[new_atoms - k][5] - 1.0
                        if cont_carbono < longitud_cadena - 1:
                            a_new[new_atoms][2] = 17
                            xyz_matrix[constante][0] = "C"
                            a_new[new_atoms][3] = -0.120
                            if a_new[new_atoms - k][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] + 1.3
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] - 1.3
                            z = k
                            k = 0
                            cont_hidrogeno = 0

                        elif cont_carbono == longitud_cadena - 1:
                            a_new[new_atoms - k][3] = -0.120
                            a_new[new_atoms][2] = 17
                            xyz_matrix[constante][0] = "C"
                            a_new[new_atoms][3] = -0.180
                            a_new[new_atoms][4] = a_new[new_atoms - k][4]
                            if a_new[new_atoms - k][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.8
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.8
                            z = k
                            k = 0
                            cont_hidrogeno = 0

                        elif cont_carbono == longitud_cadena:
                            z = k
                            a_new[new_atoms][4] = a_new[new_atoms - k][4]
                            if a_new[new_atoms - k][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.8
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.8

                    xyz_matrix[constante][1] = a_new[new_atoms][4]
                    xyz_matrix[constante][2] = a_new[new_atoms][5]
                    xyz_matrix[constante][3] = a_new[new_atoms][6]

                    #  ADICION DE ENLACES, ANGULOS Y
                    #  DIEDROS DE LA CADENA CARBONADA

                    # 1) Adicion de enlaces y angulos

                    if cont_hidrogeno <= 3:
                        new_bonds += 1
                        b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                        b_new[new_bonds][1] = 13                                            # C-H
                        b_new[new_bonds][2] = a_new[new_atoms - z][0]                       # C
                        b_new[new_bonds][3] = a_new[new_atoms][0]                           # H
                        if a_new[new_atoms - z][3] == -0.120 and a_new[new_atoms][3] == -0.180:
                            b_new[new_bonds][1] = 14

                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 26                                          # H-C-C
                        m = 0
                        while m <= len(b_new) - 1:
                            if b_new[m][3] == a_new[new_atoms - z][0]:
                                if b_new[m][2] != a_new[new_atoms][0]:
                                    an_new[new_angles][2] = b_new[m][2]                         # C
                                    c_1 = b_new[m][2]
                            m += 1
                        an_new[new_angles][3] = a_new[new_atoms - z][0]                     # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                        if cont_hidrogeno > 1:
                            new_angles += 1
                            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                            an_new[new_angles][1] = 24                                      # H-C-H
                            an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                            an_new[new_angles][3] = a_new[new_atoms - z][0]                 # C
                            an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                            if cont_hidrogeno == 3:
                                new_angles += 1
                                an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                                an_new[new_angles][1] = 24                                  # H-C-H
                                an_new[new_angles][2] = a_new[new_atoms - 2][0]             # H
                                an_new[new_angles][3] = a_new[new_atoms - z][0]             # C
                                an_new[new_angles][4] = a_new[new_atoms][0]                 # H

                                if longitud_cadena > cont_carbono:
                                    b_new[new_bonds][1] = 14                                # C-C
                                    an_new[new_angles - 2][1] = 11                          # C-C-C
                                    an_new[new_angles - 1][1] = 26                          # C-C-H
                                    an_new[new_angles][1] = 26                              # C-C-H

                    # 2) Adicion de diedros

                    m = 0
                    while m <= len(b_new) - 1:
                        if b_new[m][1] == 14 and b_new[m][2] == c_1:
                            if b_new[m][3] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 36                                    # C-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][3]                           # C
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                        elif b_new[m][1] == 14 and b_new[m][3] == c_1:
                            if b_new[m][2] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 36                                    # C-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][2]                           # C
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                        elif b_new[m][1] == 13 and b_new[m][2] == c_1:
                            if b_new[m][3] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 34                                    # H-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][3]                           # H
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                        elif b_new[m][1] == 13 and b_new[m][3] == c_1:
                            if b_new[m][2] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 34                                    # H-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][2]                           # H
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H
                        m += 1

                    if longitud_cadena >= cont_carbono and cont_hidrogeno == 3:
                        if d_new[new_dihedrals - 1][1] == 36:
                            d_new[new_dihedrals - 1][1] = 38

                        elif d_new[new_dihedrals - 1][1] == 34:
                            d_new[new_dihedrals - 1][1] = 36

                        elif d_new[new_dihedrals][1] == 36:
                            d_new[new_dihedrals][1] = 38

                        elif d_new[new_dihedrals][1] == 34:
                            d_new[new_dihedrals][1] = 36
                    k += 1
        i += 1

print("¡Empezamos con las amidas!")

###########################################
# FUNCION PARA ADICION DE H Y C1 DE AMIDA #
###########################################

def amida_gen(a_matrix, b_matrix, an_matrix, d_matrix, a_new, b_new, an_new, d_new, cont_matrix, new_atoms, new_bonds,
          new_angles, new_dihedrals):
    cont_amida = 0
    i = 0
    while i <= len(a_matrix) - 1:
        if a_matrix[i][2] == 89 and cont_amida <= int(fraccion_acido):
            cont_amida += 1
            a_matrix[i][2] = 14
            a_matrix[i][3] = -0.500

            new_atoms += 1
            a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
            constante = a_new[new_atoms][0]
            xyz_matrix[constante][0] = "C"
            a_new[new_atoms][1] = 1
            a_new[new_atoms][2] = 17
            a_new[new_atoms][3] = 0.02

            a_new[new_atoms][4] = a_matrix[i][4]
            a_new[new_atoms][5] = a_matrix[i][5]
            if a_matrix[i][6] > 0:
                a_new[new_atoms][6] = a_matrix[i][6] + 1.3
            else:
                a_new[new_atoms][6] = a_matrix[i][6] - 1.3

            xyz_matrix[constante][1] = a_new[new_atoms][4]
            xyz_matrix[constante][2] = a_new[new_atoms][5]
            xyz_matrix[constante][3] = a_new[new_atoms][6]

            new_bonds += 1
            b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
            b_new[new_bonds][1] = 10                                                    # C-N
            b_new[new_bonds][2] = a_matrix[i][0]                                        # N
            b_new[new_bonds][3] = a_new[new_atoms][0]                                   # C

            new_angles += 1
            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
            an_new[new_angles][1] = 20                                                  # C-N-H
            m = 0
            while m <= len(b_matrix) - 1:
                if b_matrix[m][1] == 8 and b_matrix[m][2] == a_matrix[i][0]:
                    an_new[new_angles][2] = b_matrix[m][3]                              # H
                    b_matrix[m][1] = 11                                                 # H-N
                elif b_matrix[m][1] == 8 and b_matrix[m][3] == a_matrix[i][0]:
                    an_new[new_angles][2] = b_matrix[m][2]                              # H
                    b_matrix[m][1] = 11                                                 # H-N
                m += 1
            an_new[new_angles][3] = a_matrix[i][0]                                      # N
            an_new[new_angles][4] = a_new[new_atoms][0]                                 # C1
            h_amida = an_new[new_angles][2]
            a_matrix[int(h_amida) - 1][3] = 0.300                                       # H

            new_angles += 1
            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
            an_new[new_angles][1] = 25                                                  # C-N-C
            m = 0
            while m <= len(b_matrix) - 1:
                if b_matrix[m][2] == a_matrix[i][0] and b_matrix[m][3] != h_amida:
                    an_new[new_angles][2] = b_matrix[m][3]                              # C(O)
                elif b_matrix[m][3] == a_matrix[i][0] and b_matrix[m][2] != h_amida:
                    an_new[new_angles][2] = b_matrix[m][2]                              # C(O)
                m += 1
            an_new[new_angles][3] = a_matrix[i][0]                                      # N
            an_new[new_angles][4] = a_new[new_atoms][0]                                 # C1
            c_amida = an_new[new_angles][2]
            a_matrix[int(c_amida) - 1][3] = 0.615

            new_dihedrals += 1
            d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
            d_new[new_dihedrals][1] = 33                                                # O-C-N-C1
            m = 0
            while m <= len(b_matrix) - 1:
                if b_matrix[m][2] == c_amida and b_matrix[m][1] == 9:
                    d_new[new_dihedrals][2] = b_matrix[m][3]                            # O
                elif b_matrix[m][3] == c_amida and b_matrix[m][1] == 9:
                    d_new[new_dihedrals][2] = b_matrix[m][2]                            # O
                m += 1
            d_new[new_dihedrals][3] = c_amida                                           # C(O)
            d_new[new_dihedrals][4] = a_matrix[i][0]                                    # N
            d_new[new_dihedrals][5] = a_new[new_atoms][0]                               # C1
            o_amida = d_new[new_dihedrals][2]
            a_matrix[int(o_amida) - 1][3] = -0.500

            new_dihedrals += 1
            d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
            d_new[new_dihedrals][1] = 30                                               # C_go-C-N-C1
            m = 0
            while m <= len(b_matrix) - 1:
                if b_matrix[m][2] == c_amida and b_matrix[m][1] == 5:
                    d_new[new_dihedrals][2] = b_matrix[m][3]                            # C_go
                elif b_matrix[m][3] == c_amida and b_matrix[m][1] == 5:
                    d_new[new_dihedrals][2] = b_matrix[m][2]                            # C_go
                m += 1
            cgo_amida = d_new[new_dihedrals][2]
            d_new[new_dihedrals][3] = c_amida                                           # C(O)
            d_new[new_dihedrals][4] = a_matrix[i][0]                                    # N
            d_new[new_dihedrals][5] = a_new[new_atoms][0]                               # C1

            # EXTENSION DE CADENA CARBONADA INICIANDO
            #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

            cont_carbono = 1
            cont_hidrogeno = 0
            l = 1
            while l <= 3:
                cont_hidrogeno += 1
                cont_carbono += 1

                new_atoms += 1
                a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                constante = a_new[new_atoms][0]
                xyz_matrix[constante][0] = "H"
                a_new[new_atoms][1] = 1
                a_new[new_atoms][2] = 18
                a_new[new_atoms][3] = 0.060
                a_new[new_atoms][4] = a_new[new_atoms - l][4]
                a_new[new_atoms][5] = a_new[new_atoms][5]

                if cont_hidrogeno == 1:
                    a_new[new_atoms][4] = a_new[new_atoms - l][4] - 1.0
                    a_new[new_atoms][5] = a_new[new_atoms - l][5] - 1.0
                    if a_new[new_atoms - l][6] > 0:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] - 0.5
                elif cont_hidrogeno == 2:
                    a_new[new_atoms][4] = a_new[new_atoms - l][4] + 1.0
                    a_new[new_atoms][5] = a_new[new_atoms - l][5] - 1.0
                    if a_new[new_atoms - l][6] > 0:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] - 0.5
                else:
                    a_new[new_atoms][5] = a_new[new_atoms - l][5] + 1.0
                    if a_new[new_atoms - l][6] > 0:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] - 0.5

                if longitud_cadena > 1 and cont_hidrogeno == 3:
                    a_new[new_atoms - l][3] = 0.08
                    a_new[new_atoms][2] = 97
                    xyz_matrix[constante][0] = "C"
                    a_new[new_atoms][3] = -0.180
                    a_new[new_atoms][5] = a_new[new_atoms - l][5] + 1.0
                    if a_new[new_atoms - l][6] > 0:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] + 1.3
                    else:
                        a_new[new_atoms][6] = a_new[new_atoms - l][6] - 1.3

                xyz_matrix[constante][1] = a_new[new_atoms][4]
                xyz_matrix[constante][2] = a_new[new_atoms][5]
                xyz_matrix[constante][3] = a_new[new_atoms][6]

                #  ADICION DE ENLACES, ANGULOS Y
                #  DIEDROS DE LA CADENA CARBONADA

                # 1) Adicion de enlaces y angulos

                if cont_hidrogeno <= 3:
                    new_bonds += 1
                    b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                    b_new[new_bonds][1] = 13
                    b_new[new_bonds][2] = a_new[new_atoms - l][0]                       # C
                    b_new[new_bonds][3] = a_new[new_atoms][0]                           # H

                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 23                                          # H-C-N
                    an_new[new_angles][2] = a_matrix[i][0]                              # N
                    an_new[new_angles][3] = a_new[new_atoms - l][0]                     # C1
                    an_new[new_angles][4] = a_new[new_atoms][0]                         # H1

                    if cont_hidrogeno > 1:
                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 23                                      # H-C-H
                        an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                        an_new[new_angles][3] = a_new[new_atoms - l][0]                 # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                     # H2

                        if cont_hidrogeno == 3:
                            cont_hidrogeno = 0
                            new_angles += 1
                            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                            an_new[new_angles][1] = 24                                 # H-C-H
                            an_new[new_angles][2] = a_new[new_atoms - 2][0]             # H
                            an_new[new_angles][3] = a_new[new_atoms - l][0]             # C
                            an_new[new_angles][4] = a_new[new_atoms][0]                 # H3

                            if longitud_cadena > 1:
                                b_new[new_bonds][1] = 14                                # C-C
                                an_new[new_angles - 2][1] = 18                          # C-C-N
                                an_new[new_angles - 1][1] = 26                          # C-C-H
                                an_new[new_angles][1] = 26                              # C-C-H

                # 2) Adicion de diedros
                new_dihedrals += 1
                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                d_new[new_dihedrals][1] = 32                                       # H-N-C-H
                d_new[new_dihedrals][2] = h_amida                                   # H
                d_new[new_dihedrals][3] = a_matrix[i][0]                            # N
                d_new[new_dihedrals][4] = a_new[new_atoms - l][0]                   # C1
                d_new[new_dihedrals][5] = a_new[new_atoms][0]                       # H

                new_dihedrals += 1
                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                d_new[new_dihedrals][1] = 31                                       # C-N-C-H
                d_new[new_dihedrals][2] = c_amida                                   # C(O)
                d_new[new_dihedrals][3] = a_matrix[i][0]                            # N
                d_new[new_dihedrals][4] = a_new[new_atoms - l][0]                   # C1
                d_new[new_dihedrals][5] = a_new[new_atoms][0]                       # H

                if longitud_cadena > 1:
                    d_new[new_dihedrals - 1][1] = 29                               # C-C-N-H
                    d_new[new_dihedrals][1] = 30                                   # C-C-N-C

                l += 1

            # MODIFICACION DE ANGULOS Y DIEDROS
            #   QUE INVOLUCRAN A N DE AMINA

            k = 0
            while k <= len(an_matrix) - 1:
                if an_matrix[k][1] == 3 and an_matrix[k][3] == a_matrix[i][0]:
                    an_matrix[k][1] = 20
                elif an_matrix[k][1] == 15 and an_matrix[k][2] == a_matrix[i][0]:
                    an_matrix[k][1] = 19
                elif an_matrix[k][1] == 15 and an_matrix[k][4] == a_matrix[i][0]:
                    an_matrix[k][1] = 19
                elif an_matrix[k][1] == 7 and an_matrix[k][2] == a_matrix[i][0]:
                    an_matrix[k][1] = 18
                elif an_matrix[k][1] == 7 and an_matrix[k][4] == a_matrix[i][0]:
                    an_matrix[k][1] = 18
                k += 1

            k = 0
            while k <= len(d_matrix) - 1:
                if d_matrix[k][1] == 22 and d_matrix[k][3] == a_matrix[i][0]:
                    d_matrix[k][1] = 27
                elif d_matrix[k][1] == 22 and d_matrix[k][4] == a_matrix[i][0]:
                    d_matrix[k][1] = 27
                elif d_matrix[k][1] == 21 and d_matrix[k][3] == a_matrix[i][0]:
                    d_matrix[k][1] = 28
                elif d_matrix[k][1] == 21 and d_matrix[k][4] == a_matrix[i][0]:
                    d_matrix[k][1] = 28
                k += 1

        i += 1

    cont_matrix[0] = new_atoms
    cont_matrix[1] = new_bonds
    cont_matrix[2] = new_angles
    cont_matrix[3] = new_dihedrals

    return


amida_gen(a_matrix, b_matrix, an_matrix, d_matrix, a_new, b_new, an_new, d_new, cont_matrix, new_atoms, new_bonds,
          new_angles, new_dihedrals)



###########################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE ETILO #
###########################################

new_atoms = cont_matrix[0]
new_bonds = cont_matrix[1]
new_angles = cont_matrix[2]
new_dihedrals = cont_matrix[3]
b_new = b_new
b_matrix = b_matrix
an_matrix = an_matrix
d_matrix = d_matrix
i = 0
while i <= len(a_new) - 1:
    if a_new[i][2] == 97:
        a_new[i][2] = 17

        # EXTENSION DE CADENA CARBONADA INICIANDO
        #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

        cont_carbono = 1
        cont_hidrogeno = 0
        l = 1
        while l <= 3:
            cont_hidrogeno += 1
            cont_carbono += 1
            new_atoms += 1
            a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
            constante = a_new[new_atoms][0]
            xyz_matrix[constante][0] = "H"
            a_new[new_atoms][1] = 1
            a_new[new_atoms][2] = 18
            a_new[new_atoms][3] = 0.060
            a_new[new_atoms][4] = a_new[i][4]
            a_new[new_atoms][5] = a_new[i][5]

            if cont_hidrogeno == 1:
                a_new[new_atoms][4] = a_new[i][4] + 1.0
                a_new[new_atoms][5] = a_new[i][5] + 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 0.5
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 0.5
            elif cont_hidrogeno == 2:
                a_new[new_atoms][4] = a_new[i][4] - 1.0
                a_new[new_atoms][5] = a_new[i][5] + 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 0.5
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 0.5
            else:
                a_new[new_atoms][5] = a_new[i][5] - 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 0.5
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 0.5

            if longitud_cadena > 2 and cont_hidrogeno == 3:
                a_new[i][3] = -0.120
                a_new[new_atoms][2] = 66
                xyz_matrix[constante][0] = "C"
                a_new[new_atoms][3] = -0.180
                a_new[new_atoms][5] = a_new[i][5] + 1.0
                if a_new[i][6] > 0:
                    a_new[new_atoms][6] = a_new[i][6] + 1.3
                else:
                    a_new[new_atoms][6] = a_new[i][6] - 1.3

            xyz_matrix[constante][1] = a_new[new_atoms][4]
            xyz_matrix[constante][2] = a_new[new_atoms][5]
            xyz_matrix[constante][3] = a_new[new_atoms][6]

            #  ADICION DE ENLACES, ANGULOS Y
            #  DIEDROS DE LA CADENA CARBONADA

            # 1) Adicion de enlaces y angulos

            if cont_hidrogeno <= 3:
                new_bonds += 1
                b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                b_new[new_bonds][1] = 13                                              # C-H
                b_new[new_bonds][2] = a_new[i][0]                                     # C
                b_new[new_bonds][3] = a_new[new_atoms][0]                             # H
                new_angles += 1

                an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                an_new[new_angles][1] = 26                                            # H-C-C
                k = 0
                while k <= len(b_new) - 1:
                    if b_new[k][3] == a_new[i][0]:
                        an_new[new_angles][2] = b_new[k][2]  # C
                        c_1 = b_new[k][2]
                    k += 1
                an_new[new_angles][3] = a_new[i][0]  # C
                an_new[new_angles][4] = a_new[new_atoms][0]  # H

                if cont_hidrogeno > 1:
                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 24                                          # H-C-H
                    an_new[new_angles][2] = a_new[new_atoms - 1][0]                     # H
                    an_new[new_angles][3] = a_new[i][0]                                 # C
                    an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                    if cont_hidrogeno == 3:
                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 24                                      # H-C-H
                        an_new[new_angles][2] = a_new[new_atoms - 2][0]                 # H
                        an_new[new_angles][3] = a_new[i][0]                             # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                        if longitud_cadena > 2:
                            b_new[new_bonds][1] = 14                                    # C-C
                            an_new[new_angles - 2][1] = 11                              # C-C-C
                            an_new[new_angles - 1][1] = 26                              # C-C-H
                            an_new[new_angles][1] = 26                                  # C-C-H

            # 2) Adicion de diedros

            k = 0
            while k <= len(b_new) - 1:
                if b_new[k][1] == 10 and b_new[k][2] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 35                                        # N-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][3]                               # N
                    d_new[new_dihedrals][3] = c_1                                       # C
                    d_new[new_dihedrals][4] = a_new[i][0]                               # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                       # H

                elif b_new[k][1] == 10 and b_new[k][3] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 35                                        # N-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][2]                               # N
                    d_new[new_dihedrals][3] = c_1                                       # C
                    d_new[new_dihedrals][4] = a_new[i][0]                               # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                       # H

                elif b_new[k][1] == 13 and b_new[k][2] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 34                                        # H-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][3]                               # H
                    d_new[new_dihedrals][3] = c_1                                       # C
                    d_new[new_dihedrals][4] = a_new[i][0]                               # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                       # H

                elif b_new[k][1] == 13 and b_new[k][3] == c_1:
                    new_dihedrals += 1
                    d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                    d_new[new_dihedrals][1] = 34                                        # H-C-C-H
                    d_new[new_dihedrals][2] = b_new[k][2]                               # H
                    d_new[new_dihedrals][3] = c_1                                       # C
                    d_new[new_dihedrals][4] = a_new[i][0]                               # C
                    d_new[new_dihedrals][5] = a_new[new_atoms][0]                       # H
                k += 1

            if int(longitud_cadena) > 2:
                if d_new[new_dihedrals - 1][1] == 35:
                    d_new[new_dihedrals - 1][1] = 37

                elif d_new[new_dihedrals - 1][1] == 34:
                    d_new[new_dihedrals - 1][1] = 36

                elif d_new[new_dihedrals][1] == 35:
                    d_new[new_dihedrals][1] = 37

                elif d_new[new_dihedrals][1] == 34:
                    d_new[new_dihedrals][1] = 36
            l += 1
    i += 1

#############################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE PROPILO #
#############################################

if longitud_cadena >= 3:
    i = 0
    while i <= len(a_new) - 1:
        if a_new[i][2] == 66:
            a_new[i][2] = 17

            # EXTENSION DE CADENA CARBONADA INICIANDO
            #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

            cont_carbono = 1
            cont_hidrogeno = 0
            l = 1
            while l <= 3:
                cont_hidrogeno += 1
                cont_carbono += 1

                new_atoms += 1
                a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                constante = a_new[new_atoms][0]
                xyz_matrix[constante][0] = "H"
                a_new[new_atoms][1] = 1
                a_new[new_atoms][2] = 18
                a_new[new_atoms][3] = 0.060
                a_new[new_atoms][4] = a_new[i][4]
                a_new[new_atoms][5] = a_new[i][5]

                if cont_hidrogeno == 1:
                    a_new[new_atoms][4] = a_new[i][4] + 1.0
                    a_new[new_atoms][5] = a_new[i][5] + 1.0
                    if a_new[i][6] > 0:
                        a_new[new_atoms][6] = a_new[i][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[i][6] - 0.5
                elif cont_hidrogeno == 2:
                    a_new[new_atoms][4] = a_new[i][4] - 1.0
                    a_new[new_atoms][5] = a_new[i][5] + 1.0
                    if a_new[i][6] > 0:
                        a_new[new_atoms][6] = a_new[i][6] + 0.5
                    else:
                        a_new[new_atoms][6] = a_new[i][6] - 0.5
                else:
                    a_new[new_atoms][5] = a_new[i][5] - 1.0
                    if longitud_cadena == 3:
                        if a_new[i][6] > 0:
                            a_new[new_atoms][6] = a_new[i][6] + 0.5
                        else:
                            a_new[new_atoms][6] = a_new[i][6] - 0.5
                    else:
                        a_new[new_atoms][2] = 17
                        xyz_matrix[constante][0] = "C"
                        a_new[new_atoms][3] = -0.180

                        a_new[new_atoms][4] = a_new[i][4]
                        if a_new[i][6] > 0:
                            a_new[new_atoms][6] = a_new[i][6] + 1.3
                        else:
                            a_new[new_atoms][6] = a_new[i][6] - 1.3

                        if cont_carbono < longitud_cadena:
                            a_new[new_atoms][3] = -0.120
                            a_new[i][3] = -0.120
                        elif cont_carbono == longitud_cadena:
                            a_new[new_atoms][3] = -0.180
                            a_new[i][3] = -0.120

                xyz_matrix[constante][1] = a_new[new_atoms][4]
                xyz_matrix[constante][2] = a_new[new_atoms][5]
                xyz_matrix[constante][3] = a_new[new_atoms][6]

                #  ADICION DE ENLACES, ANGULOS Y
                #  DIEDROS DE LA CADENA CARBONADA

                # 1) Adicion de enlaces y angulos

                if cont_hidrogeno <= 3:
                    new_bonds += 1
                    b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                    b_new[new_bonds][1] = 13                                            # H-C
                    b_new[new_bonds][2] = a_new[i][0]                                   # C
                    b_new[new_bonds][3] = a_new[new_atoms][0]                           # H

                    new_angles += 1
                    an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                    an_new[new_angles][1] = 26                                          # H-C-C
                    k = 0
                    while k <= len(b_new) - 1:
                        if b_new[k][3] == a_new[i][0]:
                            an_new[new_angles][2] = b_new[k][2]                         # C
                            c_1 = b_new[k][2]
                        k += 1
                    an_new[new_angles][3] = a_new[i][0]                                 # C
                    an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                    if cont_hidrogeno > 1:
                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 24                                      # H-C-H
                        an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                        an_new[new_angles][3] = a_new[i][0]                             # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                        if cont_hidrogeno == 3:
                            new_angles += 1
                            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                            an_new[new_angles][1] = 24                                  # H-C-H
                            an_new[new_angles][2] = a_new[new_atoms - 2][0]             # H
                            an_new[new_angles][3] = a_new[i][0]                         # C
                            an_new[new_angles][4] = a_new[new_atoms][0]                 # H

                            if longitud_cadena > 3:
                                b_new[new_bonds][1] = 14                                # C-C
                                an_new[new_angles - 2][1] = 11                          # C-C-C
                                an_new[new_angles - 1][1] = 26                          # C-C-H
                                an_new[new_angles][1] = 26                              # C-C-H

                # 2) Adicion de diedros

                k = 0
                while k <= len(b_new) - 1:
                    if b_new[k][1] == 10 and b_new[k][2] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 36                                   # C-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][3]                           # C
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                    elif b_new[k][1] == 10 and b_new[k][3] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 36                                   # C-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][2]                           # C
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                    elif b_new[k][1] == 13 and b_new[k][2] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 34                                   # H-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][3]                           # H
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                    elif b_new[k][1] == 13 and b_new[k][3] == c_1:
                        new_dihedrals += 1
                        d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                        d_new[new_dihedrals][1] = 34                                   # H-C-C-H
                        d_new[new_dihedrals][2] = b_new[k][2]                           # H
                        d_new[new_dihedrals][3] = c_1                                   # C
                        d_new[new_dihedrals][4] = a_new[i][0]                           # C
                        d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H
                    k += 1

                if longitud_cadena > 3 and cont_carbono <= longitud_cadena:
                    if d_new[new_dihedrals - 1][1] == 117:
                        d_new[new_dihedrals - 1][1] = 119

                    elif d_new[new_dihedrals - 1][1] == 115:
                        d_new[new_dihedrals - 1][1] = 117

                    elif d_new[new_dihedrals][1] == 117:
                        d_new[new_dihedrals][1] = 119

                    elif d_new[new_dihedrals][1] == 115:
                        d_new[new_dihedrals][1] = 117
                l += 1

            if longitud_cadena > 3:
                cont_carbono = 3
                cont_hidrogeno = 0
                k = 1
                while k <= 3:
                    cont_hidrogeno += 1

                    new_atoms += 1
                    a_new[new_atoms][0] = len(a_matrix) + new_atoms + 1
                    constante = a_new[new_atoms][0]
                    xyz_matrix[constante][0] = "H"
                    a_new[new_atoms][1] = 1
                    a_new[new_atoms][2] = 18
                    a_new[new_atoms][3] = 0.060
                    a_new[new_atoms][4] = a_new[new_atoms - k][4]
                    a_new[new_atoms][5] = a_new[new_atoms - k][5]

                    if cont_hidrogeno == 1:
                        z = k
                        a_new[new_atoms][4] = a_new[new_atoms - k][4] + 1.0
                        a_new[new_atoms][5] = a_new[new_atoms - k][5] + 1.0
                        if a_new[new_atoms - k][6] > 0:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.5
                        else:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.5
                    elif cont_hidrogeno == 2:
                        z = k
                        a_new[new_atoms][4] = a_new[new_atoms - k][4] - 1.0
                        a_new[new_atoms][5] = a_new[new_atoms - k][5] + 1.0
                        if a_new[new_atoms - k][6] > 0:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.5
                        else:
                            a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.5
                    else:
                        cont_carbono += 1
                        a_new[new_atoms][5] = a_new[new_atoms - k][5] - 1.0
                        if cont_carbono < longitud_cadena - 1:
                            a_new[new_atoms][2] = 17
                            xyz_matrix[constante][0] = "C"
                            a_new[new_atoms][3] = -0.120
                            if a_new[new_atoms - k][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] + 1.3
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] - 1.3
                            z = k
                            k = 0
                            cont_hidrogeno = 0

                        elif cont_carbono == longitud_cadena - 1:
                            a_new[new_atoms - k][3] = -0.120
                            a_new[new_atoms][2] = 17
                            xyz_matrix[constante][0] = "C"
                            a_new[new_atoms][3] = -0.180
                            a_new[new_atoms][4] = a_new[new_atoms - k][4]
                            if a_new[new_atoms - k][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.8
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.8
                            z = k
                            k = 0
                            cont_hidrogeno = 0

                        elif cont_carbono == longitud_cadena:
                            z = k
                            a_new[new_atoms][4] = a_new[new_atoms - k][4]
                            if a_new[new_atoms - k][6] > 0:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] + 0.8
                            else:
                                a_new[new_atoms][6] = a_new[new_atoms - k][6] - 0.8

                    xyz_matrix[constante][1] = a_new[new_atoms][4]
                    xyz_matrix[constante][2] = a_new[new_atoms][5]
                    xyz_matrix[constante][3] = a_new[new_atoms][6]

                    #  ADICION DE ENLACES, ANGULOS Y
                    #  DIEDROS DE LA CADENA CARBONADA

                    # 1) Adicion de enlaces y angulos

                    if cont_hidrogeno <= 3:
                        new_bonds += 1
                        b_new[new_bonds][0] = len(b_matrix) + new_bonds + 1
                        b_new[new_bonds][1] = 13
                        b_new[new_bonds][2] = a_new[new_atoms - z][0]                       # C
                        b_new[new_bonds][3] = a_new[new_atoms][0]                           # H
                        if a_new[new_atoms - z][3] == -0.120 and a_new[new_atoms][3] == -0.180:
                            b_new[new_bonds][1] = 14

                        new_angles += 1
                        an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                        an_new[new_angles][1] = 26                                          # H-C-C
                        m = 0
                        while m <= len(b_new) - 1:
                            if b_new[m][3] == a_new[new_atoms - z][0]:
                                if b_new[m][2] != a_new[new_atoms][0]:
                                    an_new[new_angles][2] = b_new[m][2]                         # C
                                    c_1 = b_new[m][2]
                            m += 1
                        an_new[new_angles][3] = a_new[new_atoms - z][0]                     # C
                        an_new[new_angles][4] = a_new[new_atoms][0]                         # H

                        if cont_hidrogeno > 1:
                            new_angles += 1
                            an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                            an_new[new_angles][1] = 24
                            # H-C-H
                            an_new[new_angles][2] = a_new[new_atoms - 1][0]                 # H
                            an_new[new_angles][3] = a_new[new_atoms - z][0]                 # C
                            an_new[new_angles][4] = a_new[new_atoms][0]                     # H

                            if cont_hidrogeno == 3:
                                new_angles += 1
                                an_new[new_angles][0] = len(an_matrix) + new_angles + 1
                                an_new[new_angles][1] = 24                                  # H-C-H
                                an_new[new_angles][2] = a_new[new_atoms - 2][0]             # H
                                an_new[new_angles][3] = a_new[new_atoms - z][0]             # C
                                an_new[new_angles][4] = a_new[new_atoms][0]                 # H

                                if longitud_cadena > cont_carbono:
                                    b_new[new_bonds][1] = 14                                # C-C
                                    an_new[new_angles - 2][1] = 11                          # C-C-C
                                    an_new[new_angles - 1][1] = 26                          # C-C-H
                                    an_new[new_angles][1] = 26                              # C-C-H

                    # 2) Adicion de diedros

                    m = 0
                    while m <= len(b_new) - 1:
                        if b_new[m][1] == 14 and b_new[m][2] == c_1:
                            if b_new[m][3] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 36                                   # C-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][3]                           # C
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                        elif b_new[m][1] == 14 and b_new[m][3] == c_1:
                            if b_new[m][2] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 36                                   # C-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][2]                           # C
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                        elif b_new[m][1] == 13 and b_new[m][2] == c_1:
                            if b_new[m][3] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 34                                   # H-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][3]                           # H
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H

                        elif b_new[m][1] == 13 and b_new[m][3] == c_1:
                            if b_new[m][2] != a_new[new_atoms - z][0]:
                                new_dihedrals += 1
                                d_new[new_dihedrals][0] = len(d_matrix) + new_dihedrals + 1
                                d_new[new_dihedrals][1] = 34                                   # H-C-C-H
                                d_new[new_dihedrals][2] = b_new[m][2]                           # H
                                d_new[new_dihedrals][3] = c_1                                   # C
                                d_new[new_dihedrals][4] = a_new[new_atoms - z][0]               # C
                                d_new[new_dihedrals][5] = a_new[new_atoms][0]                   # H
                        m += 1

                    if longitud_cadena >= cont_carbono and cont_hidrogeno == 3:
                        if d_new[new_dihedrals - 1][1] == 36:
                            d_new[new_dihedrals - 1][1] = 38

                        elif d_new[new_dihedrals - 1][1] == 34:
                            d_new[new_dihedrals - 1][1] = 36

                        elif d_new[new_dihedrals][1] == 36:
                            d_new[new_dihedrals][1] = 38

                        elif d_new[new_dihedrals][1] == 34:
                            d_new[new_dihedrals][1] = 36
                    k += 1
        i += 1

xyz_file = open('a-GO.xyz', 'w')
print(int(len(a_matrix) + new_atoms + 2), '\n', file=xyz_file)
i = 0
while i <= len(xyz_matrix) - 1:
    print(xyz_matrix[i][0], xyz_matrix[i][1], xyz_matrix[i][2], xyz_matrix[i][3],sep=' ',file = xyz_file)
    i += 1
xyz_file.close()

########################################################################################################################
#                               CREACCION DEL ARCHIVO TOPOLOGICO DATA FILE                                             #
########################################################################################################################

data_file = open('data_file.txt', 'w')
print('# Modelo de GO funcionalizado con alquil-aminas', file=data_file)
print('XXXX', 'atoms', file=data_file)
print('XXXX', 'bonds', file=data_file)
print('XXXX', 'angles', file=data_file)
print('XXXX', 'dihedrals', file=data_file)
print('XXXX', 'impropers','\n', file=data_file)

print(18, 'atom types', file=data_file)
print(14, 'bond types', file=data_file)
print(27, 'angle types', file=data_file)
print(38, 'dihedral types', file=data_file)
print(2, 'improper types', '\n', file=data_file)

print(-100, 100, 'xlo xhi', file=data_file)
print(-100, 100, 'ylo yhi', file=data_file)
print(-100, 100, 'zlo zhi', '\n', file=data_file)

print(' Masses', '\n', file=data_file)
print('1       12.011', file=data_file)
print('2       1.008', file=data_file)
print('3       12.011', file=data_file)
print('4       15.999', file=data_file)
print('5       1.008', file=data_file)
print('6       15.999', file=data_file)
print('7       15.999', file=data_file)
print('8       12.011', file=data_file)
print('9       15.999', file=data_file)
print('10      15.999', file=data_file)
print('11      12.011', file=data_file)
print('12      12.011', file=data_file)
print('13      15.999', file=data_file)
print('14      14.007', file=data_file)
print('15      12.011', file=data_file)
print('16      14.007', file=data_file)
print('17      12.011', file=data_file)
print('18      1.008', '\n', file=data_file)

print(' Pair Coeffs', '\n', file=data_file)
print('1       0.07    3.55', file=data_file)
print('2       0.03    2.42', file=data_file)
print('3       0.066   3.5', file=data_file)
print('4       0.17    3.12', file=data_file)
print('5       0.0     0.0', file=data_file)
print('6       0.14    2.9', file=data_file)
print('7       0.17    3.07', file=data_file)
print('8       0.105   3.75', file=data_file)
print('9       0.21    2.96', file=data_file)
print('10      0.17    3.0', file=data_file)
print('11      0.07    3.55', file=data_file)
print('12      0.105   3.75', file=data_file)
print('13      0.21    2.96', file=data_file)
print('14      0.17    3.25', file=data_file)
print('15      0.066   3.5', file=data_file)
print('16      0.17    3.3', file=data_file)
print('17      0.066   3.5', file=data_file)
print('18      0.03    2.5', '\n', file=data_file)

print(' Bond Coeffs', '\n', file=data_file)
print('1       268.0   1.529', file=data_file)
print('2       317.0   1.51', file=data_file)
print('3       320.0   1.41', file=data_file)
print('4       367.0   1.08', file=data_file)
print('5       400.0   1.49', file=data_file)
print('6       450.0   1.364', file=data_file)
print('7       469.0   1.4', file=data_file)
print('8       553.0   0.945', file=data_file)
print('9       570.0   1.229', file=data_file)
print('10      490.0   1.335', file=data_file)
print('11      434.0   1.01', file=data_file)
print('12      382.0   1.448', file=data_file)
print('13      340.0   1.09', file=data_file)
print('14      268.0   1.529', '\n', file=data_file)

print(' Angle Coeffs', '\n', file=data_file)
print('1       40.0    109.5', file=data_file)
print('2       50.0    109.5', file=data_file)
print('3       35.0    113.0', file=data_file)
print('4       63.0    114.5', file=data_file)
print('5       35.0    120.0', file=data_file)
print('6       63.0    120.0', file=data_file)
print('7       70.0    120.0', file=data_file)
print('8       85.0    120.0', file=data_file)
print('9       70.0    130.0', file=data_file)
print('10      60.0    109.5', file=data_file)
print('11      58.35   112.7', file=data_file)
print('12      35.0    117.0', file=data_file)
print('13      70.0    119.7', file=data_file)
print('14      80.0    120.4', file=data_file)
print('15      80.0    121.0', file=data_file)
print('16      70.0    123.0', file=data_file)
print('17      55.0    108.5', file=data_file)
print('18      56.2    109.5', file=data_file)
print('19      70.0    115.5', file=data_file)
print('20      35.0    119.8', file=data_file)
print('21      35.88   120.0', file=data_file)
print('22      43.6    106.4', file=data_file)
print('23      35.0    109.5', file=data_file)
print('24      33.0    107.8', file=data_file)
print('25      51.8    107.2', file=data_file)
print('26      37.5    110.7', file=data_file)
print('27      56.2    109.5', '\n', file=data_file)

print(' Dihedral Coeffs', '\n', file=data_file)
print('1       0.0     7.25    0.0     0.0 ', file=data_file)
print('2       0.0     0.0     0.0     0.0 ', file=data_file)
print('3       0.0     0.0     0.468   0.0 ', file=data_file)
print('4       0.0     -8.0    0.0     0.0 ', file=data_file)
print('5       0.0     2.1     0.0     0.0 ', file=data_file)
print('6       0.5     0.0     0.0     0.0 ', file=data_file)
print('7      -4.344  -1.714  0.0     0.0  ', file=data_file)
print('8       1.711   -0.5    0.663   0.0 ', file=data_file)
print('9       0.0     1.682   0.0     0.0 ', file=data_file)
print('10      0.0     0.0     0.366   0.0 ', file=data_file)
print('11      1.3     -0.05   0.2     0.0 ', file=data_file)
print('12      0.9     0.23    -0.505  0.0 ', file=data_file)
print('13     -0.521  -2.018    1.996   0.0', file=data_file)
print('14      -0.9    0.0     0.0     0.0 ', file=data_file)
print('15      2.817   -0.169  0.543   0.0 ', file=data_file)
print('16      -0.55   0.0     0.0     0.0 ', file=data_file)
print('17      4.319   0.0     0.0     0.0 ', file=data_file)
print('18      -1.552  0.0     0.0     0.0 ', file=data_file)
print('19      9.508   0.0     0.0     0.0 ', file=data_file)
print('20      0.0     0.0     0.318   0.0 ', file=data_file)
print('21      0.0     5.0     0.0     0.0 ', file=data_file)
print('22      4.0     5.0     0.0     0.0 ', file=data_file)
print('23      0.65    -0.25   0.67    0.0 ', file=data_file)
print('24      -0.356  -0.174  0.492   0.0 ', file=data_file)
print('25     0.798  -0.371   0.674  -1.1  ', file=data_file)
print('26     0.0     0.0     0.0     0.0  ', file=data_file)
print('27     4.9     0.0    -4.9     0.0  ', file=data_file)
print('28     4.9     0.0    -4.9     0.0  ', file=data_file)
print('29     -0.303  0.722   0.417  -0.836', file=data_file)
print('30      0.428  0.834   0.128  -1.39 ', file=data_file)
print('31      0.28   0.84    0.0    -1.12 ', file=data_file)
print('32      0.2    0.6     0.0    -0.8  ', file=data_file)
print('33      6.089  0.0    -6.089   0.0  ', file=data_file)
print('34      0.15   0.45    0.0    -0.6  ', file=data_file)
print('35     -0.979  1.216   0.709  -0.946', file=data_file)
print('36      0.15   0.45    0.0    -0.6  ', file=data_file)
print('37      0.797 -0.371   0.674  -1.1  ', file=data_file)
print('38      0.7   -0.35    0.05   -0.4  ', '\n', file=data_file)

print(' Improper Coeffs', '\n', file=data_file)
print('1       5.0     180.0', file=data_file)
print('2      15.0     180.0', '\n', file=data_file)

print('Atoms', '\n', file=data_file)

i = 0
while i <= len(a_matrix) - 1:
    print(int(a_matrix[i][0]), int(a_matrix[i][1]), int(a_matrix[i][2]), a_matrix[i][3], a_matrix[i][4], a_matrix[i][5],
          a_matrix[i][6],sep='   ',file=data_file)
    i += 1

i = 0
while i <= len(a_new) - 1:
    if a_new[i][0] != 0:
        print(int(a_new[i][0]),int(a_new[i][1]),int(a_new[i][2]),a_new[i][3],a_new[i][4],a_new[i][5],a_new[i][6], sep='   ',
          file=data_file)
    else:
        i = len(a_new) - 1
    i += 1

print('\n', 'Bonds', '\n', file=data_file)

i = 0
while i <= len(b_matrix) - 1:
    print(int(b_matrix[i][0]), int(b_matrix[i][1]), int(b_matrix[i][2]), int(b_matrix[i][3]), sep=' ', file=data_file)
    i += 1

i = 0
while i <= len(b_new) - 1:
    if b_new[i][0] != 0:
        print(int(b_new[i][0]),int(b_new[i][1]),int(b_new[i][2]),int(b_new[i][3]),sep=' ', file=data_file)
    else:
        i = len(b_new) - 1
    i += 1

print('\n', 'Angles', '\n', file=data_file)
i = 0
while i <= len(an_matrix) - 1:
    print(int(an_matrix[i][0]), int(an_matrix[i][1]), int(an_matrix[i][2]), int(an_matrix[i][3]), int(an_matrix[i][4]),
          sep=' ', file=data_file)
    i += 1

i = 0
while i <= len(an_new) - 1:
    if an_new[i][0] != 0:
        print(int(an_new[i][0]), int(an_new[i][1]), int(an_new[i][2]), int(an_new[i][3]), int(an_new[i][4]), sep=' ',
          file=data_file)
    else:
        i = len(an_new) - 1
    i += 1

print('\n', 'Dihedrals', '\n', file=data_file)
i = 0
while i <= len(d_matrix) - 1:
    print(int(d_matrix[i][0]), int(d_matrix[i][1]), int(d_matrix[i][2]), int(d_matrix[i][3]), int(d_matrix[i][4]),
          int(d_matrix[i][5]), sep=' ', file=data_file)
    i += 1

i = 0
while i <= len(d_new) - 1:
    if d_new[i][0] != 0:
        print(int(d_new[i][0]), int(d_new[i][1]), int(d_new[i][2]), int(d_new[i][3]), int(d_new[i][4]),
              int(d_new[i][5]),sep=' ', file=data_file)
    else:
        i = len(d_new) - 1
    i += 1

print('\n', 'Impropers', '\n', file=data_file)
i = 0
while i <= len(i_matrix) - 1:
    print(int(i_matrix[i][0]), int(i_matrix[i][1]), int(i_matrix[i][2]), int(i_matrix[i][3]), int(i_matrix[i][4]),
              int(i_matrix[i][5]),sep=' ', file=data_file)
    i += 1
data_file.close()

print('¡Hemos terminado!')
