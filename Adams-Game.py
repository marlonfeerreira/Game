import pygame

pygame.init()
pygame.mixer.init()

import os

# Define as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define as dimensões da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Cria um objeto de tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a música tema da família Addams
pygame.mixer.music.load("family-addams-theme.mp3")
pygame.mixer.music.play(-1)

# Cria os personagens
gomez = pygame.image.load("gomez.png")
morticia = pygame.image.load("morticia.png")
wednesday = pygame.image.load("wednesday.png")
pugsley = pygame.image.load("pugsley.png")
fester = pygame.image.load("fester.png")
lurch = pygame.image.load("lurch.png")
thing = pygame.image.load("thing.png")
granny_frump = pygame.image.load("granny-frump.png")

# Cria os objetos
hammer = pygame.image.load("hammer.png")
book_of_spells = pygame.image.load("book-of-spells.png")
book_of_puzzles = pygame.image.load("book-of-puzzles.png")
knife = pygame.image.load("knife.png")
bomb = pygame.image.load("bomb.png")
map = pygame.image.load("map.png")
treasure = pygame.image.load("treasure.png")

# Cria uma lista de inimigos
enemies = []

# Cria uma lista de quebra-cabeças
puzzles = []

# Cria uma lista de tesouros
treasures = []

# Cria uma função para desenhar os personagens
def draw_characters(characters):
    for character in characters:
        screen.blit(character, character.rect)

# Cria uma função para desenhar os objetos
def draw_objects(objects):
    for object in objects:
        screen.blit(object, object.rect)

# Cria uma função para desenhar os inimigos
def draw_enemies(enemies):
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)

# Cria uma função para desenhar os quebra-cabeças
def draw_puzzles(puzzles):
    for puzzle in puzzles:
        screen.blit(puzzle.image, puzzle.rect)

# Cria uma função para desenhar os tesouros
def draw_treasures(treasures):
    for treasure in treasures:
        screen.blit(treasure.image, treasure.rect)

# Cria uma função para verificar se o jogador colidiu com um inimigo
def check_collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

# Cria uma função para verificar se o jogador completou um quebra-cabeça
def check_puzzle_completion(puzzle):
    for object in objects:
        if object.rect.colliderect(puzzle.rect):
            return True
    return False

# Cria uma função para verificar se o jogador encontrou um tesouro
def check_treasure_found(treasure):
    if treasure.rect.colliderect(player.rect):
        return True
    return False

# Cria uma função para mover o jogador
def move_player(keys, player):
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

# Cria uma função para atualizar o jogo
def update_game(characters, objects, enemies, puzzles, treasures):
    for character in characters:
        character.update()
    for object in objects:
        object.update()
    for enemy in enemies:
        enemy.update()
    for puzzle in puzzles:
        puzzle.update()
    for treasure in treasures:
        treasure.update()

# Cria uma função para verificar se o jogo terminou
def check_game_over(characters, enemies, puzzles, treasures):
    for enemy in enemies:
        if check_collision(characters[0], enemy):
            return True
    for puzzle in puzzles:
        if not check_puzzle_completion(puzzle):
            return True
    for treasure in treasures:
        if not check_treasure_found(treasure):
            return True
    return False

# Cria uma função principal para executar o jogo
def main():
    # Inicializa o jogo
    pygame.init()

    # Define a posição do jogador
    player = Gomez(50, 50)

    # Define a lista de personagens
    characters = [player]

    # Define a lista de objetos
    objects = [hammer, book_of_spells, book_of_puzzles]

    # Define a lista de inimigos
    enemies = [Frankenstein, Mummy]

    # Define a lista de quebra-cabeças
    puzzles = [Puzzle1, Puzzle2]

    # Define a lista de tesouros
    treasures = [Treasure]

    # Inicia o loop principal do jogo
    running = True
    while running:
        # Limpa a tela
        screen.fill(BLACK)

        # Desenha os personagens
        draw_characters(characters)

        # Desenha os objetos
        draw_objects(objects)

        # Desenha os inimigos
        draw_enemies(enemies)

        # Desenha os quebra-cabeças
        draw_puzzles(puzzles)

        # Desenha os tesouros
        draw_treasures(treasures)

        # Processa os eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack()
                if event.key == pygame.K_RETURN:
                    player.interact()

        # Atualiza o jogo
        update_game(characters, objects, enemies, puzzles, treasures)

        # Verifica se o jogo terminou
        if check_game_over(characters, enemies, puzzles, treasures):
            running = False

        # Atualiza a tela
        pygame.display.update()

    pygame.quit()

# Chama a função principal
if __name__ == "__main__":
    main()

