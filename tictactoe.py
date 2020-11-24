import pygame

pygame.init()

win = pygame.display.set_mode((550, 550))

pygame.display.set_caption("Tic Tac Toe")

# draw the board
first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150))
second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(win, (255, 255, 255), (375, 25, 150, 150))

fourth = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150))
fifth = pygame.draw.rect(win, (255, 255, 255), (200, 200, 150, 150))
sixth = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))

seventh = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150))
eighth = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))
ninth = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if first.collidepoint(pos):
                pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))



    pygame.display.update()

pygame.quit()