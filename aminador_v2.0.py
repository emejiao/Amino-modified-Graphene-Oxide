import numpy as np
import os
import json
from random import randint

# ABRIR DATA FILE DE MAKEGRAPHITICS
name = input("Nombre del datafile: ")
with open(name, "r") as data:
    topology = data.readlines()

# IDENTIFICAR LAS LINEAS DONDE ESTAN LOS DATOS
i = 0
for line in topology:
    i += 1
    name = list(line)
    if "Atoms" in line:
        atoms_line = i  # Atom list is at line i
    elif "Bonds" in line:
        bonds_line = i  # Bond list is at line i
    elif "Angles" in line:
        angles_line = i  # Angle list is at line i
    elif "Dihedrals" in line:
        dihedrals_line = i  # Dihedral list is at line i
    elif "Impropers" in line:
        impropers_line = i  # Improper list is at line i

# GUARDAR MATRÍZ DE ÁTOMOS
i = 0
with open("atoms_tmp.txt", "w") as atoms:
    for line in topology:
        i += 1
        if atoms_line + 2 <= i <= bonds_line - 2:
            atoms.write(line)

# GUARDAR MATRÍZ DE ENLACES
i = 0
with open("bonds_tmp.txt", "w") as bonds:
    for line in topology:
        i += 1
        if bonds_line + 2 <= i <= angles_line - 2:
            bonds.write(line)

# GUARDAR MATRÍZ DE ÁNGULOS
i = 0
with open("angles_tmp.txt", "w") as angles:
    for line in topology:
        i += 1
        if angles_line + 2 <= i <= dihedrals_line - 2:
            angles.write(line)

# GUARDAR MATRÍZ DE DIEDROS
i = 0
with open("dihedrals_tmp.txt", "w") as dihedrals:
    for line in topology:
        i += 1
        if dihedrals_line + 2 <= i <= impropers_line - 2:
            dihedrals.write(line)

# GUARDAR MATRÍZ DE IMPROPIOS
i = 0
with open("impropers_tmp.txt", "w") as impropers:
    for line in topology:
        i += 1
        if impropers_line + 2 <= i <= len(topology):
            impropers.write(line)

# LECTURA DE MATRICES CON NUMPY
atoms_array = np.loadtxt("atoms_tmp.txt")
bonds_array = np.loadtxt("bonds_tmp.txt")
angles_array = np.loadtxt("angles_tmp.txt")
dihedrals_array = np.loadtxt("dihedrals_tmp.txt")
impropers_array = np.loadtxt("impropers_tmp.txt")

os.remove("atoms_tmp.txt")
os.remove("bonds_tmp.txt")
os.remove("angles_tmp.txt")
os.remove("dihedrals_tmp.txt")
os.remove("impropers_tmp.txt")

print("* Generación de arreglos numpy --> COMPLETADA")

########################################################################################################################
#                                  RE-ETIQUETADO DE TIPOS DE ENLACES, ÁNGULOS Y DIEDROS                                #
########################################################################################################################

# LECTURA DE DICCIONARIO DE TIPOS DE ENLACES, ÁNGULOS Y DIEDROS

with open("type_dict.json", "r") as dictionary:
    types_dict = json.load(dictionary)

# GENERACIÓN DE TUPLAS DE ENLACES

tuple_bonds = []
i = 0
for bond in bonds_array:
    nitrogen = atoms_array[int(bonds_array[i][2]) - 1][2]
    a2 = atoms_array[int(bonds_array[i][3])-1][2]
    tuple_bond = str((int(nitrogen), int(a2)))
    tuple_bonds.append(tuple_bond)
    i += 1

# GENERACIÓN DE TUPLAS DE ÁNGULOS

tuple_angles = []
i = 0
for angle in angles_array:
    nitrogen = atoms_array[int(angles_array[i][2]) - 1][2]
    a2 = atoms_array[int(angles_array[i][3])-1][2]
    a3 = atoms_array[int(angles_array[i][4])-1][2]
    tuple_angle = str((int(nitrogen), int(a2), int(a3)))
    tuple_angles.append(tuple_angle)
    i += 1

# GENERACIÓN DE TUPLAS DE DIEDROS

tuple_dihedrals = []
i = 0
for dihedral in dihedrals_array:
    nitrogen = atoms_array[int(dihedrals_array[i][2]) - 1][2]
    a2 = atoms_array[int(dihedrals_array[i][3])-1][2]
    a3 = atoms_array[int(dihedrals_array[i][4])-1][2]
    a4 = atoms_array[int(dihedrals_array[i][5])-1][2]
    tuple_dihedral = str((int(nitrogen), int(a2), int(a3), int(a4)))
    tuple_dihedrals.append(tuple_dihedral)
    i += 1

# BUSQUEDA DE ENLACE EN EL DICCIONARIO Y RE-ETIQUETADO

i = 0
for tuple_b in tuple_bonds:
    if tuple_b in types_dict[0]["Bonds"]:
        bonds_array[i][1] = int(types_dict[0]["Bonds"][tuple_b])
        i += 1
    else:
        print("Enlace no encontrado:", tuple_b, bonds_array[i][2:5])

# BUSQUEDA DE ÁNGULOS EN EL DICCIONARIO Y RE-ETIQUETADO

i = 0
for tuple_a in tuple_angles:
    if tuple_a in types_dict[1]["Angles"]:
        angles_array[i][1] = int(types_dict[1]["Angles"][tuple_a])
        i += 1
    else:
        print("Ángulo no encontrado:", tuple_a, angles_array[i][2:5])

# BUSQUEDA DE DIEDRO EN EL DICCIONARIO Y RE-ETIQUETADO

i = 0
for tuple_d in tuple_dihedrals:
    if tuple_d in types_dict[2]["Dihedrals"]:
        dihedrals_array[i][1] = int(types_dict[2]["Dihedrals"][tuple_d])
        i += 1
    else:
        print("Diedro no encontrado:", tuple_d, dihedrals_array[i][2:5])

# RE-ETIQUETADO DE IMPROPIOS

i = 0
for improper in impropers_array:
    a2 = atoms_array[int(impropers_array[i][3] - 1)][2]
    a3 = atoms_array[int(impropers_array[i][4] - 1)][2]
    a4 = atoms_array[int(impropers_array[i][5] - 1)][2]
    if a2 == 9 or a3 == 9 or a4 == 9:
        impropers_array[i][1] = 2
    else:
        impropers_array[i][1] = 1
    i += 1

print("* Re-etiquetado de tipos --> COMPLETADA", "\n")

########################################################################################################################
#         INICIO DE LA EJECUCION DEL CODIGO DE ADICION DE ALQUIL-AMINAS A OXIDO DE GRAFENO, DANDO ORIGEN               #
#              A LA FORMACION DE GRUPOS AMIDA EN LOS BORDES, Y AMINAS SECUNDARIAS EN AL PLANO BASAL                    #
########################################################################################################################

# CREACION DE MATRIZ XYZ PARA GUARDAR
#  ESTRUCTURA Y MATRIZ DE CONTADORES

xyz_matrix = [[0 for i in range(4)] for j in range(500000)]
cont_matrix = [0, 0, 0, 0, 0, 0, 0]

epoxy_array = []
carboxy_array = []

# CONTEO DE GRUPOS EPOXIDOS Y ACIDOS

c_e, c_a, x_max, y_max, i = 0, 0, 0, 0, 0
for atom in atoms_array:
    xyz_matrix[i][1:4] = atoms_array[i][4:7]
    #xyz_matrix[i][2] = atoms_array[i][5]
    #xyz_matrix[i][3] = atoms_array[i][6]
    if atoms_array[i][2] == 6:
        c_e = c_e + 1
        xyz_matrix[i][0] = "O"
        epoxy_array.append(int(atoms_array[i][0]))
    elif atoms_array[i][2] == 10:
        c_a = c_a + 1
        xyz_matrix[i][0] = "O"
        carboxy_array.append(int(atoms_array[i][0]))
    elif atoms_array[i][2] == 2 or atoms_array[i][2] == 5:
        xyz_matrix[i][0] = "H"
    elif atoms_array[i][2] == 1 or atoms_array[i][2] == 3 or atoms_array[i][2] == 8 or atoms_array[i][2] == 11:
        xyz_matrix[i][0] = "C"
    else:
        xyz_matrix[i][0] = "O"
    if atoms_array[i][4] > x_max:
        x_max = atoms_array[i][4]
    if atoms_array[i][5] > y_max:
        y_max = atoms_array[i][5]
    i += 1

# REEMPLAZO DE ATOMOS DE O POR N CON
#  BASE EN LA FRACCION DE REACCION

print("#############################################################")
print("INTRODUCIR DATOS DEL SISTEMA")
reactive_fraction = float(input("Rendimiento de reacción (0 - 1): "))
chain_length = float(input("Longitud de cadena carbonada (1 - n): "))

epoxy_fraction = int(reactive_fraction * c_e)
carboxy_fraction = int(reactive_fraction * c_a)
print("* Número de anillos de epóxido que experimentan aminación:", epoxy_fraction)
print("* Número de ácidos carboxílicos que experimentan amidación:", carboxy_fraction)
print("#############################################################", "\n")

list_epoxy = []
i = 0
while i < epoxy_fraction:
    random = randint(0, len(epoxy_array)-1)
    if random not in list_epoxy:
        list_epoxy.append(random)
        atoms_array[epoxy_array[random]-1][2:4] = 88, -0.778  # N de amida
        xyz_matrix[epoxy_array[random]-1][0] = "N"
        i += 1

list_carboxy = []
i = 0
while i < carboxy_fraction:
    random = randint(0, len(carboxy_array)-1)
    if random not in list_carboxy:
        list_carboxy.append(random)
        atoms_array[carboxy_array[random]-1][2:4] = 89, -0.500  # N de amida
        xyz_matrix[carboxy_array[random]-1][0] = "N"
        i += 1

print("* Asignación de epoxidos y ácidos que reaccionarán --> COMPLETADA", "\n")

# INICIALIZACION DE MATRIZ QUE CONTENDRA ATOMOS NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

if int(chain_length) > 1:
    j = (7 + 3 * (int(chain_length) - 1)) * epoxy_fraction + \
        (4 + 3 * (int(chain_length) - 1)) * carboxy_fraction
    atoms_new = [[0 for i in range(7)] for j in range(j)]
