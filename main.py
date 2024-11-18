import pygame, sys
from game import Game
from colors import Colors
# from grid import Grid
# from blocks import *

pygame.init()

title_font = pygame.font.Font(None, 65)
score_surface = title_font.render("score", True, Colors.white)
next_surface = title_font.render("next", True, Colors.white)
game_over_surfae = title_font.render("Game Over", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

#создать окно размером 1000 на 800
screen = pygame.display.set_mode((600, 720))
# название нового окна
pygame.display.set_caption("Tetris")

# контроль частота кадров и как хорошо "быстро будет работать игра"
clock = pygame.time.Clock()

game = Game()

#    # добавить объект класса Grid
#    game_grid = Grid()
#
#    # создать объект класса Lblock
#    block = Oblock()

#обекты тест
#game_grid.grid[0][0] = 1
#game_grid.grid[3][5] = 4
#game_grid.grid[14][5] = 7
#game_grid.print_grid()

#Всего 3 цикла
#1 любые действия или события в игре "Event Handling"

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)
#поскольку эта бесконечная игра нам нужен цикл while так как при True он будет работать до бесконечности но после смети будет "Break" или "While False" чтобы прекратить "страдания играка"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    score_value_surface = title_font.render(str(game.scored), True, Colors.white)
    
    screen.fill(Colors.dark_Green)
    #поле с инфой
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surfae, (320, 450, 50, 50))

    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 11)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 12)
    #    game_grid.draw(screen)
    #    block.draw(screen)
    game.draw(screen)

    pygame.display.update()
    #fps цикл будет повторятся 60 раз в секунду "ГРУБО говоря"
    clock.tick(60)
#2 Updating Positions обновление всех обьектов в игре на осонве событий из 1 цикла.... 20 на 10 сверху вниз и слева направо

#3 Drawing objects нарисовать все обьекты и их положения
