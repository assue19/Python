class Triangle:
  base = 0
  height = 0 base = 0
  height = 0
  hypotenus= 0
  def __init__(self, base, height,hypotenus):
    self.base = base
    self.height = height
    self.hypotenus = hypotenus
    
  def area(self):
      return 0.5*(self.base * self.height)
      
  def perimeter(self):
      return (self.base + self.height+ self.hypotenus)
        
small = Triangle(5,8,4)
large =Triangle(3000,4000,5000)
print("base and height of smaller  {}".format(small.base, small.height))
print("smaller area",small.area())
print("larger area",large. area())

small = Triangle (2,3,5)
large = Triangle ( 5000, 7000, 8000)
print ("base and height of smaller {}".format(small.base,small.height))
print ("smaller perimeter", small.perimeter())
print ( "larger perimeter", large.perimeter())





