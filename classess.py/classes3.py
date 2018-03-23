class Student :
  name = "John Doe"
  def __init__(self,name):
    self.name = name
    
  def get_name(self):
     return self.name
      
      
  def welcome(self):
    return "Welcome {} to Akirachix".format(self.name)
        
fatma = Student("fatma moha")
judith = Student("judith mueni")
print (fatma.welcome())
print (judith.welcome())