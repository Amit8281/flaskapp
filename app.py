from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")#Decorator
def hello_world():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello_world1")#Decorator
def hello_world1():
    return "<h1>Hello, World2!</h1>"

@app.route("/hello_world2")#Decorator
def hello_world2():
    return "<h1>Hello, World3!</h1>"

@app.route("/test")
def test():
    return "this is my function to run app"
    
@app.route("/test2")
def test2():
    data= request.args.get('x')
    return "this is a data input from my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
