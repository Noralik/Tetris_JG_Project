class Colors:
  # функция для выдачи картреджей цветов "для обьектов" которые будут спускаться вниз
  red = (255, 255, 255)
  orange = (255, 127, 0)
  yellow = (255, 255, 0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  purple = (127, 0, 255)
  pink = (255, 0, 255)
  lol = (125, 0, 125)

  #чвет фоона
  white = (255, 255, 255)
  dark_Green = (44, 44, 127)
  light_blue = (59, 85, 162)
  
#@classmethod - это декоратор, который позволяет добавить метод к классу без необходимости создавать экземпляр этого класса.
  @classmethod
#cls - это соглашение об именовании переменной, которое обозначает класс, для которого определён данный метод
  def get_cell_colors(cls):
    return [cls.red, cls.orange, cls.yellow, cls.green, cls.blue, cls.purple, cls.pink, cls.lol]