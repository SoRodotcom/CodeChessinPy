def affichage(tab, couleur="blanc"):
    """Affiche en theorie la grille pour l'utilisateur en fonction de sa couleur(qui se trouvera en bas)CASSE 
    ACTUELEMENT"""
    for y in range(len(tab)):
        for x in range(len(tab[y])):
            if couleur == "blanc":
                tmp = tab[y][x]
            else:
                tmp = tab[y - 1][x - 1]
            if tmp[0] == "0":
                if x + y % 2 == 0:
                    print("■", end='')
                else:
                    print("▢", end='')
            elif tmp[0] == "P":
                if tmp[1] == "b":
                    print("♙", end='')
                else:
                    print("♟︎", end='')
            elif tmp[0] == "F":
                if tmp[1] == "b":
                    print("♗", end='')
                else:
                    print("♝", end='')
            elif tmp[0] == "T":
                if tmp[1] == "b":
                    print("♖", end='')
                else:
                    print("♜", end='')
            elif tmp[0] == "C":
                if tmp[1] == "b":
                    print("♘", end='')
                else:
                    print("♞", end='')
            elif tmp[0] == "D":
                if tmp[1] == "b":
                    print("♕", end='')
                else:
                    print("♛", end='')
            elif tmp[0] == "R":
                if tmp[1] == "b":
                    print("♔", end='')
                else:
                    print("♚", end='')
        print('')


def hors_limite(deplacements):
    """Enleve les valeures se trouvant hors de l'echiquier du tableau deplacement"""
    for e in range(len(deplacements)):
        if 0 > deplacements[e][0] > 7 or 0 > deplacements[e][1] > 7:
            del deplacements[e]
    return deplacements


def cavalier(x, y):
    """Calcule les deplacements possible du cavalier en x,y (respectivement colonne et ligne)"""
    deplacements = [[x + 2, y - 1], [x + 2, y + 1], [x - 2, y - 1], [x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2],
                    [x - 1, y - 2], [x + 1, y - 2]]
    hors_limite(deplacements)
    return deplacements


def pion(x, y, tab, name):
    """Calcule les deplacements possible du pion en x,y (respectivement colonne et ligne), tient compte des pieces 
    autours"""
    if name[1] == "b":
        deplacements = [[y - 1]]
        if y > 1:
            if tab[x + 1][y + 1] != 0:
                deplacements.append([x + 1, y - 1])
            if tab[x - 1][y - 1] != 0:
                deplacements.append([x - 1, y - 1])
        if name[2] == "0":
            deplacements.append(y + 2)

    else:  # elif name[1] == "n":
        deplacements = [[y + 1]]
        if y < 7:
            if tab[x + 1][y + 1] != 0:
                deplacements.append([x + 1, y + 1])
            if tab[x - 1][y - 1] != 0:
                deplacements.append([x - 1, y + 1])
        if name[2] == "0":
            deplacements.append([y - 2])

    return deplacements


def fou(x, y):
    """Calcule les deplacements possible du fou en x,y (respectivement colonne et ligne)"""
    deplacements = []
    for i in range(8):
        deplacements.append([x - 1, y - 1])
        deplacements.append([x + 1, y - 1])
        deplacements.append([x + 1, y + 1])
        deplacements.append([x + 1, y + 1])
    hors_limite(deplacements)
    return deplacements


def roi(x, y):
    """Calcule les deplacements possible du roi en x,y (respectivement colonne et ligne)"""
    deplacements = [[x + 1, y + 1], [x - 1, y + 1], [x + 1, y - 1], [x - 1, y - 1]]
    hors_limite(deplacements)
    return deplacements


def dame(x, y):
    """Calcule les deplacements possible de la dame en x,y (respectivement colonne et ligne)"""
    deplacements = []
    for i in range(8):
        deplacements.append([x + i, y + i])
        deplacements.append([x - i, y + i])
        deplacements.append([x + i, y - i])
        deplacements.append([x - i, y - i])
    hors_limite(deplacements)
    return deplacements


def piece(name, x, y, tab):
    """Renvoie les deplacements en possibles en fonction de la piece selectionee"""
    deplacements = None
    if name[0] == "P":
        deplacements = pion(x, y, tab, name)
    elif name[0] == "C":
        deplacements = cavalier(x, y)
    elif name[0] == "F":
        deplacements = fou(x, y)
    elif name[0] == "D":
        deplacements = dame(x, y)
    elif name[0] == "R":
        deplacements = roi(x, y)
    elif name[0] == "0":
        return deplacements  # Signifie que le joueur a tenté de selectionner une case vide
    return deplacements

# tab =[["0"]for i in range(8) for i in range(8)]
# affichage(tab)
