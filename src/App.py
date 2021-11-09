from flask import Flask, request , jsonify
from flask_cors import CORS
import gramatica as g
import tabla_simbolos as TS
import principal as P
import salida as sal

from Symbol.Environment import Environment
from Symbol.Generator import Generator

app = Flask(__name__)
CORS(app)


@app.route('/compilar', methods =['POST' , 'GET'])
def compilar():
    #CREAMOS EL PARSER
    '''instrucciones = g.parse(request.json["texto"])
    ts_global = TS.TablaDeSimbolos()
    ts_global.simbolos=[]
    ts_global.anterior = ""
    salida_consola = sal.Salida_Consola() 
    #MANDAMOS A LLAMAR PARA LEER EL ARCHIVO DE ENTRADA
    P.procesar_instrucciones(instrucciones, ts_global, salida_consola)
    
    return '{\"salida\":\"'+salida_consola.obtener()+'\"}'
    '''
    try:
        
        inpt = request.json['texto']

        genAux = Generator()
        genAux.cleanAll()
        generator = genAux.getInstance()

        newEnv = Environment(None)
        
        ast = g.parse(inpt)
        try:
            for instr in ast:
                instr.compile(newEnv)
        except:
            print("Error al compilar instrucciones")
        return ({"salida": generator.getCode()})
    except:
        print('Error')
        return { 'msg': 'ERROR', 'code': 500 }

if __name__ == "__main__":
    app.run(debug=True)




