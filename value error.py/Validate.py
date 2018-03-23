class Rectangle :
  length = 0
  width = 0
  def __init__(self , length, width):
    self.length = length
    self.width = width
  
  def area (self):
    return self.length * self.width
    
    def perimeter(self):
      return 2 *(self.length + self.width)
      
small = Rectangle(2,3)
invalid = Rectangle("fixe", 5)
print(invalid.area())