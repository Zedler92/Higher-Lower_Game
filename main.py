from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper

def make_emphasized(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper

def make_underline(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper

@app.route('/')

def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>This is my paragraph</p>' \
           '<img src="https://media4.giphy.com/media/5tsjxsQXLl4GcNsd5S/giphy.gif?cid' \
           '=790b761129aa86e469edcef49e48e350bacba937885f4a2b&rid=giphy.gif&ct=g" width="400px"> '


@app.route('/bye')
@make_bold
@make_underline
@make_emphasized
def bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greetings(name, number):
    return f"Hello there {name}, and you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