elif int(chain_length) == 1:
    atoms_new = [[0 for i in range(7)] for j in range(int(10 * epoxy_fraction) + int(8 * carboxy_fraction) - 2)]

# INICIALIZACION DE MATRIZ QUE CONTENDRA ENLACES NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

j = (7 + 3 * (int(chain_length) - 1)) * int(epoxy_fraction) + \
    (4 + 3 * (int(chain_length) - 1)) * int(carboxy_fraction)
bonds_new = [[0 for i in range(4)] for j in range(j)]

# INICIALIZACION DE MATRIZ QUE CONTENDRA ANGULOS NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

j = (9 + 6 * (int(chain_length) - 1)) * int(epoxy_fraction) + (8 + 9 * (int(chain_length) - 1)) \
    * int(carboxy_fraction)
angles_new = [[0 for i in range(5)] for j in range(j)]

# INICIALIZACION DE MATRIZ QUE CONTENDRA DIEDROS NUEVOS
#    ASOCIADOS AL GRUPO -NHR AMINA Y -C(O)NHR AMIDA

j = (12 + 9 * (int(chain_length) - 1)) * int(epoxy_fraction) + (8 + 20 * (int(chain_length) - 1)) \
    * int(carboxy_fraction)
dihedrals_new = [[0 for i in range(6)] for j in range(j)]
if chain_length == 1:
    dihedrals_new = [[0 for i in range(6)] for j in range(int(15 * epoxy_fraction) + int(12 * carboxy_fraction) - 4)]

###########################################
# FUNCION PARA ADICION DE H Y C1 DE AMINA #
###########################################

print("  INICIA ADICIÓN DE AMINAS")

where_nitrogen = np.where(atoms_array == 88)

new_atoms = -1
new_bonds = -1
new_angles = -1
new_dihedrals = -1
amine_counter = 0
bond_counter = 0
for i in range(np.size(where_nitrogen[1][:])):
    if where_nitrogen[1][i] == 2:
        bond_counter += 1
        where_bond = np.where(bonds_array == where_nitrogen[0][i] + 1)
        for j in range(np.size(where_bond[0][:])):
            if where_bond[1][j] != 0 and bonds_array[where_bond[0][j]][3] == where_nitrogen[0][i] + 1 \
                    and bond_counter == 1:
                bond_counter += 1
                atoms_array[where_nitrogen[0][i]][2] = 16                                           # Atom type N amine
                a2 = int(bonds_array[where_bond[0][j]][2]) - 1
                atoms_array[a2][3] = 0.183                                                          # Carga C_go
                bonds_array[where_bond[0][j]][1] = 12                                               # Bond type N-C
                b_tmp = bonds_array[where_bond[0][j]][2]

                atoms_array[where_nitrogen[0][i]][4] = atoms_array[a2][4]
                atoms_array[where_nitrogen[0][i]][5] = atoms_array[a2][5]
                xyz_matrix[where_nitrogen[0][i]][1] = atoms_array[where_nitrogen[0][i]][4]
                xyz_matrix[where_nitrogen[0][i]][2] = atoms_array[where_nitrogen[0][i]][5]
                if atoms_array[where_nitrogen[0][i]][6] < 0:
                    atoms_array[where_nitrogen[0][i]][6] = atoms_array[a2][6] - 1.7
                    xyz_matrix[where_nitrogen[0][i]][3] = atoms_array[where_nitrogen[0][i]][6]
                elif atoms_array[where_nitrogen[0][i]][6] > 0:
                    atoms_array[where_nitrogen[0][i]][6] = atoms_array[a2][6] + 1.7
                    xyz_matrix[where_nitrogen[0][i]][3] = atoms_array[where_nitrogen[0][i]][6]

                    #   GENERACION DE ATOMOS H Y C1a Y ENLACES,
                    #  ANGULOS Y DIEDROSASOCIADOS DE TALES ATOMOS

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                h_amina = atoms_new[new_atoms][0]
                constant = atoms_new[new_atoms][0]
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 5                                                         # Type H amine
                atoms_new[new_atoms][3] = 0.383                                                     # H charge
                atoms_new[new_atoms][4] = atoms_array[a2][4] + 1.0
                atoms_new[new_atoms][5] = atoms_array[a2][5]
                atoms_new[new_atoms][6] = atoms_array[where_nitrogen[0][i]][6]
                xyz_matrix[constant][0] = "H"
                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                constant = atoms_new[new_atoms][0]
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 17                                                        # C amine
                atoms_new[new_atoms][3] = 0.023                                                     # C charge

                atoms_new[new_atoms][4] = atoms_array[a2][4]
                atoms_new[new_atoms][5] = atoms_array[a2][5]
                if atoms_array[where_nitrogen[0][i]][6] < 0:
                    atoms_new[new_atoms][6] = atoms_array[where_nitrogen[0][i]][6] - 1.4
                elif atoms_array[where_nitrogen[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_array[where_nitrogen[0][i]][6] + 1.4
                xyz_matrix[constant][0] = "C"
                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                bonds_new[new_bonds][1] = 11                                                        # H-N
                bonds_new[new_bonds][2] = atoms_array[where_nitrogen[0][i]][0]                      # N
                bonds_new[new_bonds][3] = atoms_new[new_atoms-1][0]                                 # H

                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds
                bonds_new[new_bonds][1] = 12  # C-N
                bonds_new[new_bonds][2] = atoms_array[where_nitrogen[0][i]][0]                      # N
                bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                                   # C

                new_angles += 1
                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 23                                                      # H-N-C
                angles_new[new_angles][2] = atoms_new[new_atoms-1][0]                               # H amina
                angles_new[new_angles][3] = atoms_array[where_nitrogen[0][i]][0]                    # N
                angles_new[new_angles][4] = atoms_new[new_atoms][0]                                 # C amina

                new_angles += 1
                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 25                                                      # C_go-N-C
                angles_new[new_angles][2] = b_tmp                                                   # C_go
                angles_new[new_angles][3] = atoms_array[where_nitrogen[0][i]][0]                    # N
                angles_new[new_angles][4] = atoms_new[new_atoms][0]                                 # C

                new_angles += 1
                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 23                                                      # H-N-C_go
                angles_new[new_angles][2] = b_tmp                                                   # C_go
                angles_new[new_angles][3] = atoms_array[where_nitrogen[0][i]][0]                    # N
                angles_new[new_angles][4] = atoms_new[new_atoms - 1][0]                             # H amina

                where_bond1 = []
                a = np.where(bonds_array == b_tmp)
                where_bond1.append(a)

                for j_1 in range(len(where_bond1)):
                    for k_1 in range(len(where_bond1[j_1][0])):
                        if bonds_array[where_bond1[j_1][0][k_1]][3] != where_nitrogen[0][i] + 1 and \
                                bonds_array[where_bond1[j_1][0][k_1]][2] == b_tmp:
                            d_tmp = bonds_array[where_bond1[j_1][0][k_1]][3]
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 30                                            # C-C-N-C
                            dihedrals_new[new_dihedrals][2] = d_tmp                                         # C
                            dihedrals_new[new_dihedrals][3] = b_tmp                                         # C_go
                            dihedrals_new[new_dihedrals][4] = atoms_array[where_nitrogen[0][i]][0]          # N
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                       # C

                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 29
                            dihedrals_new[new_dihedrals][2] = d_tmp                                         # C
                            dihedrals_new[new_dihedrals][3] = b_tmp                                         # C_go
                            dihedrals_new[new_dihedrals][4] = atoms_array[where_nitrogen[0][i]][0]          # N
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms - 1][0]                   # H

                        elif bonds_array[where_bond1[j_1][0][k_1]][2] != where_nitrogen[0][i] + 1 and \
                                bonds_array[where_bond1[j_1][0][k_1]][3] == b_tmp:
                            d_tmp = bonds_array[where_bond1[j_1][0][k_1]][2]
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 30                                            # C-C-N-C
                            dihedrals_new[new_dihedrals][2] = d_tmp                                         # C
                            dihedrals_new[new_dihedrals][3] = b_tmp                                         # C_go
                            dihedrals_new[new_dihedrals][4] = atoms_array[where_nitrogen[0][i]][0]          # N
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                       # C1a

                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 29
                            dihedrals_new[new_dihedrals][2] = d_tmp  # C
                            dihedrals_new[new_dihedrals][3] = b_tmp  # C_go
                            dihedrals_new[new_dihedrals][4] = atoms_array[where_nitrogen[0][i]][0]  # N
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms - 1][0]  # H

                # EXTENSION DE CADENA CARBONADA INICIANDO
                #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

                cont_carbono = 1
                cont_hidrogeno = 0
                cont_ext = 1
                while cont_ext <= 3:
                    cont_hidrogeno += 1
                    cont_carbono += 1

                    new_atoms += 1
                    atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                    constant = atoms_new[new_atoms][0]
                    xyz_matrix[constant][0] = "H"
                    atoms_new[new_atoms][1] = 1
                    atoms_new[new_atoms][2] = 18
                    atoms_new[new_atoms][3] = 0.063
                    atoms_new[new_atoms][4] = atoms_new[new_atoms-cont_ext][4]
                    atoms_new[new_atoms][5] = atoms_new[new_atoms-cont_ext][5]

                    if cont_hidrogeno == 1:
                        atoms_new[new_atoms][4] = atoms_new[new_atoms-cont_ext][4] + 1.0
                        atoms_new[new_atoms][5] = atoms_new[new_atoms-cont_ext][5] + 1.0
                        if atoms_new[new_atoms- cont_ext][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 0.5
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 0.5
                    elif cont_hidrogeno == 2:
                        atoms_new[new_atoms][4] = atoms_new[new_atoms - cont_ext][4] - 1.0
                        atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] + 1.0
                        if atoms_new[new_atoms - cont_ext][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 0.5
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 0.5
                    else:
                        atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] - 1.0
                        if atoms_new[new_atoms - cont_ext][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 0.5
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 0.5

                    if chain_length > 1 and cont_hidrogeno == 3:
                        atoms_new[new_atoms - 3][3] = 0.086
                        atoms_new[new_atoms][2] = 77
                        xyz_matrix[constant][0] = "C"
                        atoms_new[new_atoms][3] = -0.180
                        atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] - 1.0
                        if atoms_new[new_atoms - cont_ext][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 1.0
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 1.0

                    xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                    xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                    xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                    #  ADICION DE ENLACES, ANGULOS Y
                    #  DIEDROS DE LA CADENA CARBONADA

                    # 1) Adicion de enlaces y angulos

                    if cont_hidrogeno <= 3:
                        new_bonds += 1
                        bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                        bonds_new[new_bonds][1] = 13                                                    # H-C
                        bonds_new[new_bonds][2] = atoms_new[new_atoms - cont_ext][0]                    # C
                        bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                               # H
                        new_angles += 1

                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 23                                                  # H-C-N
                        angles_new[new_angles][2] = atoms_array[where_nitrogen[0][i]][0]                # N
                        angles_new[new_angles][3] = atoms_new[new_atoms - cont_ext][0]                  # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]                             # H

                        if cont_hidrogeno > 1:
                            new_angles += 1
                            angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                            angles_new[new_angles][1] = 24                                              # H-C-H
                            angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]                     # H
                            angles_new[new_angles][3] = atoms_new[new_atoms - cont_ext][0]              # C
                            angles_new[new_angles][4] = atoms_new[new_atoms][0]                         # H

                            if cont_hidrogeno == 3:
                                new_angles += 1
                                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                                angles_new[new_angles][1] = 24                                          # H-C-H
                                angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]                 # H
                                angles_new[new_angles][3] = atoms_new[new_atoms - cont_ext][0]          # C
                                angles_new[new_angles][4] = atoms_new[new_atoms][0]                     # H

                                if chain_length > 1:
                                    bonds_new[new_bonds][1] = 14                                        # C-C
                                    angles_new[new_angles - 2][1] = 27                                  # C-C-N
                                    angles_new[new_angles - 1][1] = 26                                  # C-C-H
                                    angles_new[new_angles][1] = 26                                      # C-C-H

                    # 2) Adicion de diedros

                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 32                                                # H-N-C-H
                    dihedrals_new[new_dihedrals][2] = h_amina                                           # H
                    dihedrals_new[new_dihedrals][3] = atoms_array[where_nitrogen[0][i]][0]              # N
                    dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - cont_ext][0]                # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                           # H

                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 31                                                # C-N-C-H
                    dihedrals_new[new_dihedrals][2] = b_tmp                                             # C_go
                    dihedrals_new[new_dihedrals][3] = atoms_array[where_nitrogen[0][i]][0]              # N
                    dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - cont_ext][0]                # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                           # H

                    if chain_length > 1:
                        dihedrals_new[new_dihedrals - 1][1] = 29                                        # C-C-N-H
                        dihedrals_new[new_dihedrals][1] = 30                                            # C-C-N-C

                    cont_ext += 1

                # MODIFICACION DE ANGULOS Y DIEDROS
                #   QUE INVOLUCRAN A N DE AMINA

                where_angle = []
                a = np.where(angles_array == where_nitrogen[0][i] + 1)
                where_angle.append(a)

                for j_2 in range(len(where_angle)):
                    for k_2 in range(len(where_angle[0][j_2])):
                        wan = where_angle[0][j_2][k_2]
                        if angles_array[wan][2] == where_nitrogen[0][i] + 1 and \
                                angles_array[wan][1] == 2 or \
                                angles_array[wan][4] == where_nitrogen[0][i] + 1 and \
                                angles_array[wan][1] == 2:
                            angles_array[wan][1] = 18

                where_dihedral = []
                a = np.where(dihedrals_array == where_nitrogen[0][i] + 1)
                where_dihedral.append(a)

                for j_3 in range(len(where_dihedral)):
                    for k_3 in range(len(where_dihedral[j_3][0])):
                        wd = where_dihedral[j_3][0][k_3]
                        if dihedrals_array[wd][2] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[wd][3] == b_tmp or \
                                dihedrals_array[wd][5] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[wd][4] == b_tmp:
                            dihedrals_array[wd][1] = 37

                        elif dihedrals_array[wd][3] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[wd][4] == b_tmp:
                            dihedrals_array[wd][1] = 29
                            dihedrals_array[wd][2] = dihedrals_array[wd][5]
                            dihedrals_array[wd][3] = b_tmp
                            dihedrals_array[wd][4] = where_nitrogen[0][i] + 1
                            dihedrals_array[wd][5] = h_amina

                        elif dihedrals_array[wd][4] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[wd][3] == b_tmp:
                            dihedrals_array[wd][1] = 29
                            dihedrals_array[wd][2] = dihedrals_array[wd][2]
                            dihedrals_array[wd][3] = b_tmp
                            dihedrals_array[wd][4] = where_nitrogen[0][i] + 1
                            dihedrals_array[wd][5] = h_amina

            elif where_bond[1][j] != 0 and bonds_array[where_bond[0][j]][3] == where_nitrogen[0][i] + 1 \
                    and bond_counter == 2:
                bonds_array[where_bond[0][j]][1] = 88
                bond_counter = 0

