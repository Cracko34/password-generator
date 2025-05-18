from flask import Flask, render_template, request, send_file
import random
import string
import io

app = Flask(__name__)

def generar_contraseña(longitud, usar_numeros, usar_simbolos):
    caracteres = list(string.ascii_letters)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_simbolos:
        caracteres += list("!@#$%^&*()_+-=[]{};:,.<>?")
    return ''.join(random.choice(caracteres) for _ in range(longitud))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        longitud = int(request.form['length'])
        usar_numeros = 'include_numbers' in request.form
        usar_simbolos = 'include_symbols' in request.form
        contraseña = generar_contraseña(longitud, usar_numeros, usar_simbolos)
        return render_template('result.html', password=contraseña)
    return render_template('index.html')

@app.route('/descargar/<password>')
def descargar(password):
    contenido = f'your password is: {password}'
    archivo = io.BytesIO()
    archivo.write(contenido.encode('utf-8'))
    archivo.seek(0)
    return send_file(
        archivo,
        as_attachment=True,
        download_name='your_password.txt',
        mimetype='text/plain'
    )

if __name__ == '__main__':
    app.run(debug=True)
