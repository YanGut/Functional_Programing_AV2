from q1_YanMendonca import *
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template_folder')

user = lambda: {
    "name": "Medeiros",
    "password": "654321",
}

users = user()

welcome = lambda: f'WELCOME {request.form["username"]}!{cashCurrign("Medeiros", "654321", 100)}'
wrong = lambda: 'Senha errada! ' + print_crypt_info()
invalid = lambda: 'Usuário não cadastrado! '
print_crypt_info = lambda: f'\n Apenas para verificação\nSenha inserida: {request.form["password"]}, Senha no banco: {users.get(request.form["username"])}\n '
password_matches = lambda dic: dic.get(request.form["username"]) == request.form["password"]
check_password = lambda: welcome() if password_matches(users) else wrong()
check_if_user_exists = lambda: check_password() if request.form["username"] in users else invalid()
reqresp = lambda: check_if_user_exists() if request.method == 'POST' else render_template('index.html')

app.add_url_rule("/index/", "index", reqresp, methods=["GET", "POST"])
app.run(host="0.0.0.0" ,port=5000)
