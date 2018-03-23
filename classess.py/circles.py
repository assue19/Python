class circle:
  radius = 0
  diameter = 0
 
  def __init__(self,radius,diameter):
    self.radius = radius
    self.diameter = diameter
    
  def area(self):
    return 3.142*(self.radius * self.radius)
      
  def perimeter(self):
    return 2* 3.142 * self.radius
        
small = circle(14,28)
large = circle(28,56)
print("radius and diameter of smaller  {} and {}.".format(small.radius, small.diameter))
print ("smaller area",small.area())
print ("larger area",large. area())

small =circle(14,28)
large = circle ( 5000, 7000)
print ("radius and diameter of smaller {}.".format(small.radius,small.diameter))
print ("smaller perimeter", small.perimeter())
print ( "larger perimeter", large.perimeter())





