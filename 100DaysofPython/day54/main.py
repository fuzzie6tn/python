# Flask
from flask import Flask
import random

app = Flask(__name__)
print(random.__name__)
print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello world</h1>'\
            '<p>this is a pargraph</p>'\
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGowdnFpdjZ3ODdoa2QwNGwzYWJ2ZjBiM3kxaTZia2k4dGVrenlkbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OmK8lulOMQ9XO/giphy.gif">'

@app.route('/bye')
def bye():
    return "bye"

@app.route('/username/<name>/<int:number>')
def username(name, number):
    # return f"Hello {name}, you are {number} years old!"
    pass

if __name__ == "__main__":
    app.run(debug=True)


# python decorator function
#
# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
