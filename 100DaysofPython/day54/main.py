# Flask
from flask import Flask
import random

app = Flask(__name__)
print(random.__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

if __name__ == "__main__":
    app.run()


# python decorator function
#
# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
