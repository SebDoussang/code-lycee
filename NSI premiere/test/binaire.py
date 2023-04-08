def dec2bin(nombre):

    binaire = []
    binaire.append(nombre%2)

    while nombre >= 2:
        nombre =nombre//2
        binaire.append(nombre%2)
    while len(binaire) < 7:
        binaire.append(0)
    binaire.reverse()
    mot = ''.join(str(element) for element in binaire)
    print(mot)

def dec2bin_negatif(nombre):
    if nombre >= 0:
        print("le nombre est positif")
        dec2bin(nombre)

    elif nombre < 0:
        pass

