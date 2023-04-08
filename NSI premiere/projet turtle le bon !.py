from turtle import * # importation du module turtle
from random import choice # importation du module choice
from time import sleep # importation du module sleep

def menu():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  bgcolor("black") # changer la couleur de fond
  pencolor("white") # choix de la couleur du crayon
  up() # lever le crayon
  goto(-50,50) # va à la position -50,50
  down() # poser le crayon
  write("bienvenue ! Choisir qu'elle fonction appeller :") # écrire du texte
  up() # lever le crayon
  goto(-50,30) # va à la position -50,30
  write("spirale(), fleur(), triangle(), cercle_trait(), etoile(), cercle_carre(), avenger()") # écrire du texte
  up() # lever le crayon
  goto(-50,10) # va à la position -50,10
  down() # poser le crayon
  write("(le dessin mettra 15 secondes a disparaitre)") # écrire du texte
menu() # appel de la fonction menu

def spirale():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  speed(0) # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  width(3)
  couleur_alea = ['purple', 'blue','red'] # creation d'une liste
  goto(0,0) # revient à la position initiale
  for i in range(500): # création d'une boucle
    pencolor(choice(couleur_alea)) # choix de la couleur du crayon aléatoire parmis les couleur de "couleur_alea"
    forward(10+i) # la tortue avance de 10 pixels + i
    right(89) # la tortue tourne sur elle-même de 89° à droite
  sleep(15) # met le programme en pause 15 secondes
  menu() # appel de la fonction menu

def fleur():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  speed(0) # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  couleur = ["orange","red"] # creation d'une liste
  for i in range(120): # création d'une boucle
    for c in couleur: # création d'une boucle
      pencolor(c) # choix de la couleur du crayon dans "couleur"
      circle(80+i, 100) # trace un arc de cercle d’angle 80+i et de rayon 100
      left(90) # la tortue tourne sur elle-même de 90° à gauche
      circle(80+i, 100) # trace un arc de cercle d’angle 80+i et de rayon 100
      right(60) # la tortue tourne sur elle-même de 60° à droite
  sleep(15) # met le programme en pause 15 secondes
  menu() # appel de la fonction menu

def triangle():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  pencolor("cyan") # choix de la couleur du crayon
  speed(0) # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  up()
  goto(100,-50)
  down()
  for i in range(3): # création d'une boucle
    for i in range(3): # création d'une boucle
      for i in range(3): # création d'une boucle
        for i in range(3): # création d'une boucle
          for i in range(3): # création d'une boucle
            for i in range(3): # création d'une boucle
              for i in range(3): # création d'une boucle
                right(-120) # la tortue tourne sur elle-même de -120° à droite
                forward(8) # la tortue avance de 8 pixels
              right(-120) # la tortue tourne sur elle-même de -120° à droite
              forward(16) # la tortue avance de 16 pixels
            right(-120) # la tortue tourne sur elle-même de -120° à droite
            forward(32) # la tortue avance de 32 pixels
          right(-120) # la tortue tourne sur elle-même de -120° à droite
          forward(64) # la tortue avance de 64 pixels
        right(-120) # la tortue tourne sur elle-même de -120° à droite
        forward(128) # la tortue avance de 128 pixels
      right(-120) # la tortue tourne sur elle-même de -120° à droite
      forward(256) # la tortue avance de 256 pixels
    right(-120) # la tortue tourne sur elle-même de -120° à droite
    forward(512) # la tortue avance de 512 pixels
  sleep(15) # met le programme en pause 15 secondes
  menu() # appel de la fonction menu

def cercle_trait():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  speed(0) # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  couleur = ["red", "blue"] # creation d'une liste
  for i in range(180): # création d'une boucle
    for c in couleur: # création d'une boucle
      pencolor(c) # choix de la couleur du crayon dans "couleur"
      up() # lever le crayon
      goto(0,0) # revient à la position initiale
      down() # poser le crayon
      for f in range(3): # création d'une boucle
        forward(50) # la tortue avance de 50 pixels
        left(20) # la tortue tourne sur elle-même de 20° à gauche
        forward(25) # la tortue avance de 25 pixels
        right(20) # la tortue tourne sur elle-même de 20° à droite
        forward(50) # la tortue avance de 50 pixels
      left(1) # la tortue tourne sur elle-même de 1° à gauche
  sleep(15) # met le programme en pause 15 secondes
  menu() # appel de la fonction menu

def etoile():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  speed(0) # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  couleur = ["blue", "purple"] # creation d'une liste
  for i in range(100): # création d'une boucle
    for c in couleur: # création d'une boucle
      pencolor(c) # choix de la couleur du crayon dans "couleur"
      forward(i*5) # la tortue avance de 5 pixels multiplié par i
      left(200) # la tortue tourne sur elle-même de 200° à gauche
  sleep(15) # met le programme en pause 15 secondes
  menu() # appel de la fonction menu

