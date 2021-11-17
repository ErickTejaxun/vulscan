import json
from json import JSONEncoder
from datetime import date
import datetime

# Errors 
_error_counter = 0
_file_ = ''
entornoGlobal = None
contadorTemporal = 0



class Error():
    def __init__(self, id, type, desc, line, column):
        global _error_counter
        global _file_
        self.index = _error_counter
        self.id = id
        self.type = type
        self.desc = desc
        self.line = line
        self.column = column
        self.file = _file_
        self.hora = str(datetime.datetime.now())
        _error_counter = _error_counter + 1 

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)        

class SinglentonMeta(type):
    _instances = {}    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singlenton(metaclass=SinglentonMeta):
    _errors = []
    fecha = date.today()
    contadorTemporales = 0
    contadorEtiquetas = 0
    etiquetasReutilizables = []
    temporalesReutilizables = []
    pila=[]
    metodoActual='main'
    etiquetaSalida=''

    def iniciar(self):
        global  _error_counter
        global  _file_   
        global contadorTemporal     
        _error_counter = 0                 
        contadorTemporal = 0
        self.contadorEtiquetas = 0
        self.contadorTemporales = 0

    def metodoActual(self):
        if len(self.pila)==0:
            return 'main'
        else:
            return self.pila[len(self.pila)-1]
    
    def apilarMetodo(self, metodo):
        self.pila.append(metodo)
    
    def desapilarMetodo(self):
        self.pila.pop()

    def establecerSalida(self, salida):
        self.etiquetaSalida=salida  

    def Salida(self): 
        return self.etiquetaSalida

    def generarTemporal(self):
        contador = self.contadorTemporales
        self.contadorTemporales += 1
        return 't'+str(contador)
    
    def generarEtiqueta(self):
        contador = self.contadorEtiquetas
        self.contadorEtiquetas += 1
        return 'L'+str(contador)
    
    def obtenerNumeroTemporales(self):
        return self.contadorTemporales
    
    def obtenerNumeroEtiquetas(self):
        return self.contadorEtiquetas
    
    def obtenerNulo(self):
        return 238932827;

    def registryError(self, id, desc, line, column):
        self._errors.append(Error(id, type, desc, line, column))

    def registryLexicalError(self, id, desc, line, column):
        self._errors.append(Error(id, 'Léxico', desc, line, column))
    
    def registrySyntaxError(self,id, desc, line, column):
        self._errors.append(Error(id, 'Sintáctico', desc, line, column))

    def registrySemanticError(self,id, desc, line, column):
        self._errors.append(Error(id, 'Semántico', desc, line, column))


class ErrorEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class SinglentonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__    

global_utils = Singlenton()