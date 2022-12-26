#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/calculaedad', methods = ['GET', 'POST'])
def calcula_edad():
    anyo = request.form.get('anyo')
    edad_aproximada = devuelve_anyo_actual() - int(anyo)
    return render_template('edad.html', edad_aproximada = edad_aproximada)

def devuelve_anyo_actual():
    fecha_actual = datetime.datetime.now()
    return int(fecha_actual.year)

if __name__ == '__main__':
    app.run()



    

