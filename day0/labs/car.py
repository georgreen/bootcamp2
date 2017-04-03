class Car(object):
  def __init__(self, name = 'General', model = 'GM',Type = ''):
    self.name = name
    self.model = model
    self.speed = 0
    self.Type = Type
    self.num_of_doors = 4
    self.set_door(name)

    self.num_of_wheels = 4
    self.set_wheels(Type)

    return

  def set_door(self, name):
    if name == 'Porshe' or name == 'Koenigsegg':
      self.num_of_doors = 2

  def set_wheels(self, Type):
    if Type == 'trailer':
        self.num_of_wheels = 8


  def drive(self,speed):
    if speed == 7 and self.Type == 'trailer':
      self.speed = 77
    elif speed == 3 and self.name == 'Mercedes':
      self.speed = 1000
    return self

  def set_speed(self, n):
    self.speed = n


  def is_saloon(self):
    if self.Type== 'trailer':
      return False
    return True