print("* Adición de -H y -CH3 sobre átomo N de amina --> COMPLETADA")

##############################################
# ADICION DE -OH SOBRE C2 DE GRUPOS EPOXIDOS #
##############################################

where_bond = np.where(bonds_array == 88)

for i in range(np.size(where_nitrogen[1][:])):
    if where_nitrogen[1][i] == 2:
        for j in range(len(where_bond[0])):
            if bonds_array[where_bond[0][j]][1] == 88 and bonds_array[where_bond[0][j]][3] == where_nitrogen[0][i] + 1:
                bonds_array[where_bond[0][j]][1] = 6                              # C-O(H)
                a2 = bonds_array[where_bond[0][j]][2]                             # Cgo index
                atoms_array[int(a2)-1][3] = 0.265

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                bonds_array[where_bond[0][j]][3] = atoms_new[new_atoms][0]
                constant = atoms_new[new_atoms][0]
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 4
                atoms_new[new_atoms][3] = -0.683
                xyz_matrix[constant][0] = "O"
                atoms_new[new_atoms][4] = atoms_array[int(a2) - 1][4]
                atoms_new[new_atoms][5] = atoms_array[int(a2) - 1][5]
                if atoms_array[where_nitrogen[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_array[int(a2) - 1][6] - 1.4
                else:
                    atoms_new[new_atoms][6] = atoms_array[int(a2) - 1][6] + 1.4

                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                constant = atoms_new[new_atoms][0]
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 5
                atoms_new[new_atoms][3] = 0.418
                xyz_matrix[constant][0] = "H"
                atoms_new[new_atoms][4] = atoms_array[int(a2) - 1][4]
                atoms_new[new_atoms][5] = atoms_array[int(a2) - 1][5]
                if atoms_array[where_nitrogen[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[new_atoms - 1][6] - 1.0
                else:
                    atoms_new[new_atoms][6] = atoms_new[new_atoms - 1][6] + 1.0

                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                bonds_new[new_bonds][1] = 8
                bonds_new[new_bonds][2] = atoms_new[new_atoms - 1][0]
                bonds_new[new_bonds][3] = atoms_new[new_atoms][0]

                where_angle = []
                a = np.where(angles_array == where_nitrogen[0][i] + 1)
                where_angle.append(a)

                for j_2 in range(len(where_angle)):
                    for k_2 in range(len(where_angle[0][j_2])):
                        if angles_array[where_angle[0][j_2][k_2]][2] == where_nitrogen[0][i] + 1 and \
                                angles_array[where_angle[0][j_2][k_2]][3] == bonds_array[where_bond[0][j]][2] or \
                                angles_array[where_angle[0][j_2][k_2]][4] == where_nitrogen[0][i] + 1 and \
                                angles_array[where_angle[0][j_2][k_2]][3] == bonds_array[where_bond[0][j]][2]:
                            if angles_array[where_angle[0][j_2][k_2]][1] == 18:
                                angles_array[where_angle[0][j_2][k_2]][1] = 2  # N-Cgo-C
                            elif angles_array[where_angle[0][j_2][k_2]][1] == 27:
                                angles_array[where_angle[0][j_2][k_2]][1] = 2  # N-Cgo-C

                        elif angles_array[where_angle[0][j_2][k_2]][3] == where_nitrogen[0][i] + 1:
                            angles_array[where_angle[0][j_2][k_2]][1] = 8  # Cgo-O-H
                            angles_array[where_angle[0][j_2][k_2]][2] = bonds_array[where_bond[0][j]][2]  # Cgo
                            angles_array[where_angle[0][j_2][k_2]][3] = atoms_new[new_atoms - 1][0]  # O
                            angles_array[where_angle[0][j_2][k_2]][4] = atoms_new[new_atoms][0]  # H

                where_dihedral = []
                a = np.where(dihedrals_array == where_nitrogen[0][i] + 1)
                where_dihedral.append(a)

                for j_3 in range(len(where_dihedral)):
                    for k_3 in range(len(where_dihedral[j_3][0])):
                        if dihedrals_array[where_dihedral[j_3][0][k_3]][2] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[where_dihedral[j_3][0][k_3]][3] == bonds_array[where_bond[0][j]][2] or \
                                dihedrals_array[where_dihedral[j_3][0][k_3]][5] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[where_dihedral[j_3][0][k_3]][4] == bonds_array[where_bond[0][j]][2]:

                            if dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 11:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 18
                            elif dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 7:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 10
                            elif dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 16:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 17
                            elif dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 7:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 10
                            elif dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 17:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 19

                        elif dihedrals_array[where_dihedral[j_3][0][k_3]][3] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[where_dihedral[j_3][0][k_3]][4] == bonds_array[where_bond[0][j]][2] or \
                                dihedrals_array[where_dihedral[j_3][0][k_3]][4] == where_nitrogen[0][i] + 1 and \
                                dihedrals_array[where_dihedral[j_3][0][k_3]][3] == bonds_array[where_bond[0][j]][2]:

                            if dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 23:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 24
                            elif dihedrals_array[where_dihedral[j_3][0][k_3]][1] == 13:
                                dihedrals_array[where_dihedral[j_3][0][k_3]][1] = 14

print("* Adición de -OH del 2-aminoalcohol --> COMPLETADA")

###########################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE ETILO #
###########################################

atoms_new = np.array(atoms_new)

if chain_length > 1:
    where_c = np.where(atoms_new == 77)
    for i in range(np.size(where_c[0][:])):
        atoms_new[where_c[0][i]][2] = 17

        # EXTENSION DE CADENA CARBONADA INICIANDO
        #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

        cont_carbono = 1
        cont_hidrogeno = 0
        for cont in range(3):
            cont_hidrogeno += 1
            cont_carbono += 1

            new_atoms += 1
            atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
            constant = int(atoms_new[new_atoms][0])
            xyz_matrix[constant][0] = "H"
            atoms_new[new_atoms][1] = 1
            atoms_new[new_atoms][2] = 18
            atoms_new[new_atoms][3] = 0.060
            atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4]
            atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5]

            if cont_hidrogeno == 1:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] - 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] - 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            elif cont_hidrogeno == 2:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] + 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] - 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            else:
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5

            if chain_length > 2 and cont_hidrogeno == 3:
                atoms_new[where_c[0][i]][3] = -0.120
                atoms_new[new_atoms][2] = 66
                xyz_matrix[constant][0] = "C"
                atoms_new[new_atoms][3] = -0.180
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 1.3
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 1.3

            xyz_matrix[constant][1] = atoms_new[new_atoms][4]
            xyz_matrix[constant][2] = atoms_new[new_atoms][5]
            xyz_matrix[constant][3] = atoms_new[new_atoms][6]

            #  ADICION DE ENLACES, ANGULOS Y
            #  DIEDROS DE LA CADENA CARBONADA

            # 1) Adicion de enlaces y angulos

            if cont_hidrogeno <= 3:
                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                bonds_new[new_bonds][1] = 13                                                            # C-H
                bonds_new[new_bonds][2] = atoms_new[where_c[0][i]][0]                                   # C
                bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                                       # H
                new_angles += 1

                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 26                                                          # H-C-C
                where_bond = np.where(bonds_new == atoms_new[where_c[0][i]][0])
                for k in range(len(where_bond[0][:])):
                    if bonds_new[where_bond[0][k]][3] == atoms_new[where_c[0][i]][0]:
                        angles_new[new_angles][2] = bonds_new[where_bond[0][k]][2]                                     # C
                        c_1 = bonds_new[where_bond[0][k]][2]
                angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                                 # C
                angles_new[new_angles][4] = atoms_new[new_atoms][0]                                     # H

                if cont_hidrogeno > 1:
                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 24  # H-C-H
                    angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]  # H
                    angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]  # C
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                    if cont_hidrogeno == 3:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 24  # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]  # H
                        angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]  # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                        if chain_length > 2:
                            bonds_new[new_bonds][1] = 14  # C-C
                            angles_new[new_angles - 2][1] = 11  # C-C-C
                            angles_new[new_angles - 1][1] = 26  # C-C-H
                            angles_new[new_angles][1] = 26  # C-C-H

                # 2) Adicion de diedros

            bonds_new = np.array(bonds_new)
            where_c1 = np.where(bonds_new == c_1)

            for j in range(len(where_c1)):
                for k_1 in range(np.size(where_c1[j])):
                    if bonds_new[where_c1[j][k_1]][1] == 12 and bonds_new[where_c1[j][k_1]][2] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 35  # N-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][3]  # N
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

                    elif bonds_new[where_c1[j][k_1]][1] == 12 and bonds_new[where_c1[j][k_1]][3] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 35  # N-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][2]  # N
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

                    elif bonds_new[where_c1[j][k_1]][1] == 13 and bonds_new[where_c1[j][k_1]][2] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 34  # H-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][3]  # H
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

                    elif bonds_new[where_c1[j][k_1]][1] == 13 and bonds_new[where_c1[j][k_1]][3] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 34  # H-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][2]  # H
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

            if int(chain_length) > 2:
                if dihedrals_new[new_dihedrals - 1][1] == 35:
                    dihedrals_new[new_dihedrals - 1][1] = 37  # N-C-C-C

                elif dihedrals_new[new_dihedrals - 1][1] == 34:
                    dihedrals_new[new_dihedrals - 1][1] = 36  # H-C-C-C

                elif dihedrals_new[new_dihedrals][1] == 35:
                    dihedrals_new[new_dihedrals][1] = 37  # N-C-C-C

                elif dihedrals_new[new_dihedrals][1] == 34:
                    dihedrals_new[new_dihedrals][1] = 36  # H-C-C-C

