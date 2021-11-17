from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask import send_file, current_app as app
from gramatica import parse
from singlenton import global_utils, Error
import json
from json import JSONEncoder
import AST as AST
import graphviz
import os

EntornoGlobal = None
ArbolAnterior = None
app = Flask(__name__)

@app.route("/")# de esta forma le indicamos la ruta para acceder a esta pagina. 'Decoramos' la funcion. 
def home():
    return render_template('index.html')

@app.route("/analyze", methods=["POST","GET"])
def analyze():
    global EntornoGlobal
    global ArbolAnterior
    if request.method == "POST":                         
        global_utils.iniciar()
        inpt = request.form["inpt"] 
        raiz = parse(inpt)          
        if raiz is not None:
            ArbolAnterior = raiz
            entornoGlobal  = AST.Entorno(None)
            EntornoGlobal = entornoGlobal            
            raiz.ejecutar(entornoGlobal)            
            if len(global_utils._errors)>0:
                return jsonify(output=completarPrograma(AST), errores=True)
            else:
                return jsonify(output=completarPrograma(AST), errores=False)
        else:        
            salida = []
            salida.append('')
            if len(global_utils._errors)>0:
                return jsonify(output=salida, errores= True)
            else:
                return jsonify(output=salida, errores= False)
    else:
        path= os.getcwd() +"/test/main.jolc"
        archivo = open(path, 'r')
        codigo = archivo.read()
        return render_template('analyze.html', initial=codigo)

def completarPrograma(AST):
    pass    
    consola = []    
    consola.append('package main')        
    consola.append('import ( "fmt" )')
    consola.append('')
    consola.append('var stack [1000]float64 // Stack')        
    consola.append('var heap [1000]float64 // Heap')
    consola.append('var P, H float64  // declaración de Stack y heap pointer')     
    numeroTemporales = global_utils.obtenerNumeroTemporales()
    numeroEtiquetas = global_utils.obtenerNumeroEtiquetas()
    cadenaTemporales = 'var t0'
    for x in range(numeroTemporales):
        if x > 0:                    
            cadenaTemporales += ', t'+ str(x)
    cadenaTemporales += ' float64// Temporales'
    consola.append(cadenaTemporales)    
    consola = consola + AST.consola          
    return consola   


@app.route("/reports", methods=["POST", "GET"])
def reports():
    if request.method == "POST":
        inpt = request.form["valor"]
    else:
        return render_template('reports.html')

@app.route("/errors" , methods=["POST"])
def errors():
    global EntornoGlobal
    global ArbolAnterior
    if request.method == "POST":
        errores = []
        for err in global_utils._errors:
            errores.append(json.loads(err.toJSON()))    
        simbolos = []
        indice = 0
        for simb in EntornoGlobal.tabla.tabla: 
            var = EntornoGlobal.tabla.tabla.get(simb)           
            simbolos.append({"index": indice, "nombre": var.id, "tipo": var.tipo.getNombre(), "rol" : var.getRol(), "ambito": "Global", "linea": var.linea, "columna": var.columna  })
            indice += 1               
        return jsonify(errors=errores,tabla = simbolos)


@app.route("/descargar" , methods=["POST"])
def descargar():
    global EntornoGlobal
    global ArbolAnterior
    if request.method == "POST":
        u = graphviz.Digraph(filename='rank_same.gv')
        if ArbolAnterior is not None:
            ArbolAnterior.graficar('Raiz',u)                
            u.render('static/ast.gv', view=False)
        path= os.getcwd() +"/static/ast.gv.pdf"        
        return redirect("/static/ast.gv.pdf")

@app.route('/output/')
def output(inpt):
    inpt=inpt.replace("aa11a223","/")
    result = parse(inpt)
    return render_template('output.html', input=result)

if __name__ == "__main__":    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)#para que se actualice al detectar cambios