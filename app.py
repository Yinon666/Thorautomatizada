from flask import Flask
from flask import render_template, jsonify
import csv

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')

@app.route('/nosotros')
def nosotros():
    data = []
    with open("data.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append({"hebrew": row["palabra"], "translation": row["traduccion"]})
    return render_template("sitio/nosotros.html", data=data)

@app.route('/manejar_clic', methods=['POST'])
def manejar_click():
    # Puedes realizar cualquier lógica necesaria aquí
    # En este ejemplo, simplemente devolvemos un mensaje
  
    return ( 'Hola desde el servidor Flask!')

if __name__ =='__main__':
    app.run(debug=True, port=5001)
    

    

    