if chain_length > 1:
    print("* Extensión de cadena de amina a 2 carbonos --> COMPLETADA")

#############################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE PROPILO #
#############################################

if chain_length > 2:
    where_c = np.where(atoms_new == 66)
    for i in range(np.size(where_c[0][:])):
        atoms_new[where_c[0][i]][2] = 17

        # EXTENSION DE CADENA CARBONADA INICIANDO
        #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

        cont_carbono = 1
        cont_hidrogeno = 0
        for cont in range(3):
            cont_hidrogeno += 1
            cont_carbono += 1

            new_atoms += 1
            atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
            constant = int(atoms_new[new_atoms][0])
            xyz_matrix[constant][0] = "H"
            atoms_new[new_atoms][1] = 1
            atoms_new[new_atoms][2] = 18
            atoms_new[new_atoms][3] = 0.060
            atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4]
            atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5]

            if cont_hidrogeno == 1:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] + 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[i][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            elif cont_hidrogeno == 2:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] - 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[i][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            else:
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] - 1.0
                if chain_length == 3:
                    if atoms_new[where_c[0][i]][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
                else:
                    atoms_new[new_atoms][2] = 17
                    xyz_matrix[constant][0] = "C"
                    atoms_new[new_atoms][3] = -0.180

                    atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4]
                    if atoms_new[where_c[0][i]][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 1.3
                    else:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 1.3

                    if cont_carbono < chain_length:
                        atoms_new[new_atoms][3] = -0.120
                        atoms_new[where_c[0][i]][3] = -0.120
                    elif cont_carbono == chain_length:
                        atoms_new[new_atoms][3] = -0.180
                        atoms_new[where_c[0][i]][3] = -0.120

            xyz_matrix[constant][1] = atoms_new[new_atoms][4]
            xyz_matrix[constant][2] = atoms_new[new_atoms][5]
            xyz_matrix[constant][3] = atoms_new[new_atoms][6]

            #  ADICION DE ENLACES, ANGULOS Y
            #  DIEDROS DE LA CADENA CARBONADA

            # 1) Adicion de enlaces y angulos

            if cont_hidrogeno <= 3:
                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                bonds_new[new_bonds][1] = 13  # C-H
                bonds_new[new_bonds][2] = atoms_new[where_c[0][i]][0]  # C
                bonds_new[new_bonds][3] = atoms_new[new_atoms][0]  # H

                new_angles += 1
                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 26  # H-C-C

                k = 0
                while k <= len(bonds_new) - 1:
                    if bonds_new[k][3] == atoms_new[where_c[0][i]][0]:
                        angles_new[new_angles][2] = bonds_new[k][2]  # C
                        c_1 = bonds_new[k][2]
                    k += 1
                angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]  # C
                angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                if cont_hidrogeno > 1:
                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 24  # H-C-H
                    angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]  # H
                    angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]  # C
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                    if cont_hidrogeno == 3:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 24  # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]  # H
                        angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]  # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                        if chain_length > 3:
                            bonds_new[new_bonds][1] = 14  # C-C
                            angles_new[new_angles - 2][1] = 11  # C-C-C
                            angles_new[new_angles - 1][1] = 26  # C-C-H
                            angles_new[new_angles][1] = 26  # C-C-H

            # 2) Adicion de diedros

            bonds_new = np.array(bonds_new)
            where_c1 = np.where(bonds_new == c_1)
            
            for j in range(len(where_c1)):
                for k_1 in range(np.size(where_c1[j])):
                    if bonds_new[where_c1[j][k_1]][1] == 12 and bonds_new[where_c1[j][k_1]][2] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 36  # C-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][3]  # C
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H
            
                    elif bonds_new[where_c1[j][k_1]][1] == 12 and bonds_new[where_c1[j][k_1]][3] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 36  # C-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][2]  # C
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H
            
                    elif bonds_new[where_c1[j][k_1]][1] == 13 and bonds_new[where_c1[j][k_1]][2] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 34  # C-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][3]  # C
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]
            
                    elif bonds_new[where_c1[j][k_1]][1] == 13 and bonds_new[where_c1[j][k_1]][3] == c_1:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 34  # C-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][2]  # C
                        dihedrals_new[new_dihedrals][3] = c_1  # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]  # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]
            
            if chain_length > 3 and cont_carbono <= chain_length:
                if dihedrals_new[new_dihedrals - 1][1] == 36:
                    dihedrals_new[new_dihedrals - 1][1] = 38  # C-C-C-C
            
                elif dihedrals_new[new_dihedrals - 1][1] == 34:
                    dihedrals_new[new_dihedrals - 1][1] = 36  # H-C-C-C
            
                elif dihedrals_new[new_dihedrals][1] == 36:
                    dihedrals_new[new_dihedrals][1] = 38  # C-C-C-C
            
                elif dihedrals_new[new_dihedrals][1] == 34:
                    dihedrals_new[new_dihedrals][1] = 36  # H-C-C-C

        if chain_length > 3:
            cont_carbono = 3
            cont_hidrogeno = 0
            k = 1
            while k <= 3:
                cont_hidrogeno += 1

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                constant = int(atoms_new[new_atoms][0])
                xyz_matrix[constant][0] = "H"
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 18
                atoms_new[new_atoms][3] = 0.060
                atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4]
                atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5]

                if cont_hidrogeno == 1:
                    z = k
                    atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4] + 1.0
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5] + 1.0
                    if atoms_new[new_atoms - k][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.5
                elif cont_hidrogeno == 2:
                    z = k
                    atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4] - 1.0
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5] + 1.0
                    if atoms_new[new_atoms - k][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.5
                else:
                    cont_carbono += 1
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5] - 1.0
                    if cont_carbono < chain_length - 1:
                        atoms_new[new_atoms][2] = 17
                        xyz_matrix[constant][0] = "C"
                        atoms_new[new_atoms][3] = -0.120
                        if atoms_new[new_atoms - k][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 1.3
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 1.3
                        z = k
                        k = 0
                        cont_hidrogeno = 0

                    elif cont_carbono == chain_length - 1:
                        atoms_new[new_atoms - k][3] = -0.120
                        atoms_new[new_atoms][2] = 17
                        xyz_matrix[constant][0] = "C"
                        atoms_new[new_atoms][3] = -0.180
                        atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4]
                        if atoms_new[new_atoms - k][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.8
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.8
                        z = k
                        k = 0
                        cont_hidrogeno = 0

                    elif cont_carbono == chain_length:
                        z = k
                        atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4]
                        if atoms_new[new_atoms - k][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.8
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.8

                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                #  ADICION DE ENLACES, ANGULOS Y
                #  DIEDROS DE LA CADENA CARBONADA

                # 1) Adicion de enlaces y angulos

                if cont_hidrogeno <= 3:
                    new_bonds += 1
                    bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                    bonds_new[new_bonds][1] = 13  # C-H
                    bonds_new[new_bonds][2] = atoms_new[new_atoms - z][0]  # C
                    bonds_new[new_bonds][3] = atoms_new[new_atoms][0]  # H
                    if atoms_new[new_atoms - z][3] == -0.120 and atoms_new[new_atoms][3] == -0.180:
                        bonds_new[new_bonds][1] = 14

                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 26  # H-C-C

                    where_a = np.where(bonds_new == atoms_new[new_atoms - z][0])

                    for j_2 in range(len(where_a)):
                        for k_2 in range(len(where_a[j_2][:])):
                            if bonds_new[where_a[j_2][k_2]][3] == atoms_new[new_atoms - z][0] and \
                                    bonds_new[where_a[j_2][k_2]][2] != atoms_new[new_atoms][0]:
                                angles_new[new_angles][2] = bonds_new[where_a[j_2][k_2]][2]  # C
                                c_1 = bonds_new[where_a[j_2][k_2]][2]

                    angles_new[new_angles][3] = atoms_new[new_atoms - z][0]  # C
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                    if cont_hidrogeno > 1:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 24  # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]  # H
                        angles_new[new_angles][3] = atoms_new[new_atoms - z][0]  # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                        if cont_hidrogeno == 3:
                            new_angles += 1
                            angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                            angles_new[new_angles][1] = 24  # H-C-H
                            angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]  # H
                            angles_new[new_angles][3] = atoms_new[new_atoms - z][0]  # C
                            angles_new[new_angles][4] = atoms_new[new_atoms][0]  # H

                            if chain_length > cont_carbono:
                                bonds_new[new_bonds][1] = 14  # C-C
                                angles_new[new_angles - 2][1] = 11  # C-C-C
                                angles_new[new_angles - 1][1] = 26  # C-C-H
                                angles_new[new_angles][1] = 26  # C-C-H

                if chain_length >= cont_carbono and cont_hidrogeno == 3:
                    if dihedrals_new[new_dihedrals - 1][1] == 36:
                        dihedrals_new[new_dihedrals - 1][1] = 38

                    elif dihedrals_new[new_dihedrals - 1][1] == 34:
                        dihedrals_new[new_dihedrals - 1][1] = 36

                    elif dihedrals_new[new_dihedrals][1] == 36:
                        dihedrals_new[new_dihedrals][1] = 38

                    elif dihedrals_new[new_dihedrals][1] == 34:
                        dihedrals_new[new_dihedrals][1] = 36

                # 2) Adicion de diedros

                bonds_new = np.array(bonds_new)
                where_c1 = np.where(bonds_new == c_1)

                for j in range(len(where_c1)):
                    for k_1 in range(np.size(where_c1[j])):
                        if bonds_new[where_c1[j][k_1]][1] == 14 and bonds_new[where_c1[j][k_1]][2] == c_1 and \
                                bonds_new[where_c1[j][k_1]][3] != atoms_new[new_atoms - z][0]:
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 36  # C-C-C-H
                            dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][3]  # C
                            dihedrals_new[new_dihedrals][3] = c_1  # C
                            dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]  # C
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

                        elif bonds_new[where_c1[j][k_1]][1] == 14 and bonds_new[where_c1[j][k_1]][3] == c_1 and \
                                bonds_new[where_c1[j][k_1]][2] != atoms_new[new_atoms - z][0]:
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 36  # C-C-C-H
                            dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][2]  # C
                            dihedrals_new[new_dihedrals][3] = c_1  # C
                            dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]  # C
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

                        elif bonds_new[where_c1[j][k_1]][1] == 13 and bonds_new[where_c1[j][k_1]][2] == c_1 and \
                                bonds_new[where_c1[j][k_1]][3] != atoms_new[new_atoms - z][0]:
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 34  # H-C-C-H
                            dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][3]  # H
                            dihedrals_new[new_dihedrals][3] = c_1  # C
                            dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]  # C
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H

                        elif bonds_new[where_c1[j][k_1]][1] == 13 and bonds_new[where_c1[j][k_1]][3] == c_1 and \
                                bonds_new[where_c1[j][k_1]][2] != atoms_new[new_atoms - z][0]:
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 34  # H-C-C-H
                            dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[j][k_1]][2]  # H
                            dihedrals_new[new_dihedrals][3] = c_1  # C
                            dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]  # C
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]  # H
                k += 1

