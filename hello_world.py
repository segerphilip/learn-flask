from flask import Flask
from flask import Markup
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello world! Possible pages include: Markup('<a>http://localhost:5000/test</a>')"

@app.route("/test")
def test():
  return "Wow, you've visited this page {} times!".format('TEST')

if __name__ == '__main__':
  app.run(debug = True)