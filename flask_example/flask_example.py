from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/<username>') # переменные задаются через <>
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<post_id>') # отдельно можем задать ограничение на тип (например, здесь указываем int)
def show_post(post_id):
    return 'Post %s' % post_id


@app.route('/login', methods=['GET', 'POST']) #указываем методы, которые обрабатываем
def login():
    if request.method == 'POST': # если метод POST, то сделай одно
        do_the_login()
        return "POST"
    else:
        show_the_login_form() # иначе другое (GET)
        return "GET"

@app.route('/hello/')
def hello(name=None):
    return render_template('PPP.html', name=name)

@app.route('/start')
def index():
    return redirect(url_for('hello')) #сделай редирект на страницу с login

@app.route('/log')
def log():
    abort(401) # Выдай ошибку 401   
     


if __name__ == '__main__':
    app.run(debug=True)

# прокидываем туннель в интернет https://my.tuna.am/