if chain_length > 2:
    print("* Extensión de cadena de amina a 3 o más carbonos --> COMPLETADA", "\n")

########################################################################################################################
#                                  ADICION DE AMIDAS SOBRE LOS ÁCIDOS CARBOXÍLICOS                                     #
########################################################################################################################
if carboxy_fraction > 0:
    print("  INICIA ADICIÓN DE AMIDAS")

where_nitrogen = np.where(atoms_array == 89)

cont_amida = 1

for i in range(np.size(where_nitrogen[1][:])):
    if where_nitrogen[1][i] == 2:
        if cont_amida <= int(carboxy_fraction):
            cont_amida += 1
            atoms_array[where_nitrogen[0][i]][2] = 14
            atoms_array[where_nitrogen[0][i]][3] = -0.500

            new_atoms += 1
            atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
            constant = atoms_new[new_atoms][0]
            xyz_matrix[int(constant)][0] = "C"
            atoms_new[new_atoms][1] = 1
            atoms_new[new_atoms][2] = 17
            atoms_new[new_atoms][3] = 0.02

            atoms_new[new_atoms][4] = atoms_array[where_nitrogen[0][i]][4]
            atoms_new[new_atoms][5] = atoms_array[where_nitrogen[0][i]][5]
            if atoms_array[where_nitrogen[0][i]][6] > 0:
                atoms_new[new_atoms][6] = atoms_array[where_nitrogen[0][i]][6] + 1.3
            else:
                atoms_new[new_atoms][6] = atoms_array[where_nitrogen[0][i]][6] - 1.3

            xyz_matrix[int(constant)][1] = atoms_new[new_atoms][4]
            xyz_matrix[int(constant)][2] = atoms_new[new_atoms][5]
            xyz_matrix[int(constant)][3] = atoms_new[new_atoms][6]

            new_bonds += 1
            bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
            bonds_new[new_bonds][1] = 10                                                                # C-N
            bonds_new[new_bonds][2] = atoms_array[where_nitrogen[0][i]][0]                              # N
            bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                                           # C

            new_angles += 1
            angles_new[new_angles][0] = len(angles_array) + new_angles + 1
            angles_new[new_angles][1] = 20                                                              # C-N-H
            where_bond = np.where(bonds_array == where_nitrogen[0][i] + 1)
            for j in range(np.size(where_bond[0][:])):
                if bonds_array[where_bond[0][j]][2] == where_nitrogen[0][i] + 1 and \
                        bonds_array[where_bond[0][j]][1] == 8:
                    angles_new[new_angles][2] = bonds_array[where_bond[0][j]][3]
                    bonds_array[where_bond[0][j]][1] = 11

                elif bonds_array[where_bond[0][j]][3] == where_nitrogen[0][i] + 1 and \
                        bonds_array[where_bond[0][j]][1] == 8:
                    angles_new[new_angles][2] = bonds_array[where_bond[0][j]][2]
                    bonds_array[where_bond[0][j]][1] = 11

            angles_new[new_angles][3] = atoms_array[where_nitrogen[0][i]][0]                                # N
            angles_new[new_angles][4] = atoms_new[new_atoms][0]                                             # C1
            h_amida = angles_new[new_angles][2]                                                             # H
            atoms_array[int(h_amida) - 1][3] = 0.300

            new_angles += 1
            angles_new[new_angles][0] = len(angles_array) + new_angles + 1
            angles_new[new_angles][1] = 25                                                                  # C-N-C
            where_bond = np.where(bonds_array == where_nitrogen[0][i] + 1)
            for j in range(np.size(where_bond[0][:])):
                if bonds_array[where_bond[0][j]][2] == where_nitrogen[0][i] + 1 and \
                        bonds_array[where_bond[0][j]][3] != h_amida:
                    angles_new[new_angles][2] = bonds_array[where_bond[0][j]][3]

                elif bonds_array[where_bond[0][j]][3] == where_nitrogen[0][i] + 1 and \
                        bonds_array[where_bond[0][j]][2] != h_amida:
                    angles_new[new_angles][2] = bonds_array[where_bond[0][j]][2]

            angles_new[new_angles][3] = atoms_array[where_nitrogen[0][i]][0]                                # N
            angles_new[new_angles][4] = atoms_new[new_atoms][0]                                             # C1
            c_amida = angles_new[new_angles][2]                                                             # C
            atoms_array[int(c_amida) - 1][3] = 0.615

            new_dihedrals += 1
            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
            dihedrals_new[new_dihedrals][1] = 33                                                            # O-C-N-C1
            where_c1 = np.where(bonds_array == c_amida)
            for j in range(len(where_c1[0][:])):
                if bonds_array[where_c1[0][j]][2] == c_amida and bonds_array[where_c1[0][j]][1] == 9:
                    dihedrals_new[new_dihedrals][2] = bonds_array[where_c1[0][j]][3]                        # O
                elif bonds_array[where_c1[0][j]][3] == c_amida and bonds_array[where_c1[0][j]][1] == 9:
                    dihedrals_new[new_dihedrals][2] = bonds_array[where_c1[0][j]][2]                        # O

            dihedrals_new[new_dihedrals][3] = c_amida                                                       # C(O)
            dihedrals_new[new_dihedrals][4] = atoms_array[where_nitrogen[0][i]][0]                          # N
            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                                       # C1
            o_amida = dihedrals_new[new_dihedrals][2]
            atoms_array[int(o_amida) - 1][3] = -0.500

            new_dihedrals += 1
            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
            dihedrals_new[new_dihedrals][1] = 30                                                          # C_go-C-N-C1
            for j in range(len(where_c1[0][:])):
                if bonds_array[where_c1[0][j]][2] == c_amida and bonds_array[where_c1[0][j]][1] == 5:
                    dihedrals_new[new_dihedrals][2] = bonds_array[where_c1[0][j]][3]                      # C_go
                elif bonds_array[where_c1[0][j]][3] == c_amida and bonds_array[where_c1[0][j]][1] == 5:
                    dihedrals_new[new_dihedrals][2] = bonds_array[where_c1[0][j]][2]

            cgo_amida = dihedrals_new[new_dihedrals][2]
            dihedrals_new[new_dihedrals][3] = c_amida                                                     # C(O)
            dihedrals_new[new_dihedrals][4] = atoms_array[where_nitrogen[0][i]][0]                        # N
            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                                     # C1

            # EXTENSION DE CADENA CARBONADA INICIANDO
            #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

            cont_carbono = 1
            cont_hidrogeno = 0
            cont_ext = 1
            while cont_ext <= 3:
                cont_hidrogeno += 1
                cont_carbono += 1

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                constant = int(atoms_new[new_atoms][0])
                xyz_matrix[constant][0] = "H"
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 18
                atoms_new[new_atoms][3] = 0.060
                atoms_new[new_atoms][4] = atoms_new[new_atoms - cont_ext][4]
                atoms_new[new_atoms][5] = atoms_new[new_atoms][5]

                if cont_hidrogeno == 1:
                    atoms_new[new_atoms][4] = atoms_new[new_atoms - cont_ext][4] - 1.0
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] - 1.0
                    if atoms_new[new_atoms - cont_ext][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 0.5
                elif cont_hidrogeno == 2:
                    atoms_new[new_atoms][4] = atoms_new[new_atoms - cont_ext][4] + 1.0
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] - 1.0
                    if atoms_new[new_atoms - cont_ext][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 0.5
                else:
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] + 1.0
                    if atoms_new[new_atoms - cont_ext][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 0.5

                if chain_length > 1 and cont_hidrogeno == 3:
                    atoms_new[new_atoms - cont_ext][3] = 0.08
                    atoms_new[new_atoms][2] = -97
                    xyz_matrix[constant][0] = "C"
                    atoms_new[new_atoms][3] = -0.180
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - cont_ext][5] + 1.0
                    if atoms_new[new_atoms - cont_ext][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] + 1.3
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - cont_ext][6] - 1.3

                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                #  ADICION DE ENLACES, ANGULOS Y
                #  DIEDROS DE LA CADENA CARBONADA

                # 1) Adicion de enlaces y angulos

                if cont_hidrogeno <= 3:
                    new_bonds += 1
                    bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                    bonds_new[new_bonds][1] = 13
                    bonds_new[new_bonds][2] = atoms_new[new_atoms - cont_ext][0]                            # C
                    bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                                       # H

                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 23                                                          # H-C-N
                    angles_new[new_angles][2] = atoms_array[where_nitrogen[0][i]][0]                        # N
                    angles_new[new_angles][3] = atoms_new[new_atoms - cont_ext][0]                          # C1
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]                                     # H1

                    if cont_hidrogeno > 1:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 23                                                      # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]                             # H
                        angles_new[new_angles][3] = atoms_new[new_atoms - cont_ext][0]                      # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]                                 # H2

                        if cont_hidrogeno == 3:
                            cont_hidrogeno = 0
                            new_angles += 1
                            angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                            angles_new[new_angles][1] = 24                                                  # H-C-H
                            angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]                         # H
                            angles_new[new_angles][3] = atoms_new[new_atoms - cont_ext][0]                  # C
                            angles_new[new_angles][4] = atoms_new[new_atoms][0]                             # H3

                            if chain_length > 1:
                                bonds_new[new_bonds][1] = 14                                                # C-C
                                angles_new[new_angles - 2][1] = 18                                          # C-C-N
                                angles_new[new_angles - 1][1] = 26                                          # C-C-H
                                angles_new[new_angles][1] = 26                                              # C-C-H

                # 2) Adicion de diedros
                new_dihedrals += 1
                dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                dihedrals_new[new_dihedrals][1] = 32                                                        # H-N-C-H
                dihedrals_new[new_dihedrals][2] = h_amida                                                   # H
                dihedrals_new[new_dihedrals][3] = atoms_array[where_nitrogen[0][i]][0]                      # N
                dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - cont_ext][0]                        # C1
                dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                                   # H

                new_dihedrals += 1
                dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                dihedrals_new[new_dihedrals][1] = 31                                                        # C-N-C-H
                dihedrals_new[new_dihedrals][2] = c_amida                                                   # C(O)
                dihedrals_new[new_dihedrals][3] = atoms_array[where_nitrogen[0][i]][0]                      # N
                dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - cont_ext][0]                        # C1
                dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                                   # H

                if chain_length > 1:
                    dihedrals_new[new_dihedrals - 1][1] = 29                                                # C-C-N-H
                    dihedrals_new[new_dihedrals][1] = 30                                                    # C-C-N-C

                cont_ext += 1

            # MODIFICACION DE ANGULOS Y DIEDROS
            #   QUE INVOLUCRAN A N DE AMINA

            where_angle = np.where(angles_array == where_nitrogen[0][i] + 1)

            for j in range(len(where_angle[0][:])):
                if angles_array[where_angle[0][j]][1] == 3 and \
                        angles_array[where_angle[0][j]][3] == where_nitrogen[0][i] + 1:
                    angles_array[where_angle[0][j]][1] = 20
                elif angles_array[where_angle[0][j]][1] == 15 and \
                        angles_array[where_angle[0][j]][2] == where_nitrogen[0][i] + 1 or \
                        angles_array[where_angle[0][j]][1] == 15 and \
                        angles_array[where_angle[0][j]][4] == where_nitrogen[0][i] + 1:
                    angles_array[where_angle[0][j]][1] = 19
                elif angles_array[where_angle[0][j]][1] == 7 and \
                        angles_array[where_angle[0][j]][2] == where_nitrogen[0][i] + 1 or \
                        angles_array[where_angle[0][j]][1] == 7 and \
                        angles_array[where_angle[0][j]][4] == where_nitrogen[0][i] + 1:
                    angles_array[where_angle[0][j]][1] = 18

            where_dihedral = np.where(dihedrals_array == where_nitrogen[0][i] + 1)

            for j in range(len(where_dihedral[0][:])):
                if dihedrals_array[where_dihedral[0][j]][1] == 22 and \
                        dihedrals_array[where_dihedral[0][j]][3] == where_nitrogen[0][i] + 1 or \
                        dihedrals_array[where_dihedral[0][j]][1] == 22 and \
                        dihedrals_array[where_dihedral[0][j]][4] == where_nitrogen[0][i] + 1:
                    dihedrals_array[where_dihedral[0][j]][1] = 27
                elif dihedrals_array[where_dihedral[0][j]][1] == 21 and \
                        dihedrals_array[where_dihedral[0][j]][3] == where_nitrogen[0][i] + 1 or \
                        dihedrals_array[where_dihedral[0][j]][1] == 21 and \
                        dihedrals_array[where_dihedral[0][j]][4] == where_nitrogen[0][i] + 1:
                    dihedrals_array[where_dihedral[0][j]][1] = 28

