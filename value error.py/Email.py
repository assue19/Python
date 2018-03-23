class Student:
  
  def __init__(self, names, email):
    self.names = names
    self.email = email
    self.validateEmail()
    self.validateName()
  
  def validateEmail(self):
    pass
  
  def validateName(self):
    if type(self.names) is not str:
      raise ValueError("{} is not a valid name".format(self.email))
      
jane = Student("Jane","jane")
print(jane.email)
