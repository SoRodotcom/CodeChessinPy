def Affichage(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tmp = tab[i][j]
            if tmp[0] == "R":
                if tmp[1] == "b":
                    print("Roi blanc", end = '')
                else:
                    print("Roi noir", end ='')
            elif tmp[0] == "D":
                if tmp[1] == "b":
                    print("Dame blanc", end = '')
                else:
                    print("Dame noir", end = '')
            elif tmp[0] == "F":
                if tmp[1] == "b":
                    print("Fou blanc", end = '')
                else:
                    print("Fou noir", end = '')
            elif tmp[0] == 'T':
                if tmp[1] == "b":
                    print("Tour blanche", end = '')
                else:
                    print("Tour noire", end = '')
            elif tmp[0] == 'C':
                if tmp[1] == 'b':
                    print("Cavalier blanc", end ='')
                else:
                    print("Cavalier noir", end = '')
            elif tmp[0] == 'P':
                if tmp[1] == 'b':
                    print('Pion Blanc', end = '')
                else:
                    print('Pion Noir', end = '')
            
            
        print()