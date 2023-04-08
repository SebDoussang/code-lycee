import random

def jeu_de():
    dice_n = 0
    dice = []
    total = 0

    print("bienvenue sur le meilleur jeu de dé du monde !!!!!!!")
    choice=int(input("entrer un nombre de dé (max 100):"))
    while True:
        if choice > 100:
            print("erreur")
            choice = int(input("entrer un nombre de dé (max 100):"))
        else:
            break

    pari = input("faire un pari ? (oui/non)").lower()
    running = 1
    while running == 1 :
        if pari == "oui":
            j_1 = input("nom du joueur 1:")
            j_2 = input("nom du joueur 2:")
            p_j_1 = int(input(f"prediction du joueur 1"))
            p_j_2 = int(input(f"prediction du joueur 2"))
            a_pari = input("combien parier$$ (le total revient au vainqueur) :")
        elif pari == "non":
            pass
        elif not pari == "non" or "oui":
            print("erreur (run again)")
            running = 0

        for i in range(choice):
            dice_n = random.randint(1,6)
            dice.append(dice_n)
            #print("dé", i+1, "=", dice_n) #pour afficher les resultats des dés

        for i in dice:
            total += i
        if pari == "oui":
            print("______________________________")
            print("le total est:", total)
            print(j_1, "a predit", p_j_1)
            print(j_2, "a predit", p_j_2)
            result_dej1 = total - p_j_1
            result_dej2 = total - p_j_2
            result_dej1 = abs(result_dej1)
            result_dej2 = abs(result_dej2)
            if result_dej1 < result_dej2:
                win = j_1
            if result_dej2 < result_dej1:
                win = j_2
            print("la somme de", a_pari, "revient a", win)
        if pari == "non":
            print("______________________________")
            print("le total est:", total)
            print("(fait un pari c'est mieux !)")

        print("______________________________")
        again = input("play again ???")
        if again == "oui":
            jeu_de()
        elif pari == "non":
            print("thanks for playing (run again to play)")
            running = 0
        running = 0

jeu_de()