def cercle_carre():
  reset() # tout effacer et recommencer à zéro
  ht() # cache la tortue
  speed(0) # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  pencolor("grey")
  for i in range(36): # création d'une boucle
    for f in range(4): # création d'une boucle
      forward(75) # la tortue avance de 75 pixels
      left(90) # la tortue tourne sur elle-même de 20° à gauche
    left(10) # la tortue tourne sur elle-même de 10° à gauche
  sleep(15) # met le programme en pause 15 secondes
  menu() # appel de la fonction menu

def cercle():
  reset()  # tout effacer et recommencer à zéro
  ht()  # cache la tortue
  speed(0)  # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  fillcolor("red")  # choix de la couleur de remplissage
  begin_fill()  # activer le mode remplissage
  circle(110)  # trace un cercle de rayon 110
  end_fill()
  left(90)  # la tortue tourne sur elle-même de 90° à gauche
  up()  # lever le crayon
  forward(25)  # la tortue avance de 25 pixels
  down()  # poser le crayon
  right(90)  # la tortue tourne sur elle-même de 90° à droite
  fillcolor("black")  # choix de la couleur de remplissage
  pencolor("black")  # choix de la couleur du crayon
  begin_fill()  # activer le mode remplissage
  circle(85)  # trace un cercle de rayon 85
  circle(85)  # trace un cercle de rayon 85
  end_fill()

def avenger():
  reset()  # tout effacer et recommencer à zéro
  ht()  # cache la tortue
  cercle()  # appel de la fonction cercle
  speed(5)  # parametragede la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
  fillcolor("white")  # choix de la couleur de remplissage
  pencolor("white")  # choix de la couleur du crayon
  up()  # lever le crayon
  goto(-100, 10)  # va à la position -100,10
  down()  # poser le crayon
  left(60)  # la tortue tourne sur elle-même de 60° à gauche
  up()  # lever le crayon
  backward(30)  # la tortue recule de 30 pixels
  down()  # poser le crayon
  begin_fill()  # activer le mode remplissage
  forward(280)  # la tortue avance de 280 pixels
  right(60)  # la tortue tourne sur elle-même de 60° à droite
  forward(30)  # la tortue avance de 30 pixels
  right(90)  # la tortue tourne sur elle-même de 90° à droite
  forward(150)  # la tortue avance de 150 pixels
  up()  # lever le crayon
  forward(41)  # la tortue avance de 41 pixels
  down()  # poser le crayon
  forward(30)  # la tortue avance de 30 pixels
  right(90)  # la tortue tourne sur elle-même de 90° à droite
  forward(30)  # la tortue avance de 30 pixels
  right(133)  # la tortue tourne sur elle-même de 133° à droite
  forward(42)  # la tortue avance de 42 pixels
  up()  # lever le crayon
  left(41)  # la tortue tourne sur elle-même de 41° à gauche
  forward(41)  # la tortue avance de 41 pixels
  left(180)  # la tortue tourne sur elle-même de 180° à gauche
  down()  # poser le crayon
  right(130)  # la tortue tourne sur elle-même de 130° à droite
  forward(40)  # la tortue avance de 40 pixels
  right(50)  # la tortue tourne sur elle-même de 50° à droite
  forward(70)  # la tortue avance de 70 pixels
  left(154)  # la tortue tourne sur elle-même de 154° à gauche
  forward(216)  # la tortue avance de 216 pixels
  right(62)  # la tortue tourne sur elle-même de 62° à droite
  forward(40)  # la tortue avance de 40 pixels
  end_fill()  # desactiver le mode remplissage
  begin_fill() # activer le mode remplissage
  up()  # lever le crayon
  backward(40)  # la tortue recule de 40 pixels
  right(120)  # la tortue tourne sur elle-même de 120° à droite
  forward(77)  # la tortue avance de 77 pixels
  right(60)  # la tortue tourne sur elle-même de 60° à droite
  backward(2)  # la tortue recule de 2 pixels
  down()  # poser le crayon
  forward(62)  # la tortue avance de 62 pixels
  right(90)  # la tortue tourne sur elle-même de 90° à droite
  forward(25)  # la tortue avance de 25 pixels
  left(137)  # la tortue tourne sur elle-même de 137° à gauche
  forward(45)  # la tortue avance de 25 pixels
  left(87)  # la tortue tourne sur elle-même de 87° à gauche
  forward(45)  # la tortue avance de 45 pixels
  left(138)  # la tortue tourne sur elle-même de 138° à gauche
  forward(25)  # la tortue avance de 25 pixels
  right(93)  # la tortue tourne sur elle-même de 93° à droite
  forward(55)  # la tortue avance de 55 pixels
  end_fill()  # activer le mode remplissage
  sleep(15)  # met le programme en pause 15 secondes
  menu()  # appel de la fonction menu