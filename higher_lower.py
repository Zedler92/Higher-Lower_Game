from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)
print(random_number)
@app.route('/')
def text():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"

@app.route('/<number>/')
def higher_lower(number):
    if int(number) == random_number:
        return "<h1>You are right!</h1>" \
               "<img src='https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp'>"
    elif int(number) < random_number:
        return "<h1>Too low! try again!</h1>" \
               "<img src='https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp'>"
    else:
        return "<h1>Too High! try again!</h1>" \
               "<img src='https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp'>"




if __name__ == "__main__":
    app.run(debug=True)