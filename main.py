import pygame
import random
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

clock = pygame.time.Clock()

leaves = []

red_leaf = pygame.transform.scale(pygame.image.load('red_leaf.png'), (108, 138))
red_leaf.set_colorkey((247, 247, 247))
many_leaves = pygame.transform.scale(pygame.image.load('several-fall-leaves.png'), (108, 138))
many_leaves.set_colorkey((247, 247, 247))

running = True
while running:
    mx, my = pygame.mouse.get_pos()

    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    leaves.append([random.randint(0, screen_width), random.uniform(4, 5), 0, random.randint(0, 360),
                   random.randint(-100, 100)])
    for leaf in leaves:
        leaf[2] += leaf[1]
        rotated_leaf = pygame.transform.rotate(red_leaf, leaf[3])
        rotated_leaf.set_colorkey((247, 247, 247))

        screen.blit(rotated_leaf, (leaf[0], leaf[2]))

        if leaf[2] > (screen_height+200):
            leaves.remove(leaf)

    for leaf in leaves:
        leaf[2] += leaf[1]
        rotated_many_leaves = pygame.transform.rotate(many_leaves, leaf[3])
        rotated_many_leaves.set_colorkey((247, 247, 247))

        screen.blit(rotated_many_leaves, (leaf[0] + leaf[4], leaf[2] + leaf[4]))

        if leaf[2] > (screen_height+200):
            leaves.remove(leaf)

    pygame.display.update()
    clock.tick(60)
