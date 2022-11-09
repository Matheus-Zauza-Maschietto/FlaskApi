"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template, abort
from forms import SigupForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")


@app.route("/details/<int:id>")
def details(id):
    """View function for details pets page"""
    try:
        pets[id]
    except:
        abort(404, description="Doesn't exists a pet with this id")
    else:
        return render_template("details.html", pet=pets[id])


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form = SigupForm()
    if form.validate_on_submit():
        return render_template("login.html", message="Successfully Logged In")
    return render_template("signup.html", form=form, message='Invalid signup')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
