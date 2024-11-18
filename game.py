from blocks import *
from grid import Grid
import random


class Game:

  def __init__(self):
    self.grid = Grid()
    self.blocks = [
        Iblock(),
        Jblock(),
        Lblock(),
        Oblock(),
        Sblock(),
        Tblock(),
        Zblock()
    ]
    self.current_block = self.get_random_block()
    self.next_block = self.get_random_block()
    self.game_over = False
    self.scored = 0

  #счёт 1 ряд 100 2 ряда 300 3 ряд 500 и движение фигуры ползователем 1 очко
  def update_score(self, lines_clearned, move_down_points):
    if lines_clearned == 1:
      self.scored += 100
    elif lines_clearned == 2:
      self.scored += 300
    elif lines_clearned == 3:
      self.scored += 500
    elif lines_clearned == 4:
      self.scored += 1000
    self.scored += move_down_points

  def get_random_block(self):
    if (len(self.blocks) == 0):
      self.blocks = [
          Iblock(),
          Jblock(),
          Lblock(),
          Oblock(),
          Sblock(),
          Tblock(),
          Zblock()
      ]
    block = random.choice(self.blocks)
    self.blocks.remove(block)
    return block

# движение по кнопкам функиция для того чтобы обозначить что стрелка в низ это ускорение в низ

  def move_left(self):
    self.current_block.move(0, -1)
    if self.block_inside() == False or self.block_fits() == False:
      self.current_block.move(0, 1)

#Сверху это движение лево

  def move_right(self):
    self.current_block.move(0, 1)
    if self.block_inside() == False or self.block_fits() == False:
      self.current_block.move(0, -1)

  #Сверху это движение право

  def move_down(self):
    self.current_block.move(1, 0)
    if self.block_inside() == False or self.block_fits() == False:
      self.current_block.move(-1, 0)
      self.lock_block()

  #Сверху это ускорение вниз

  def lock_block(self):
    tiles = self.current_block.get_cell_position()
    for position in tiles:
      self.grid.grid[position.row][position.column] = self.current_block.id
    self.current_block = self.next_block
    self.next_block = self.get_random_block()
    rows_cleared = self.grid.clear_full_rows()
    self.update_score(rows_cleared, 0)
    if self.block_fits() == False:
      self.game_over = True

# ресет игры после проигроша он разделен на 2 части 2 часть сама функиция в Грид

  def reset(self):
    self.grid.reset()
    self.blocks = [
        Iblock(), Jblock(), Lblock(), Oblock(), Sblock(), Tblock(), Zblock()]
    self.current_block = self.get_random_block()
    self.next_block = self.get_random_block()
    self.score = 0

#Сверху это блоки которые будут складываться и не будут проходить сквозьдруг друга

  def block_fits(self):
    tiles = self.current_block.get_cell_position()
    for tile in tiles:
      if self.grid.is_empty(tile.row, tile.column) == False:
        return False
    return True

#поворачивать функция

  def rotate(self):
    self.current_block.rotate()
    if self.block_inside() == False or self.block_fits() == False:
      self.current_block.undo_rotation()


#блок внутри

  def block_inside(self):
    tiles = self.current_block.get_cell_position()
    for tile in tiles:
      if self.grid.is_inside(tile.row, tile.column) == False:
        return False
    return True

  def draw(self, screen):
    self.grid.draw(screen)
    self.current_block.draw(screen, 11, 11)

    if self.next_block.id == 3:
      self.next_block.draw(screen, 255, 290)
    elif self.next_block.id == 4:
      self.next_block.draw(screen, 255, 280)
    else:
      self.next_block.draw(screen, 270, 270)