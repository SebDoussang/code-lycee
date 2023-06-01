Grille= [[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0
[0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1
[0, 0, 0, 0, 1, 3, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#2
[0, 0, 1, 1, 1, 2, 2, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],#3
[0, 0, 1, 2, 2, 3, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],#4
[1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],#5
[1, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 4, 1],#6 
[1, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],#7
[1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1,5, 1, 1, 2, 2, 2, 2, 1], #8 Sokoban ici
[0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],#9
[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]#10

nb_caisse=6
ligneSokoban = 8
colonneSokoban= 11

def representerLigne(ligne) :
        affichage=""
        for case in ligne:
            if case==0 :
                symbole=" "#rien
            elif case==1 :
                symbole="M"#mur
            elif case==2 :
                symbole=" "#libre
            elif case==3 :
                symbole="C"#caisse
            elif case==4 :
                symbole="O"#objectif
            elif case==5 :
                symbole="S"#sokoban
            affichage=affichage+symbole
        print(affichage)

def representer(jeu) :
    for ligne in jeu :
        representerLigne(ligne)

z= "z"
Z="Z"
q="q"
Q="Q"
s="s"
S="S"
d="d"
D="D"

def deplacer(direction) :
    """
    La variable locale direction est une chaˆıne de caract`ere :
    "z" : aller en haut
    "q" : aller `a gauche
    "d" : aller `a droite
    "s" : aller en bas
    """
    global Grille
    global ligneSokoban
    global colonneSokoban
    global nb_caisse
    
    if direction=="Z" or direction=="z" :
        if Grille[ligneSokoban-1][colonneSokoban] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            ligneSokoban -= 1
            Grille[ligneSokoban][colonneSokoban] = 5
            
        elif Grille[ligneSokoban-1][colonneSokoban] == 3:
            if Grille[ligneSokoban-2][colonneSokoban] == 2 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban -= 1
                Grille[ligneSokoban][colonneSokoban] = 5
                Grille[ligneSokoban-1][colonneSokoban]=3
        
            elif Grille[ligneSokoban-2][colonneSokoban] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban -= 1
                Grille[ligneSokoban][colonneSokoban] = 5

                

    if direction=="Q" or direction=="q" :
        if Grille[ligneSokoban][colonneSokoban-1] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            colonneSokoban -= 1
            Grille[ligneSokoban][colonneSokoban] = 5
            
        elif Grille[ligneSokoban][colonneSokoban-1] == 3:
            if Grille[ligneSokoban][colonneSokoban-2] == 2 :
                Grille[ligneSokoban][colonneSokoban] = 2
                colonneSokoban -= 1
                Grille[ligneSokoban][colonneSokoban] = 5
                Grille[ligneSokoban][colonneSokoban-1]=3
        
            elif Grille[ligneSokoban][colonneSokoban-2] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                colonneSokoban -= 1
                Grille[ligneSokoban][colonneSokoban] = 5
            
            
    if direction=="D" or direction=="d" :
        if Grille[ligneSokoban][colonneSokoban+1] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            colonneSokoban += 1
            Grille[ligneSokoban][colonneSokoban] = 5
            
        elif Grille[ligneSokoban][colonneSokoban+1] == 3:
            if Grille[ligneSokoban][colonneSokoban+2] == 2 :
                Grille[ligneSokoban][colonneSokoban] = 2
                colonneSokoban += 1
                Grille[ligneSokoban][colonneSokoban] = 5
                Grille[ligneSokoban][colonneSokoban+1]=3
        
            elif Grille[ligneSokoban][colonneSokoban] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban -= 1
                Grille[ligneSokoban][colonneSokoban] = 5
                
        
    if direction=="S" or direction=="s" :
        if Grille[ligneSokoban+1][colonneSokoban] == 2:
            Grille[ligneSokoban][colonneSokoban] = 2
            ligneSokoban += 1
            Grille[ligneSokoban][colonneSokoban] = 5
            
        elif Grille[ligneSokoban+1][colonneSokoban] == 3:
            if Grille[ligneSokoban+2][colonneSokoban] == 2 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban += 1
                Grille[ligneSokoban][colonneSokoban] = 5
                Grille[ligneSokoban+1][colonneSokoban]=3
        
            elif Grille[ligneSokoban+2][colonneSokoban] == 4 :
                Grille[ligneSokoban][colonneSokoban] = 2
                ligneSokoban += 1
                Grille[ligneSokoban][colonneSokoban] = 5



def jouer_Sokoban():
    global Grille
    global ligneSokoban
    global colonneSokoban
    global nb_caisse
    representer(Grille)
    reponse="nImporteQuoi"
    while reponse!="r" and nb_caisse!=0:
        reponse=input("Votre d´eplacement (z/q/s/d) ou r pour recommencer ?")
        deplacer(reponse)
        representer(Grille)
    if reponse=="r":
        print("ce n'est pas grave, tu feras mieux la prochaine fois...")
    else :
        print("Bravo !!!")
    try_again=input("Voulez vous refaire une partie (y/n - y par d´efaut)")
    if try_again!="n":
        jouer_Sokoban()
    else :
        print("A bient^ot")
