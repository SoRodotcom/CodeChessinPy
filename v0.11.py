def affichage(tab, couleur="blanc"):
    for y in range(len(tab)):
        for x in range(len(tab[y])):
            if couleur == "blanc":
                tmp = tab[y][x]
            else:
                tmp = tab[y - 1][x - 1]
            if tmp[0] == "R":
                if tmp[1] == "b":
                    print("♔", end='')
                else:
                    print("♚", end='')
            elif tmp[0] == "D":
                if tmp[1] == "b":
                    print("♕", end='')
                else:
                    print("♛", end='')
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
            elif tmp[0] == "P":
                if tmp[1] == "b":
                    print("♙", end='')
                else:
                    print("♟︎", end='')
        print()


def cavalier(x, y):
    deplacements = [[x + 2, y - 1], [x + 2, y + 1], [x - 2, y - 1], [x - 2, y + 1], [x - 1, y + 2], [x + 1, y + 2],
                    [x - 1, y - 2], [x + 1, y - 2]]
    for e in range(len(deplacements)):
        if 0 > deplacements[e][0] > 7 or 0 > deplacements[e][1] > 7:
            del deplacements[e]
    return deplacements


def pion(x, y, tab, name):
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
    deplacements = []
    for i in range(8):
        deplacements.append([x - 1, y - 1])
        deplacements.append([x + 1, y - 1])
        deplacements.append([x + 1, y + 1])
        deplacements.append([x + 1, y + 1])
    for e in range(len(deplacements)):
        if 0 > deplacements[e][0] > 7 or 0 > deplacements[e][1] > 7:
            del deplacements[e]


def roi(x, y):
    deplacements = [[x + 1, y + 1], [x - 1, y + 1], [x + 1, y - 1], [x - 1, y - 1]]
    for e in range(len(deplacements)):
        if 0 > deplacements[e][0] > 7 or 0 > deplacements[e][1] > 7:
            del deplacements[e]


def dame(x, y):
    deplacements = []
    for i in range(8):
        deplacements.append([x + i, y + i])
        deplacements.append([x - i, y + i])
        deplacements.append([x + i, y - i])
        deplacements.append([x - i, y - i])
    for e in range(len(deplacements)):
        if 0 > deplacements[e][0] > 7 or 0 > deplacements[e][1] > 7:
            del deplacements[e]


def piece(name, x, y, tab):
    if name[0] == "R":
        roi(x, y)
    elif name[0] == "D":
        dame(x, y)
    elif name[0] == "F":
        fou(x, y)
    elif name[0] == "C":
        cavalier(x, y)
    elif name[0] == "P":
        pion(x, y, tab, name)
