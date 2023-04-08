import pygame

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre
width, height = 640, 480

# Créer la fenêtre
screen = pygame.display.set_mode((width, height))

# Définir le titre de la fenêtre
pygame.display.set_caption("Tetris")

# Définir les couleurs
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Définir les dimensions d'une case (carré) du Tetris
block_size = 30

# Définir la grille du Tetris
grid_width = 10
grid_height = 20
grid = []
for i in range(grid_height):
    grid.append([0] * grid_width)

# Classe qui représente une forme (un Tetrimino)
class Shape:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = green

# Créer une forme (un Tetrimino)
shape = Shape(5, 0, [[1, 1, 1], [0, 1, 0]])

# Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner la grille et les formes
    screen.fill(black)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, blue, (j * block_size, i * block_size, block_size, block_size))
    for i in range(len(shape.shape)):
        for j in range(len(shape.shape[i])):
            if shape.shape[i][j] == 1:
                pygame.draw.rect(screen, shape.color, ((shape.x + j) * block_size, (shape.y + i) * block_size, block_size, block_size))

    # Mettre à jour l'affichage
    pygame.display.update()

# Quitter pygame
pygame.quit()
