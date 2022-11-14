"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template, abort, request, url_for, redirect
from forms import SigupForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

users = [
            {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.co", "password": "adminpass"},
            {"id": 2, "full_name": "Matheus Zauza maschietto", "email": " matheus_maschietto@yahoo.com.br", "password": "12345 "}
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
    if request.method == 'POST':
        if form.is_submitted():
            if form.validate():
                users.append({"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data})
                return render_template("successful.html", message="Successfully Signup In")
            return render_template("signup.html", form=form,)
        return render_template("signup.html", form=form, message="No field can be blank")
    return render_template("signup.html", form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    print(request.method)
    if request.method == 'POST':
        if form.is_submitted():
            if form.validate():
                for user in users:
                    if form.email.data in user and form.password.data in user:
                        
                        return render_template('login.html', form=form, message="Successfully logged")
                return render_template('login.html', form=form, message="No user found")
            return render_template('login.html', form=form)
        return render_template('login.html', form=form, message="No field can be blank")
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
