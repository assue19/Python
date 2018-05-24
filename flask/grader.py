from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/grader')
def grader(mark = "0"):
  mark = int(request.args.get('mark',mark))
  total_marks = int(mark)
  if mark > 71:
    return 'A'
  elif mark > 61:
    return 'B'
  elif mark > 51:
    return 'C'
  else:
    return 'D'
  return "for marks {} the grade is{}".format(mark,total_marks)
if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0', port=8080)