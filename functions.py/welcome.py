def welcome_student(name):
  welcome_str = "Hi {} welcome to AKIrachix"
  return welcome_str.format(name)
name =input("Enter the student name:")
print(welcome_student(name))
print(welcome_student("Esther"))
print(welcome_student("Assue"))