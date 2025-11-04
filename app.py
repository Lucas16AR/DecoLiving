from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/comentario', methods=['POST'])
def comentario():
    nombre = request.form.get('nombre')
    mensaje = request.form.get('mensaje')
    return render_template('index.html', nombre=nombre, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)