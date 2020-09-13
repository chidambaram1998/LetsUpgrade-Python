import math

class cone():
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height

  def volume(self):
    v = (math.pi)*pow(self.radius,2)*(self.height/3)
    return ("Volume: %.2f"%v)

  def area(self):
    a = (math.pi)*self.radius*(self.radius+math.sqrt((pow(self.radius,2)+pow(self.height,2))))
    return ("Surface Area: %.2f"%a)

vol = cone(5,2)
vol.volume()
vol.area()