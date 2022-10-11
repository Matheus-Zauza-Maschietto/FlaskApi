from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/educative")
def learn():
    return "Happy Learning at Educative!"


@app.route('/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of " + str(number) + " is: " + str(number * number) 


if __name__ == '__main__':
    app.run(debug=True)
