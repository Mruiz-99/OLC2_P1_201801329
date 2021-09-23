from flask import Flask, request , jsonify
from flask_cors import CORS
import gramatica as g
import tabla_simbolos as TS
import principal as P
import salida as sal

app = Flask(__name__)
CORS(app)


@app.route('/compilar', methods =['POST' , 'GET'])
def compilar():
    #CREAMOS EL PARSER
    instrucciones = g.parse(request.json["texto"])
    ts_global = TS.TablaDeSimbolos()
    ts_global.simbolos=[]
    ts_global.anterior = ""
    salida_consola = sal.Salida_Consola() 
    #MANDAMOS A LLAMAR PARA LEER EL ARCHIVO DE ENTRADA
    P.procesar_instrucciones(instrucciones, ts_global, salida_consola)
    return '{\"salida\":\"'+salida_consola.obtener()+'\"}'


if __name__ == "__main__":
    app.run(debug=True)