if carboxy_fraction > 0:
    print("* Adición de -H y -CH3 sobre átomo N de amida --> COMPLETADA")

###########################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE ETILO #
###########################################

if chain_length > 1:
    where_c = np.where(atoms_new == -97)
    for i in range(np.size(where_c[0][:])):
        atoms_new[where_c[0][i]][2] = 17

        # EXTENSION DE CADENA CARBONADA INICIANDO
        #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

        cont_carbono = 1
        cont_hidrogeno = 0
        for cont_ext in range(3):
            cont_hidrogeno += 1
            cont_carbono += 1
            new_atoms += 1
            atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
            constant = int(atoms_new[new_atoms][0])
            xyz_matrix[constant][0] = "H"
            atoms_new[new_atoms][1] = 1
            atoms_new[new_atoms][2] = 18
            atoms_new[new_atoms][3] = 0.060
            atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4]
            atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5]

            if cont_hidrogeno == 1:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] + 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            elif cont_hidrogeno == 2:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] - 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            else:
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] - 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5

            if chain_length > 2 and cont_hidrogeno == 3:
                atoms_new[where_c[0][i]][3] = -0.120
                atoms_new[new_atoms][2] = -66
                xyz_matrix[constant][0] = "C"
                atoms_new[new_atoms][3] = -0.180
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 1.3
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 1.3

            xyz_matrix[constant][1] = atoms_new[new_atoms][4]
            xyz_matrix[constant][2] = atoms_new[new_atoms][5]
            xyz_matrix[constant][3] = atoms_new[new_atoms][6]

            #  ADICION DE ENLACES, ANGULOS Y
            #  DIEDROS DE LA CADENA CARBONADA

            # 1) Adicion de enlaces y angulos

            if cont_hidrogeno <= 3:
                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                bonds_new[new_bonds][1] = 13  # C-H
                bonds_new[new_bonds][2] = atoms_new[where_c[0][i]][0]  # C
                bonds_new[new_bonds][3] = atoms_new[new_atoms][0]  # H

                new_angles += 1
                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 26  # H-C-C

                bonds_new = np.array(bonds_new)
                where_bond = np.where(bonds_new == atoms_new[where_c[0][i]][0])

                for j in range(len(where_bond[0][:])):
                    if bonds_new[where_bond[0][j]][3] == atoms_new[where_c[0][i]][0] and \
                            bonds_new[where_bond[0][j]][2] != atoms_new[new_atoms][0]:
                        angles_new[new_angles][2] = bonds_new[where_bond[0][j]][2]                          # C
                        c_1 = bonds_new[where_bond[0][j]][2]

                angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                                     # C
                angles_new[new_angles][4] = atoms_new[new_atoms][0]                                         # H

                if cont_hidrogeno > 1:
                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 24                                                          # H-C-H
                    angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]                                 # H
                    angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                                 # C
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]                                     # H

                    if cont_hidrogeno == 3:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 24                                                      # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]                             # H
                        angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                             # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]                                 # H

                        if chain_length > 2:
                            bonds_new[new_bonds][1] = 14                                                    # C-C
                            angles_new[new_angles - 2][1] = 11                                              # C-C-C
                            angles_new[new_angles - 1][1] = 26                                              # C-C-H
                            angles_new[new_angles][1] = 26                                                  # C-C-H

                # 2) Adicion de diedros

            where_c1 = np.where(bonds_new == c_1)
            for j in range(len(where_c1[0][:])):
                if bonds_new[where_c1[0][j]][1] == 10 and bonds_new[where_c1[0][j]][2] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 35                                                    # N-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][3]                          # N
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                elif bonds_new[where_c1[0][j]][1] == 10 and bonds_new[where_c1[0][j]][3] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 35                                                    # N-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][2]                          # N
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                elif bonds_new[where_c1[0][j]][1] == 13 and bonds_new[where_c1[0][j]][2] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 34                                                    # H-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][3]                          # H
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                elif bonds_new[where_c1[0][j]][1] == 13 and bonds_new[where_c1[0][j]][3] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 34                                                    # H-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][2]                          # H
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                if int(chain_length) > 2:
                    if dihedrals_new[new_dihedrals - 1][1] == 35:
                        dihedrals_new[new_dihedrals - 1][1] = 37

                    elif dihedrals_new[new_dihedrals - 1][1] == 34:
                        dihedrals_new[new_dihedrals - 1][1] = 36

                    elif dihedrals_new[new_dihedrals][1] == 35:
                        dihedrals_new[new_dihedrals][1] = 37

                    elif dihedrals_new[new_dihedrals][1] == 34:
                        dihedrals_new[new_dihedrals][1] = 36

