from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_contraseña(longitud, usar_numeros, usar_simbolos):
    caracteres = list(string.ascii_letters)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_simbolos:
        caracteres += list("!@#$%^&*()_+-=[]{};:,.<>?")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        longitud = int(request.form['length'])
        usar_numeros = 'include_numbers' in request.form
        usar_simbolos = 'include_symbols' in request.form

        contraseña = generar_contraseña(longitud, usar_numeros, usar_simbolos)
        return render_template('result.html', password=contraseña)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
