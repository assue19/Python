class Taxpayer:
  income = 0
  name = "Jane Doe"
  def __init__(self,name,income):
   self.income = income
   self.name = name
   self.validateIncome()
   self.validateName()
  
  def validateIncome(self):
    if self.income.isnumeric() == False:
   
      raise ValueError("The income {} is not numeric" . format(self.income))
      
      def Validateminimum(self)
      if float(self income)< 10000:
        raise ValueError("Below wage")
      
  def validateName(self):
   if self.name.isnumeric():
     raise ValueError("The name {} is not a string" .format(self.name))
      
  def calculate_tax(self):
    return float(self.income)* 0.3
    
income = input("What is your income:")
name = input("What is your name")
employee = Taxpayer( name,income)
print(employee.calculate_tax())