if carboxy_fraction > 0 and chain_length > 1:
    print("* Extensión de cadena de amida a 2 carbonos --> COMPLETADA")

#############################################
# ADICION DE H1, H2 Y H3 AL -CH3 DE PROPILO #
#############################################

if chain_length > 2:
    where_c = np.where(atoms_new == -66)
    for i in range(len(where_c[0][:])):
        atoms_new[where_c[0][i]][2] = 17

        # EXTENSION DE CADENA CARBONADA INICIANDO
        #  CON LA ADICION DE H1, H2 Y C2 SOBRE C1

        cont_carbono = 1
        cont_hidrogeno = 0
        for cont_ext in range(3):
            cont_hidrogeno += 1
            cont_carbono += 1

            new_atoms += 1
            atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
            constant = int(atoms_new[new_atoms][0])
            xyz_matrix[constant][0] = "H"
            atoms_new[new_atoms][1] = 1
            atoms_new[new_atoms][2] = 18
            atoms_new[new_atoms][3] = 0.060
            atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4]
            atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5]

            if cont_hidrogeno == 1:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] + 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            elif cont_hidrogeno == 2:
                atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4] - 1.0
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] + 1.0
                if atoms_new[where_c[0][i]][6] > 0:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                else:
                    atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
            else:
                atoms_new[new_atoms][5] = atoms_new[where_c[0][i]][5] - 1.0
                if chain_length == 3:
                    if atoms_new[where_c[0][i]][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 0.5
                else:
                    atoms_new[new_atoms][2] = 17
                    xyz_matrix[constant][0] = "C"
                    atoms_new[new_atoms][3] = -0.180

                    atoms_new[new_atoms][4] = atoms_new[where_c[0][i]][4]
                    if atoms_new[where_c[0][i]][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] + 1.3
                    else:
                        atoms_new[new_atoms][6] = atoms_new[where_c[0][i]][6] - 1.3

                    if cont_carbono < chain_length:
                        atoms_new[new_atoms][3] = -0.120
                        atoms_new[where_c[0][i]][3] = -0.120
                    elif cont_carbono == chain_length:
                        atoms_new[new_atoms][3] = -0.180
                        atoms_new[where_c[0][i]][3] = -0.120

            xyz_matrix[constant][1] = atoms_new[new_atoms][4]
            xyz_matrix[constant][2] = atoms_new[new_atoms][5]
            xyz_matrix[constant][3] = atoms_new[new_atoms][6]

            #  ADICION DE ENLACES, ANGULOS Y
            #  DIEDROS DE LA CADENA CARBONADA

            # 1) Adicion de enlaces y angulos

            if cont_hidrogeno <= 3:
                new_bonds += 1
                bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                bonds_new[new_bonds][1] = 13                                                                # H-C
                bonds_new[new_bonds][2] = atoms_new[where_c[0][i]][0]                                       # C
                bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                                           # H

                new_angles += 1
                angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                angles_new[new_angles][1] = 26
                bonds_new = np.array(bonds_new)
                where_bond = np.where(bonds_new == atoms_new[where_c[0][i]][0])

                for j in range(len(where_bond[0][:])):
                    if bonds_new[where_bond[0][j]][3] == atoms_new[where_c[0][i]][0] and \
                            bonds_new[where_bond[0][j]][2] != atoms_new[new_atoms][0]:
                        angles_new[new_angles][2] = bonds_new[where_bond[0][j]][2]                          # C
                        c_1 = bonds_new[where_bond[0][j]][2]

                angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                                     # C
                angles_new[new_angles][4] = atoms_new[new_atoms][0]                                         # H

                if cont_hidrogeno > 1:
                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 24                                                          # H-C-H
                    angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]                                 # H
                    angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                                 # C
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]                                     # H

                    if cont_hidrogeno == 3:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 24                                                      # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]                             # H
                        angles_new[new_angles][3] = atoms_new[where_c[0][i]][0]                             # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]                                 # H

                        if chain_length > 3:
                            bonds_new[new_bonds][1] = 14                                                    # C-C
                            angles_new[new_angles - 2][1] = 11                                              # C-C-C
                            angles_new[new_angles - 1][1] = 26                                              # C-C-H
                            angles_new[new_angles][1] = 26                                                  # C-C-H

            # 2) Adicion de diedros

            where_c1 = np.where(bonds_new == c_1)
            for j in range(len(where_c1[0][:])):
                if bonds_new[where_c1[0][j]][1] == 10 and bonds_new[where_c1[0][j]][2] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 36                                                    # C-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][3]                          # C
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                elif bonds_new[where_c1[0][j]][1] == 10 and bonds_new[where_c1[0][j]][3] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 36                                                    # C-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][2]                          # C
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                elif bonds_new[where_c1[0][j]][1] == 13 and bonds_new[where_c1[0][j]][2] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 34                                                    # H-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][3]                          # H
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

                elif bonds_new[where_c1[0][j]][1] == 13 and bonds_new[where_c1[0][j]][3] == c_1:
                    new_dihedrals += 1
                    dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                    dihedrals_new[new_dihedrals][1] = 34                                                    # H-C-C-H
                    dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][2]                          # H
                    dihedrals_new[new_dihedrals][3] = c_1                                                   # C
                    dihedrals_new[new_dihedrals][4] = atoms_new[where_c[0][i]][0]                           # C
                    dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                               # H

            if chain_length > 3 and cont_carbono <= chain_length:
                if dihedrals_new[new_dihedrals - 1][1] == 117:
                    dihedrals_new[new_dihedrals - 1][1] = 119

                elif dihedrals_new[new_dihedrals - 1][1] == 115:
                    dihedrals_new[new_dihedrals - 1][1] = 117

                elif dihedrals_new[new_dihedrals][1] == 117:
                    dihedrals_new[new_dihedrals][1] = 119

                elif dihedrals_new[new_dihedrals][1] == 115:
                    dihedrals_new[new_dihedrals][1] = 117

        if chain_length > 3:
            cont_carbono = 3
            cont_hidrogeno = 0
            k = 1
            while k <= 3:
                cont_hidrogeno += 1

                new_atoms += 1
                atoms_new[new_atoms][0] = len(atoms_array) + new_atoms + 1
                constant = int(atoms_new[new_atoms][0])
                xyz_matrix[constant][0] = "H"
                atoms_new[new_atoms][1] = 1
                atoms_new[new_atoms][2] = 18
                atoms_new[new_atoms][3] = 0.060
                atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4]
                atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5]

                if cont_hidrogeno == 1:
                    z = k
                    atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4] + 1.0
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5] + 1.0
                    if atoms_new[new_atoms - k][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.5
                elif cont_hidrogeno == 2:
                    z = k
                    atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4] - 1.0
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5] + 1.0
                    if atoms_new[new_atoms - k][6] > 0:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.5
                    else:
                        atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.5
                else:
                    cont_carbono += 1
                    atoms_new[new_atoms][5] = atoms_new[new_atoms - k][5] - 1.0
                    if cont_carbono < chain_length - 1:
                        atoms_new[new_atoms][2] = 17
                        xyz_matrix[constant][0] = "C"
                        atoms_new[new_atoms][3] = -0.120
                        if atoms_new[new_atoms - k][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 1.3
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 1.3
                        z = k
                        k = 0
                        cont_hidrogeno = 0

                    elif cont_carbono == chain_length - 1:
                        atoms_new[new_atoms - k][3] = -0.120
                        atoms_new[new_atoms][2] = 17
                        xyz_matrix[constant][0] = "C"
                        atoms_new[new_atoms][3] = -0.180
                        atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4]
                        if atoms_new[new_atoms - k][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.8
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.8
                        z = k
                        k = 0
                        cont_hidrogeno = 0

                    elif cont_carbono == chain_length:
                        z = k
                        atoms_new[new_atoms][4] = atoms_new[new_atoms - k][4]
                        if atoms_new[new_atoms - k][6] > 0:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] + 0.8
                        else:
                            atoms_new[new_atoms][6] = atoms_new[new_atoms - k][6] - 0.8

                xyz_matrix[constant][1] = atoms_new[new_atoms][4]
                xyz_matrix[constant][2] = atoms_new[new_atoms][5]
                xyz_matrix[constant][3] = atoms_new[new_atoms][6]

                #  ADICION DE ENLACES, ANGULOS Y
                #  DIEDROS DE LA CADENA CARBONADA

                # 1) Adicion de enlaces y angulos

                if cont_hidrogeno <= 3:
                    new_bonds += 1
                    bonds_new[new_bonds][0] = len(bonds_array) + new_bonds + 1
                    bonds_new[new_bonds][1] = 13
                    bonds_new[new_bonds][2] = atoms_new[new_atoms - z][0]                                   # C
                    bonds_new[new_bonds][3] = atoms_new[new_atoms][0]                                       # H
                    if atoms_new[new_atoms - z][3] == -0.120 and atoms_new[new_atoms][3] == -0.180:
                        bonds_new[new_bonds][1] = 14

                    new_angles += 1
                    angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                    angles_new[new_angles][1] = 26                                                          # H-C-C
                    m = 0
                    while m <= len(bonds_new) - 1:
                        if bonds_new[m][3] == atoms_new[new_atoms - z][0]:
                            if bonds_new[m][2] != atoms_new[new_atoms][0]:
                                angles_new[new_angles][2] = bonds_new[m][2]                                 # C
                                c_1 = bonds_new[m][2]
                        m += 1
                    angles_new[new_angles][3] = atoms_new[new_atoms - z][0]                                 # C
                    angles_new[new_angles][4] = atoms_new[new_atoms][0]                                     # H

                    if cont_hidrogeno > 1:
                        new_angles += 1
                        angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                        angles_new[new_angles][1] = 24
                        # H-C-H
                        angles_new[new_angles][2] = atoms_new[new_atoms - 1][0]                             # H
                        angles_new[new_angles][3] = atoms_new[new_atoms - z][0]                             # C
                        angles_new[new_angles][4] = atoms_new[new_atoms][0]                                 # H

                        if cont_hidrogeno == 3:
                            new_angles += 1
                            angles_new[new_angles][0] = len(angles_array) + new_angles + 1
                            angles_new[new_angles][1] = 24                                                  # H-C-H
                            angles_new[new_angles][2] = atoms_new[new_atoms - 2][0]                         # H
                            angles_new[new_angles][3] = atoms_new[new_atoms - z][0]                         # C
                            angles_new[new_angles][4] = atoms_new[new_atoms][0]                             # H

                            if chain_length > cont_carbono:
                                bonds_new[new_bonds][1] = 14                                                # C-C
                                angles_new[new_angles - 2][1] = 11                                          # C-C-C
                                angles_new[new_angles - 1][1] = 26                                          # C-C-H
                                angles_new[new_angles][1] = 26                                              # C-C-H

                # 2) Adicion de diedros

                where_c1 = np.where(bonds_new == c_1)
                for j in range(len(where_c1[0][:])):
                    if bonds_new[where_c1[0][j]][1] == 14 and bonds_new[where_c1[0][j]][2] == c_1 and \
                            bonds_new[where_c1[0][j]][3] != atoms_new[new_atoms - z][0]:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 36                                                # C-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][3]                      # C
                        dihedrals_new[new_dihedrals][3] = c_1                                               # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]                       # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                           # H

                    elif bonds_new[where_c1[0][j]][1] == 14 and bonds_new[where_c1[0][j]][3] == c_1 and \
                            bonds_new[where_c1[0][j]][2] != atoms_new[new_atoms - z][0]:
                        new_dihedrals += 1
                        dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                        dihedrals_new[new_dihedrals][1] = 36                                                # C-C-C-H
                        dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][2]                      # C
                        dihedrals_new[new_dihedrals][3] = c_1                                               # C
                        dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]                       # C
                        dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                           # H

                    elif bonds_new[where_c1[0][j]][1] == 13 and bonds_new[where_c1[0][j]][2] == c_1 and \
                            bonds_new[where_c1[0][j]][3] != atoms_new[new_atoms - z][0]:
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 34                                            # H-C-C-H
                            dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][3]                  # H
                            dihedrals_new[new_dihedrals][3] = c_1                                           # C
                            dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]                   # C
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                       # H

                    elif bonds_new[where_c1[0][j]][1] == 13 and bonds_new[where_c1[0][j]][3] == c_1 and \
                            bonds_new[where_c1[0][j]][2] != atoms_new[new_atoms - z][0]:
                            new_dihedrals += 1
                            dihedrals_new[new_dihedrals][0] = len(dihedrals_array) + new_dihedrals + 1
                            dihedrals_new[new_dihedrals][1] = 34                                            # H-C-C-H
                            dihedrals_new[new_dihedrals][2] = bonds_new[where_c1[0][j]][2]                  # H
                            dihedrals_new[new_dihedrals][3] = c_1                                           # C
                            dihedrals_new[new_dihedrals][4] = atoms_new[new_atoms - z][0]                   # C
                            dihedrals_new[new_dihedrals][5] = atoms_new[new_atoms][0]                       # H

                if chain_length >= cont_carbono and cont_hidrogeno == 3:
                    if dihedrals_new[new_dihedrals - 1][1] == 36:
                        dihedrals_new[new_dihedrals - 1][1] = 38

                    elif dihedrals_new[new_dihedrals - 1][1] == 34:
                        dihedrals_new[new_dihedrals - 1][1] = 36

                    elif dihedrals_new[new_dihedrals][1] == 36:
                        dihedrals_new[new_dihedrals][1] = 38

                    elif dihedrals_new[new_dihedrals][1] == 34:
                        dihedrals_new[new_dihedrals][1] = 36

                k += 1

