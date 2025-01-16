from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3)/3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "DESAPROBADO"

        return render_template('ejercicio1.html', estado=estado, promedio=promedio)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            resultado = nombre1
            cant = len(nombre1)
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            resultado = nombre2
            cant = len(nombre2)
        else:
            resultado = nombre3
            cant = len(nombre3)

        return render_template('ejercicio2.html', resultado=resultado, cant=cant)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)