from flask import Flask

app = Flask(__name__)


@app.route('/')
def homePage():
    return "Paws Rescue Center 🐾"


@app.route('/about')
def aboutPage():
    return "We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology 'adopt, don't hop'! "


if __name__ == '__main__':
    app.run()

