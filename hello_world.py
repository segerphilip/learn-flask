from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/test")
def test():
  return "Wow, you've visited this page {} times!"

if __name__ == '__main__':
  app.run()