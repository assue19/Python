from flask import Flask
app = Flask(__name__)
@app.route("/")
def index(name= "student"):
  return "welcome {} to Akirachix".format(name)

@app.route("/welcome/<name>")
def welcome(name= "student"):
  return "welcome {} to Akirachix".format(name)
@app.route("/add/<int:num1>/<int:num2>")
@app.route("/add/<float:num1>/<float:num2>")
@app.route("/add/<float:num1>/<int:num2>")
@app.route("/add/<int:num1>/<float:num2>")
def add(num1 =0,num2=0):
  sum = num1 + num2
  return " sum of {} and {} is {}".format(num1,num2,sum)
  
if __name__ == '__main__':
  app.run(host = '0.0.0.0',port=8080