if carboxy_fraction > 0 and chain_length > 2:
    print("* Extensión de cadena de amida a 3 o más carbonos --> COMPLETADA", "\n")


########################################################################################################################
#                               CREACCION DEL ARCHIVO TOPOLOGICO DATA FILE Y ARCHIVO XYZ                               #
########################################################################################################################

data_file = open('data_file.dat', 'w')
print('# Modelo de GO funcionalizado con alquil-aminas', file=data_file)
print(len(atoms_array) + new_atoms + 1, 'atoms', file=data_file)
print(len(bonds_array) + new_bonds + 1, 'bonds', file=data_file)
print(len(angles_array) + new_angles + 1, 'angles', file=data_file)
print(len(dihedrals_array) + new_dihedrals + 1, 'dihedrals', file=data_file)
print(len(impropers_array), 'impropers', '\n', file=data_file)

print(18, 'atom types', file=data_file)
print(14, 'bond types', file=data_file)
print(27, 'angle types', file=data_file)
print(38, 'dihedral types', file=data_file)
print(2, 'improper types', '\n', file=data_file)

print(0, int(x_max + 1.5), 'xlo xhi', file=data_file)
print(0, int(y_max + 1.1), 'ylo yhi', file=data_file)
print(0, 100, 'zlo zhi', '\n', file=data_file)

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
print('2      10.0     180.0', '\n', file=data_file)

print('Atoms', '\n', file=data_file)

i = 0
while i <= len(atoms_array) - 1:
    print(int(atoms_array[i][0]), int(atoms_array[i][1]), int(atoms_array[i][2]), atoms_array[i][3], atoms_array[i][4],
          atoms_array[i][5], atoms_array[i][6], sep='   ', file=data_file)
    i += 1

i = 0
while i <= len(atoms_new) - 1:
    if atoms_new[i][0] != 0:
        print(int(atoms_new[i][0]), int(atoms_new[i][1]), int(atoms_new[i][2]), atoms_new[i][3], atoms_new[i][4],
              atoms_new[i][5], atoms_new[i][6], sep='   ', file=data_file)
    else:
        i = len(atoms_new) - 1
    i += 1

print('\n', 'Bonds', '\n', file=data_file)

i = 0
while i <= len(bonds_array) - 1:
    print(int(bonds_array[i][0]), int(bonds_array[i][1]), int(bonds_array[i][2]), int(bonds_array[i][3]), sep=' ',
          file=data_file)
    i += 1

i = 0
while i <= len(bonds_new) - 1:
    if bonds_new[i][0] != 0:
        print(int(bonds_new[i][0]), int(bonds_new[i][1]), int(bonds_new[i][2]), int(bonds_new[i][3]), sep=' ',
              file=data_file)
    else:
        i = len(bonds_new) - 1
    i += 1

print('\n', 'Angles', '\n', file=data_file)
i = 0
while i <= len(angles_array) - 1:
    print(int(angles_array[i][0]), int(angles_array[i][1]), int(angles_array[i][2]), int(angles_array[i][3]),
          int(angles_array[i][4]), sep=' ', file=data_file)
    i += 1

i = 0
while i <= len(angles_new) - 1:
    if angles_new[i][0] != 0:
        print(int(angles_new[i][0]), int(angles_new[i][1]), int(angles_new[i][2]), int(angles_new[i][3]),
              int(angles_new[i][4]), sep=' ', file=data_file)
    else:
        i = len(angles_new) - 1
    i += 1

print('\n', 'Dihedrals', '\n', file=data_file)
i = 0
while i <= len(dihedrals_array) - 1:
    print(int(dihedrals_array[i][0]), int(dihedrals_array[i][1]), int(dihedrals_array[i][2]),
          int(dihedrals_array[i][3]), int(dihedrals_array[i][4]), int(dihedrals_array[i][5]), sep=' ', file=data_file)
    i += 1

i = 0
while i <= len(dihedrals_new) - 1:
    if dihedrals_new[i][0] != 0:
        print(int(dihedrals_new[i][0]), int(dihedrals_new[i][1]), int(dihedrals_new[i][2]), int(dihedrals_new[i][3]),
              int(dihedrals_new[i][4]), int(dihedrals_new[i][5]), sep=' ', file=data_file)
    else:
        i = len(dihedrals_new) - 1
    i += 1

print('\n', 'Impropers', '\n', file=data_file)
i = 0
while i <= len(impropers_array) - 1:
    print(int(impropers_array[i][0]), int(impropers_array[i][1]), int(impropers_array[i][2]),
          int(impropers_array[i][3]), int(impropers_array[i][4]), int(impropers_array[i][5]), sep=' ', file=data_file)
    i += 1
data_file.close()

xyz_file = open('data_file.xyz', 'w')
print(int(len(atoms_array) + new_atoms + 1), '\n', file=xyz_file)
i = 0
cont_zero = 0
while i <= len(xyz_matrix) - 1:
    if xyz_matrix[i][0] != 0 and cont_zero < 2:
        print(xyz_matrix[i][0], xyz_matrix[i][1], xyz_matrix[i][2], xyz_matrix[i][3], sep=' ', file=xyz_file)
    else:
        cont_zero += 1
        if cont_zero == 2:
            i = len(xyz_matrix) - 1
    i += 1
xyz_file.close()

print("* Generación de topología y archivo xyz -> COMPLETADA")
