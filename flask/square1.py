from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def index(name = "student"):
  name = request.args.get('name',name)
  return "welcome {} ".format(name)
@app.route('/home')
def home():
  return "welcome student"

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0', port=8080)