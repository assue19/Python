class Student :
  name = "John Doe"
  weekday = True
    
  def __init__(self,name,weekday):
    self.name = name
    self.weekday = weekday
      
  def morning(self):
    if self. weekday :
      return "wake up"
    else :
     return "sleeps"
fatma = Student("fatma moha", True)
judith = Student( name="judith mueni",weekday=False)
print ("fatma:",fatma.morning())
print ("judith:",judith.morning())