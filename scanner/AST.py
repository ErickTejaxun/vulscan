'''
Erick Tejaxún
erickteja@gmail.com 
Compiladores 2
USAC 2021
'''

from abc import ABC, abstractmethod
from enum import Enum
from json import JSONEncoder
import json
from singlenton import global_utils
import math


consola = []

def esExpresionBasica(exp):
    return isinstance(exp,(Suma, Resta, Multiplicacion, Division, Potencia, Modulo, Variable, Entero, Float, Bool, Char))

def esRelacional(exp):
    return isinstance(exp, (Mayor, MayorIgual, Menor, MenorIgual, Igualigual, Diferente))

def agregarFuncionesNativas():
    global consola 
    nativaImpresion(consola)    
    nativaImpresionln(consola)
    nativaConcatenacion(consola)
    nativaIntToString(consola)
    nativaFloatToString(consola)
    nativaPotencia(consola)
    nativaCompararCadenas(consola)
    nativaUpperCase(consola)
    nativaLowerCase(consola)
    nativaBoolToString(consola)


def nativaBoolToString(consol):
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()

    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()    
    consola.append('func BoolToString_Nativa(){') 
    consola.append(t0+'=P+1;// Obtener direccion valor')
    consola.append(t1+'=stack[int('+t0+')];// valor ')
    consola.append('if('+t1+'==1){goto '+L1+';}//Verdadero')
    consola.append('goto '+L2+';//Falso')

    consola.append(L1+':')
    valor="true"
    t0 = global_utils.generarTemporal()                   
    t1 = global_utils.generarTemporal() 
    consola.append(t0+'=H;')
    consola.append(t1+'='+t0+';')
    consola.append('H=H+'+str(len(valor)+1)+';')
    for car in str(valor):
        consola.append('heap[int('+t1+')]='+ str(ord(car))+';//' + car)
        consola.append(t1+'='+t1+'+1;')
    consola.append('heap[int('+t1+')]='+str(global_utils.obtenerNulo())+';// Fin cadena')
    consola.append(t3+'='+t0+';// valor ')

    consola.append('goto '+L3+';')
    consola.append(L2+':')
    valor="false"
    t0 = global_utils.generarTemporal()                   
    t1 = global_utils.generarTemporal() 
    consola.append(t0+'=H;')
    consola.append(t1+'='+t0+';')
    consola.append('H=H+'+str(len(valor)+1)+';')
    for car in str(valor):
        consola.append('heap[int('+t1+')]='+ str(ord(car))+';//' + car)
        consola.append(t1+'='+t1+'+1;')
    consola.append('heap[int('+t1+')]='+str(global_utils.obtenerNulo())+';// Fin cadena')
    consola.append(t3+'='+t0+';// valor ')
    consola.append(t3+'='+t0+';// valor ')
    consola.append(L3+':')
    consola.append('}')
    consola.append(' ')     


def nativaLowerCase(consola):

    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()

    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()
    L5 = global_utils.generarEtiqueta()
    L6 = global_utils.generarEtiqueta()


    consola.append('func lowercase_Nativa(){') 
    consola.append(t0+'=P+1;// Direccion parametro 1')
    consola.append(t1+'=stack[int('+t0+')];// Obtener inicio cadena')
    consola.append(t2+'=H;//Inicio de la nueva cadena')    
    consola.append(L1+':')
    consola.append(t3+'=heap[int('+t1+')];// caracter actual')
    consola.append('if('+t3+'=='+str(global_utils.obtenerNulo())+'){ goto '+L2+';} // fin de la cadena;')
    consola.append('goto '+L3+'; // Traslado de caracter')
    consola.append(L3+': // Traslado de caracter')
    consola.append('if('+t3+'>=65){goto '+L4+';}//Ir a segunda verificacion')
    consola.append('goto '+L5+';//Almacenar el caracter')
    consola.append(L4+':')
    consola.append('if('+t3+'<=90){goto '+L6+';}// Hay que pasarlo mayúscula')
    consola.append('goto '+L5+';//Almacenar el caracter')
    consola.append(L6+':')
    consola.append(t3+'='+t3+'+32;//Pasando a mayúscula')
    #consola.append('goto '+L4+';//Almacenar el caracter')
    consola.append(L5+':')
    consola.append(t4+'=H;//Direccion cadena')
    consola.append('H=H+1;//Reservando espacio')
    consola.append('heap[int('+t4+')]='+t3+';')
    consola.append(t1+'='+t1+'+1;')
    consola.append('goto '+L1+';')
    consola.append(L2+':')
    consola.append(t5+'=H;')
    consola.append('H=H+1;//Reservando espacio')
    consola.append('heap[int('+t5+')]='+str(global_utils.obtenerNulo())+';')
    consola.append('stack[int(P)]='+t2+';//Set retorno')
    consola.append('}')
    consola.append(' ')       

def nativaUpperCase(consola):

    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()

    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()
    L5 = global_utils.generarEtiqueta()
    L6 = global_utils.generarEtiqueta()


    consola.append('func uppercase_Nativa(){') 
    consola.append(t0+'=P+1;// Direccion parametro 1')
    consola.append(t1+'=stack[int('+t0+')];// Obtener inicio cadena')
    consola.append(t2+'=H;//Inicio de la nueva cadena')    
    consola.append(L1+':')
    consola.append(t3+'=heap[int('+t1+')];// caracter actual')
    consola.append('if('+t3+'=='+str(global_utils.obtenerNulo())+'){ goto '+L2+';} // fin de la cadena;')
    consola.append('goto '+L3+'; // Traslado de caracter')
    consola.append(L3+': // Traslado de caracter')
    consola.append('if('+t3+'>=97){goto '+L4+';}//Ir a segunda verificacion')
    consola.append('goto '+L5+';//Almacenar el caracter')
    consola.append(L4+':')
    consola.append('if('+t3+'<=122){goto '+L6+';}// Hay que pasarlo mayúscula')
    consola.append('goto '+L5+';//Almacenar el caracter')
    consola.append(L6+':')
    consola.append(t3+'='+t3+'-32;//Pasando a mayúscula')
    #consola.append('goto '+L4+';//Almacenar el caracter')
    consola.append(L5+':')
    consola.append(t4+'=H;//Direccion cadena')
    consola.append('H=H+1;//Reservando espacio')
    consola.append('heap[int('+t4+')]='+t3+';')
    consola.append(t1+'='+t1+'+1;')
    consola.append('goto '+L1+';')
    consola.append(L2+':')
    consola.append(t5+'=H;')
    consola.append('H=H+1;//Reservando espacio')
    consola.append('heap[int('+t5+')]='+str(global_utils.obtenerNulo())+';')
    consola.append('stack[int(P)]='+t2+';//Set retorno')
    consola.append('}')
    consola.append(' ')    


def nativaCompararCadenas(consola):
    '''
    t0=P+1;// Direccion parametro 1
    t1=stack[int(t0)];//Direccion cadena 1
    t2=P+2;// Direccion parametro 2
    t3=stack[int(t2)];// Direccion cadena 2
    L1:
    t6=heap[t1]; // Caracter actual
    if(t4!=finCadena){ goto L2;}
    goto L3;
    L3:
    t7=heap[t3];
    if(t7==finCadena){goto L4;}// Retornar verdadero
    goto L5;
    L2:// Comparar cadenas
    t8=heap[t1]; // Caracter i-esimo cadena 1
    t9=heap[t3]; // Caracter i-esimo cadena 2
    if(t8==t9){goto L6;}// Aumentar contadores
    goto L7; Retornar falseo
    L6:
    t1=t1+1;
    t3=t3+1;
    goto L1;
    L3:
    t8=heap[t1]; // Caracter i-esimo cadena 1
    t9=heap[t3]; // Caracter i-esimo cadena 2
    if(t8==t9){goto L8;}// Aumentar contadores 
    goto L7; Retornar falseo   
    L8:
    t10=P+0;//Direccion de retorno
    stack[int(t10)]=1;// Devolvermos verdedaero
    L5:
    L7:
    '''  
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()
    t6 = global_utils.generarTemporal()
    t7 = global_utils.generarTemporal()
    t8 = global_utils.generarTemporal()
    t9 = global_utils.generarTemporal()
    t10 = global_utils.generarTemporal()

    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()
    L5 = global_utils.generarEtiqueta()
    L6 = global_utils.generarEtiqueta()
    L7 = global_utils.generarEtiqueta()
    L8 = global_utils.generarEtiqueta()   
    
    consola.append('func ComparacionCadenas_nativa(){') 
    consola.append(t0+'=P+1;// Direccion parametro 1')
    consola.append(t1+'=stack[int('+t0+')];//Direccion cadena 1')
    consola.append(t2+'=P+2;// Direccion parametro 2')
    consola.append(t3+'=stack[int('+t2+')];// Direccion cadena 2')
    consola.append(L1+':')
    consola.append(t6+'=heap[int('+t1+')]; // Caracter actual')
    consola.append('if('+t6+'== '+str(global_utils.obtenerNulo())+'){ goto '+L3+';}')
    consola.append('goto '+L2+';')
    consola.append(L3+':')
    consola.append(t7+'=heap[int('+t3+')];')
    consola.append('if('+t7+'=='+str(global_utils.obtenerNulo())+'){goto '+L4+';}// Retornar verdadero')
    consola.append('goto '+L5+';')
    consola.append(L2+':// Comparar cadenas')
    consola.append(t8+'=heap[int('+t1+')]; // Caracter i-esimo cadena 1')
    consola.append(t9+'=heap[int('+t3+')]; // Caracter i-esimo cadena 2')
    consola.append('if('+t8+'=='+t9+'){goto '+L6+';}// Aumentar contadores')
    consola.append('goto '+L7+'; //Retornar falso')
    consola.append(L6+':')
    consola.append(t1+'='+t1+'+1;')
    consola.append(t3+'='+t3+'+1;')
    consola.append('goto '+L1+';')
    consola.append(L4+':')
    consola.append(t8+'=heap[int('+t1+')]; // Caracter i-esimo cadena 1')
    consola.append(t9+'=heap[int('+t3+')]; // Caracter i-esimo cadena 2')
    consola.append('if('+t8+'=='+t9+'){goto '+L8+';}// Aumentar contadores ')
    consola.append('goto '+L7+'; //Retornar falseo')
    consola.append(L8+':')
    consola.append(t10+'=P+0;//Direccion de retorno')
    consola.append('stack[int('+t10+')]=1;// Devolvermos verdedaero')
    consola.append(L5+':')
    consola.append(L7+':')
    consola.append('}')
    consola.append(' ')               

def nativaPotencia(consola):
    '''
    func main() {
        stack[1] = 2
        stack[2] = 5
        t1 = P + 1
        t2 = stack[int(t1)]
        t3 = P + 2
        t4 = stack[int(t3)]
        t5 = 0 //Contador repeticiones
        t6 = 1 //Base
        if t4 == 0 {
            goto L1
        }
        goto L2
        L1:
            t7 = P + 0
            stack[int(t7)] = 1
            goto L3
        L2:
            if t5 >= t4 {
                goto L5
            }
            goto L4
        L4:
            t6 = t6 * t2
            t5 = t5 + 1
            goto L2
        L5:
            t7 = P + 0 //Direccion retorno
            stack[int(t7)] = t6
        L3: //Salida
        }        
    '''

    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()
    t6 = global_utils.generarTemporal()
    t7 = global_utils.generarTemporal()
    t8 = global_utils.generarTemporal()
    t9 = global_utils.generarTemporal()
    t10 = global_utils.generarTemporal()
    t11 = global_utils.generarTemporal()
    t12 = global_utils.generarTemporal()
    t13 = global_utils.generarTemporal()
    t14 = global_utils.generarTemporal()
    t15 = global_utils.generarTemporal()    
    t16 = global_utils.generarTemporal()
    t17 = global_utils.generarTemporal()
    t18 = global_utils.generarTemporal()    
    t19 = global_utils.generarTemporal()
    t20 = global_utils.generarTemporal()
    t21 = global_utils.generarTemporal()
    t22 = global_utils.generarTemporal()
    t23 = global_utils.generarTemporal()
    t24 = global_utils.generarTemporal()
    t25 = global_utils.generarTemporal()
    t26 = global_utils.generarTemporal()
    t27 = global_utils.generarTemporal()
    t28 = global_utils.generarTemporal()
    t29 = global_utils.generarTemporal()    

    L0 = global_utils.generarEtiqueta()
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()
    L5 = global_utils.generarEtiqueta()
    L6 = global_utils.generarEtiqueta()
    L7 = global_utils.generarEtiqueta()
    L8 = global_utils.generarEtiqueta()
    L9 = global_utils.generarEtiqueta()
    L10 = global_utils.generarEtiqueta()



    consola.append('func Potencia_nativa(){')    
    consola.append(t1+'=P+1;')
    consola.append(t2+'=stack[int('+t1+')];')
    consola.append(t3+'=P+2;')
    consola.append(t4+'=stack[int('+t3+')];')    
    consola.append(t5+'=0; //Contador repeticiones')
    consola.append(t6+'=1; //Base')
    consola.append('if ('+t4+' == 0) { goto '+L1+';}')
    consola.append('goto '+L2+';')
    consola.append(L1+':')
    consola.append(t7+'= P + 0')
    consola.append('stack[int('+t7+')] = 1')
    consola.append('goto '+L3+';')
    consola.append(L2+':')
    consola.append('if ('+t5+' >= '+t4+') { goto '+L5+';}')
    consola.append('goto '+L4+';')
    consola.append(L4+':')
    consola.append(t6+'='+t6+'*'+t2+';')
    consola.append(t5+'='+t5+'+1;')
    consola.append('goto '+L2+';')
    consola.append(L5+':')
    consola.append(t7+'=P+0;//Direccion retorno')
    consola.append('stack[int('+t7+')] = '+t6+';')
    consola.append(L3+': //Salida') 
    consola.append('}')
    consola.append(' ') 




def nativaFloatToString(consola):
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()
    t6 = global_utils.generarTemporal()
    t7 = global_utils.generarTemporal()
    t8 = global_utils.generarTemporal()
    t9 = global_utils.generarTemporal()
    t10 = global_utils.generarTemporal()
    t11 = global_utils.generarTemporal()
    t12 = global_utils.generarTemporal()
    t13 = global_utils.generarTemporal()
    t14 = global_utils.generarTemporal()
    t15 = global_utils.generarTemporal()    
    t16 = global_utils.generarTemporal()
    t17 = global_utils.generarTemporal()
    t18 = global_utils.generarTemporal()    
    t19 = global_utils.generarTemporal()
    t20 = global_utils.generarTemporal()
    t21 = global_utils.generarTemporal()
    t22 = global_utils.generarTemporal()
    t23 = global_utils.generarTemporal()
    t24 = global_utils.generarTemporal()
    t25 = global_utils.generarTemporal()
    t26 = global_utils.generarTemporal()
    t27 = global_utils.generarTemporal()
    t28 = global_utils.generarTemporal()
    t29 = global_utils.generarTemporal()    
    t30 = global_utils.generarTemporal() 

    L0 = global_utils.generarEtiqueta()
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()
    L5 = global_utils.generarEtiqueta()
    L6 = global_utils.generarEtiqueta()
    L7 = global_utils.generarEtiqueta()
    L8 = global_utils.generarEtiqueta()
    L9 = global_utils.generarEtiqueta()
    L10 = global_utils.generarEtiqueta()
    L11 = global_utils.generarEtiqueta()
    L12 = global_utils.generarEtiqueta()
    L13 = global_utils.generarEtiqueta()
    '''
    t0=P+0;
	t1=stack[int(t0)];//t1=3532.200006;
	t2=0;
    //Nuevo
    if(t1<0){goto L11;}
    goto L0;
    L11:
    t0=H;
    H=H+1;
    heap[int(t0)]=45;// -
    t1=t1*-1;
    t2=1;
    //Nuevo
	L0:
	t3=float64(int(t1));
	t4=t1-t3; // residuo decimal
	if(t4 >0){ goto L1;}	
	goto L2;
	L1:
	t1=t1*10;
	t2=t2+1;
	goto L0;
	L2: // Se comienza a crear la cadena
	t3=0;// Contador dígitos
	L3:
	if(t1>=10){ goto L4;}
	goto L5;// Ya sólo queda un dígito
	L4:
	if(t3==t2){goto L6;}
	goto L7;
	L6: // Ponemos el punto
	t4=H;
	H=H+1;
	heap[int(t4)]=46; // . 
	t3=t3+1;
	goto L3;
	L7: // Normal
	t5=float64(int(t1/10))
	t6=t5*10;
	t7=t1-t6;// Digito
	t8=t7+48;// Caracter digito
	t1=t6/10;
	t9=H;// Direccion nuevo caracter
	H=H+1;// Reservando espacio
	heap[int(t9)]=t8;// Guardando caracter
	t3=t3+1;
	goto L3;			
	L5: // Ultimo dígito
	t10=H;// Direccion nuevo caracter
	H=H+1;// Reservando espacio	
	t11=t1+48;// Caracter digito
	heap[int(t10)]=t11;
	t3=t3+1;s
	t10=H;// Inicio de cadena ordena
	t15=H;// Inicio cadena
	L8:
	if(t3>=0){ goto L9;}
	goto L10;
	L9:
	t11=heap[int(t10)];
	t12=H;
	H=H+1;
	heap[int(t12)]=t11;
	t3=t3-1;
	t10=t10-1;
	goto L8;
	L10:
	t13=H;
	H=H+1;
	heap[int(t13)]=55555;
	t14=P+0;//Direccion retorno
	stack[int(t14)]=t15;    
    '''

    consola.append('func FloatToString_Nativa(){')    
    consola.append(t0+'=P+1;')
    consola.append(t1+'=stack[int('+t0+')];')
    consola.append(t2+'=0;')
    ## Para manejo de negativos
    consola.append(t30+'=0;//Por defecto es positivo')    
    consola.append('if('+t1+'<0){goto '+L11+';}')
    consola.append('goto '+L0+';')
    consola.append(L11+':')
    consola.append(t1+'='+t1+'*-1;')
    consola.append(t30+'=1;//Significa negativo')
    ## Para manejo de negativos
    consola.append(L0+':')
    consola.append(t3+'=float64(int('+t1+'));')
    consola.append(t4+'='+t1+'-'+t3+'; // residuo decimal')
    consola.append('if('+t4+' >0){ goto '+L1+';}')
    consola.append('goto '+L2+';')
    consola.append(L1+':')
    consola.append(t1+'='+t1+'*10;')
    consola.append(t2+'='+t2+'+1;')
    consola.append('goto '+L0+';')
    consola.append(L2+': // Se comienza a crear la cadena')
    consola.append(t3+'=0;// Contador dígitos')
    consola.append(L3+':')
    consola.append('if('+t1+'>=10){ goto '+L4+';}')
    consola.append('goto '+L5+';// Ya sólo queda un dígito')
    consola.append(L4+':')
    consola.append('if('+t3+'=='+t2+'){goto '+L6+';}')
    consola.append('goto '+L7+';')
    consola.append(L6+': // Ponemos el punto')
    consola.append(t4+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t4+')]=46; // . ')
    consola.append(t3+'='+t3+'+1;')
    consola.append('goto '+L3+';')
    consola.append(L7+': // Normal')
    consola.append(t5+'=float64(int('+t1+'/10))')
    consola.append(t6+'='+t5+'*10;')
    consola.append(t7+'='+t1+'-'+t6+';// Digito')
    consola.append(t8+'='+t7+'+48;// Caracter digito')
    consola.append(t1+'='+t6+'/10;')
    consola.append(t9+'=H;// Direccion nuevo caracter')
    consola.append('H=H+1;// Reservando espacio')
    consola.append('heap[int('+t9+')]='+t8+';// Guardando caracter')
    consola.append(t3+'='+t3+'+1;')
    consola.append('goto '+L3+';')
    consola.append(L5+': // Ultimo dígito')
    consola.append(t10+'=H;// Direccion nuevo caracter')
    consola.append('H=H+1;// Reservando espacio')
    consola.append(t11+'='+t1+'+48;// Caracter digito')
    consola.append('heap[int('+t10+')]='+t11+';')
    consola.append(t3+'='+t3+'+1;')
    ### Verificamos para agregar el simbolo de menos    
    consola.append('if('+t30+'==1){ goto '+L12+';}//Agregamos el símbolo -')
    consola.append('goto '+L13+';')
    consola.append(L12+':')
    consola.append(t15+'=H;//Direccion nuevo caracter')
    consola.append('H=H+1;//Reservando espacio en memoria')
    consola.append('heap[int('+t15+')]=45;// -')
    consola.append(L13+':')    
    ### Verificamos para agregar el simbolo de menos
    consola.append(t10+'=H;// Inicio de cadena ordena')
    consola.append(t15+'=H;// Inicio cadena')
    consola.append(L8+':')
    consola.append('if('+t3+'>=0){ goto '+L9+';}')
    consola.append('goto '+L10+';')
    consola.append(L9+':')
    consola.append(t11+'=heap[int('+t10+')];')
    consola.append(t12+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t12+')]='+t11+';')
    consola.append(t3+'='+t3+'-1;')
    consola.append(t10+'='+t10+'-1;')
    consola.append('goto '+L8+';')
    consola.append(L10+':')
    consola.append(t13+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t13+')]='+str(global_utils.obtenerNulo())+';')
    consola.append(t14+'=P+0;//Direccion retorno')
    consola.append('stack[int('+t14+')]='+t15+';')        
    consola.append('}')
    consola.append(' ')   


def nativaIntToString(consola):
    '''
    t0=P+1  // Direccion valor int
    t1=stack[int(t0)]  // Valor int
    t2=0 // Contador de caracteres
    L0:
    if (t1>=10){ goto L1}
    goto L2
    L1:
    t3=t1/10  
    t4=t3*10
    t5=t1%t4 // Digito
    t6=t5+48 // Caracter digito
    t1=t3
    t7=H
    H=H+1 
    heap[int(t7)]=t6
    t2=t2+1 // Aumento contador
    goto L0
    L2:
    t8=t1+48 // Caracter digito
    t9=H
    H=H+1
    heap[int(t9)]=t8
    //t10=H
    //H=H+1
    //heap[int(t10)]=str(global_utils.obtenerNulo())
    t2=t2+1 // Aumento contador
    t11=H; // Inicio cadena    
    L3:    
    //t12=t11-t2 // Inicio cadena    
    if(t2>0){goto L4;}
    goto L5;
    L4:
    t12=heap[int(t2)]; // Caracter
    t13=H;
    H=H+1; // Reservando espacio
    heap[int(t13)]=t12;
    t2=t2-1;
    goto L3;
    L5:
    t14=H
    H=H+1
    heap[int(t14)]=str(global_utils.obtenerNulo())    
    t15=P+0
    stack[t15]=t11 // H ---> inicio nueva cadena
    '''
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()
    t6 = global_utils.generarTemporal()
    t7 = global_utils.generarTemporal()
    t8 = global_utils.generarTemporal()
    t9 = global_utils.generarTemporal()
    t10 = global_utils.generarTemporal()
    t11 = global_utils.generarTemporal()
    t12 = global_utils.generarTemporal()
    t13 = global_utils.generarTemporal()
    t14 = global_utils.generarTemporal()
    t15 = global_utils.generarTemporal()  
    t30 = global_utils.generarTemporal()  

    L0 = global_utils.generarEtiqueta()
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()
    L5 = global_utils.generarEtiqueta()
    L11 = global_utils.generarEtiqueta()
    L12 = global_utils.generarEtiqueta()
    L13 = global_utils.generarEtiqueta()
    L15 = global_utils.generarEtiqueta()
    
    consola.append('func IntToString_Nativa(){')
    consola.append(t0+'=P+1;  // Direccion valor int')
    consola.append(t1+'=stack[int('+t0+')];  // Valor int')
    consola.append(t2+'=0;// Contador de caracteres')
    ## Para manejo de negativos
    consola.append(t30+'=0;//Por defecto es positivo')    
    consola.append('if('+t1+'<0){goto '+L11+';}')
    consola.append('goto '+L0+';')
    consola.append(L11+':')
    consola.append(t1+'='+t1+'*-1;')
    consola.append(t30+'=1;//Significa negativo')
    ## Para manejo de negativos
    consola.append(L0+':')
    consola.append('if ('+t1+'>=10){ goto '+L1+'; }')
    consola.append('goto '+L2+';')
    consola.append(L1+':')
    consola.append(t3+'=float64(int('+t1+'/10));')
    consola.append(t4+'='+t3+'*10;')
    consola.append(t5+'='+t1+'-'+t4+'; // Digito')
    consola.append(t6+'='+t5+'+48;// Caracter digito')
    consola.append(t1+'='+t4+'/10;')
    consola.append(t7+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t7+')]='+t6+';')
    consola.append(t2+'='+t2+'+1;// Aumento contador')
    consola.append('goto '+L0+';')
    consola.append(L2+':')
    consola.append(t8+'='+t1+'+48; // Caracter digito')
    consola.append(t9+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t9+')]='+t8+';')
    consola.append(t2+'='+t2+'+1;// Aumento contador')
    consola.append(t11+'=H; // Inicio de cadena ordenada')
    consola.append(t10+'=H;')
    ### Verificamos para agregar el simbolo de menos    
    consola.append('if('+t30+'==1){ goto '+L12+';}//Agregamos el símbolo -')
    consola.append('goto '+L13+';')
    consola.append(L12+':')
    consola.append(t15+'=H;//Direccion nuevo caracter')
    consola.append('H=H+1;//Reservando espacio en memoria')
    consola.append('heap[int('+t15+')]=45;// -')
    consola.append(t10+'=H;')
    consola.append(L13+':')    
    ### Verificamos para agregar el simbolo de menos    
    consola.append(L3+':')
    consola.append('if('+t2+'>=0){ goto '+ L4+ ';}')
    consola.append('goto '+L5+';')
    consola.append(L4+':')  
    consola.append(t12+'=heap[int('+t11+')]; // Caracter')
    consola.append(t13+'=H;')
    consola.append('H=H+1; // Reservando espacio')
    consola.append('heap[int('+t13+')]='+t12+';')
    consola.append(t2+'='+t2+'-1;')
    consola.append(t11+'='+t11+'-1;')
    consola.append('goto '+L3+';')
    consola.append(L5+':')
    consola.append(t14+'=H')
    consola.append('H=H+1')
    consola.append('heap[int('+t14+')]='+str(global_utils.obtenerNulo())+';// Fin cadena')    
    consola.append(t15+'=P+0;')    
    consola.append('stack[int('+t15+')]='+t10+';// H ---> inicio nueva cadena')
    consola.append('}')
    consola.append(' ')    
    

def nativaConcatenacion(consola):
    '''
    t0=P+1 // Direccion primer cadena
    t1=stack[t0] // Referencia primer cadena
    t2=P+2 // Direccion segunda cadena
    t3=stack[t2] // Referencia segunda cadena
    t4=H
    t5=t1
    t6=t3
    L1: 
    t7=heap[t5]
    if (t7!=str(global_utils.obtenerNulo()) {goto L2}
    goto L3
    L2: 
    t8=H
    H=H+1
    heap[t8]=t7
    t5=t5+1
    goto L1
    L3:    
    t9=heap[t6]
    if (t9!=str(global_utils.obtenerNulo()){goto L4}
    goto L5
    L4:
    t10=H
    H=H+1
    heap[t10]=t9
    t6=t6+1
    goto L3
    L5:
    t11=H
    H=H+1
    heap[t11]=str(global_utils.obtenerNulo()
    t12=P+0
    stack[t12]=t4
    '''    
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    t3 = global_utils.generarTemporal()
    t4 = global_utils.generarTemporal()
    t5 = global_utils.generarTemporal()
    t6 = global_utils.generarTemporal()
    t7 = global_utils.generarTemporal()
    t8 = global_utils.generarTemporal()
    t9 = global_utils.generarTemporal()
    t10 = global_utils.generarTemporal()
    t11 = global_utils.generarTemporal()
    t12 = global_utils.generarTemporal()        
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()    
    L3 = global_utils.generarEtiqueta()
    L4 = global_utils.generarEtiqueta()    
    L5 = global_utils.generarEtiqueta()
    consola.append('func concatenar_Nativa(){')
    consola.append(t0+'=P+1;// Direccion primer cadena')
    consola.append(t1+'=stack[int('+t0+')];// Referencia primer cadena')
    consola.append(t2+'=P+2;// Direccion segunda cadena')
    consola.append(t3+'=stack[int('+t2+')];// Referencia segunda cadena')
    consola.append(t4+'=H;')
    consola.append(t5+'='+t1+';')
    consola.append(t6+'='+t3+';')
    consola.append(L1+':') 
    consola.append(t7+'=heap[int('+t5+')];')
    consola.append('if ('+t7+'!='+str(global_utils.obtenerNulo())+'){ goto '+L2+'; }')
    consola.append('goto '+L3+';')
    consola.append(L2+':')
    consola.append(t8+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t8+')]='+t7+';')
    consola.append(t5+'='+t5+'+1;')
    consola.append('goto '+L1+';')
    consola.append(L3+':')
    consola.append(t9+'=heap[int('+t6+')];')
    consola.append('if ('+t9+'!='+str(global_utils.obtenerNulo())+'){ goto '+L4+'; }')
    consola.append('goto '+L5+';')
    consola.append(L4+':')
    consola.append(t10+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t10+')]='+t9+';')
    consola.append(t6+'='+t6+'+1;')
    consola.append('goto '+L3+';')
    consola.append(L5+':')
    consola.append(t11+'=H;')
    consola.append('H=H+1;')
    consola.append('heap[int('+t11+')]='+str(global_utils.obtenerNulo())+';')
    consola.append(t12+'=P+0;')
    consola.append('stack[int('+t12+')]='+t4+';')
    consola.append('}')
    consola.append(' ')

def nativaImpresion(consola):
    consola.append('func imprimir_Nativa(){')
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()    
    consola.append(t0+'=P+0;// Direccion parametro')
    consola.append(t1+'=stack[int('+t0+')];// Direccion en el heap')
    consola.append(L1+':')
    consola.append(t2+'=heap[int('+t1+')];')
    consola.append('if('+t2+'=='+str(global_utils.obtenerNulo())+'){goto '+L2+'; }')
    consola.append('fmt.Printf("%c",int('+t2+'));')
    consola.append(t1+'='+t1+'+1;')
    consola.append('goto '+ L1+';')
    consola.append(L2+':')
    consola.append('}')
    consola.append(' ')

def nativaImpresionln(consola):
    consola.append('func imprimir_Nativa(){')
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()    
    consola.append(t0+'=P+0;// Direccion parametro')
    consola.append(t1+'=stack[int('+t0+')];// Direccion en el heap')
    consola.append(L1+':')
    consola.append(t2+'=heap[int('+t1+')];')
    consola.append('if('+t2+'=='+str(global_utils.obtenerNulo())+'){goto '+L2+'; }')
    consola.append('fmt.Printf("%c",int('+t2+'));')
    consola.append(t1+'='+t1+'+1;')
    consola.append('goto '+ L1+';')
    consola.append(L2+':')
    consola.append('fmt.Printf("%c",10);// Salto de linea')
    consola.append('}')
    consola.append(' ') 

def nativaImpresion(consola):
    consola.append('func imprimir_sn_Nativa(){')
    t0 = global_utils.generarTemporal()
    t1 = global_utils.generarTemporal()
    t2 = global_utils.generarTemporal()
    L1 = global_utils.generarEtiqueta()
    L2 = global_utils.generarEtiqueta()    
    consola.append(t0+'=P+0;// Direccion parametro')
    consola.append(t1+'=stack[int('+t0+')];// Direccion en el heap')
    consola.append(L1+':')
    consola.append(t2+'=heap[int('+t1+')];')
    consola.append('if('+t2+'=='+str(global_utils.obtenerNulo())+'){goto '+L2+'; }')
    consola.append('fmt.Printf("%c",int('+t2+'));')
    consola.append(t1+'='+t1+'+1;')
    consola.append('goto '+ L1+';')
    consola.append(L2+':')    
    consola.append('}')
    consola.append(' ')     


### Tabla de símbolo
class TipoPrimitivo(Enum):
    NULO = 1
    ENTERO = 2
    FLOAT = 3
    BOOL = 4
    CHAR = 5
    STRING = 6
    ARREGLO = 7
    STRUCT = 8
    ERROR = 9
    DINAMICO =20

class Rol(Enum):
    VAR = 10
    FUNCION = 11    

NOMBRES = {
    1: 'Nulo',
    2: 'int',
    3: 'float',
    4: 'bool',
    5: 'char',
    6: 'string',
    7: 'arreglo',
    8: 'struct',
    9: 'error'
}

class Tipo():
    def __init__(self, tipo, primitivo = True,  nombre=""):
        self.tipo = tipo
        self.primitivo = primitivo
        self.nombre = nombre

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2) 
        
    def getNombre(self):
        if self.tipo == TipoPrimitivo.NULO:
            return 'nulo'
        if self.tipo == TipoPrimitivo.ENTERO:
            return 'Int64'
        if self.tipo ==  TipoPrimitivo.FLOAT:
            return 'Float64'
        if self.tipo ==  TipoPrimitivo.BOOL:
            return 'Bool'
        if self.tipo ==  TipoPrimitivo.CHAR:
            return 'char'
        if self.tipo ==  TipoPrimitivo.STRING:
            return 'String'
        if self.tipo ==  TipoPrimitivo.ARREGLO:
            return 'arreglo'
        if self.tipo ==  TipoPrimitivo.STRUCT:
            return 'struct'
        if self.tipo ==  TipoPrimitivo.DINAMICO:
            return 'dinamico'            
        if self.tipo ==  TipoPrimitivo.ERROR:
            return 'error'        

    def esCadena(self):
        return self.tipo == TipoPrimitivo.STRING
    def esNulo(self):
        return self.tipo == TipoPrimitivo.NULO
    def esEntero(self):
        return self.tipo == TipoPrimitivo.ENTERO
    def esFloat(self):
        return self.tipo == TipoPrimitivo.FLOAT
    def esBool(self):
        return self.tipo == TipoPrimitivo.BOOL 
    def esChar(self):
        return self.tipo == TipoPrimitivo.CHAR
    def esError(self):
        return self.tipo == TipoPrimitivo.ERROR
    def esArreglo(self):
        return self.tipo == TipoPrimitivo.ARREGLO
    def esLlamada(self):
        return self.tipo == TipoPrimitivo.LLAMADA   
    def esDinamico(self):
        return self.tipo == TipoPrimitivo.DINAMICO or self.tipo == TipoPrimitivo.ARREGLO             
    def esNumerico(self):
        return self.tipo == TipoPrimitivo.ENTERO or self.tipo == TipoPrimitivo.FLOAT 
    def compararTipo(self, tipo):
        return self.tipo == tipo.tipo


class Simbolo():
    def __init__(self, id, tipo, linea, columna):
        self.id = id 
        self.tipo = tipo        
        self.linea = linea
        self.columna = columna        
        self.mutable = True
        self.rol = Rol.VAR
    
    def getTipo(self):
        return self.tipo

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)

    def getRol(self):
        if self.rol == Rol.FUNCION:
            return 'funcion'
        if self.rol == Rol.VAR:
            return 'variable'   

class Variable(Simbolo):
    def __init__(self, id, tipo, valor, linea, columna):
        self.id = id 
        self.tipo = tipo        
        self.linea = linea
        self.columna = columna  
        self.rol = Rol.VAR      
        self.mutable = True

    def getTipo(self):
        return self.tipo

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)

    def getRol(self):
        if self.rol == Rol.FUNCION:
            return 'funcion'
        if self.rol == Rol.VAR:
            return 'variable' 
        

class FuncionSimbolo(Simbolo):
    def __init__(self, id, parametros, instrucciones, linea, columna):
        self.id = id 
        self.parametros = parametros
        self.rol = Rol.FUNCION
        self.linea = linea 
        self.columna = columna 
        self.instrucciones = instrucciones
        self.tipo = Tipo(TipoPrimitivo.DINAMICO)

    def getTipo(self, entorno):
        tmp = self.instrucciones.ejecutar(entorno)
        if tmp is None:
            return Tipo(TipoPrimitivo.ERROR)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)
    def getRol(self):
        if self.rol == Rol.FUNCION:
            return 'funcion'
        if self.rol == Rol.VAR:
            return 'variable'

class EstructuraSimbolo(Simbolo):
    def __init__(self, id, atributos, mutable, linea, columna):
        self.id = id 
        self.atributos = atributos
        self.linea = linea
        self.columna = columna
        self.mutable = mutable
        self.tipo = Tipo(TipoPrimitivo.STRUCT, self.id)
    
    def getTipo(self, entorno):
        return Tipo(TipoPrimitivo.STRUCT, self.id)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)

    def getRol(self):
        return 'Struct ' + self.id

    def generarInstancia(self, id, valores, entorno):        
        instancia = Simbolo(id, self.getTipo(entorno), None, self.linea, self.columna)
        instancia.mutable = self.mutable
        entorno = Entorno(None)
        contador = 0
        if len(valores) == len(self.atributos):
            for i in valores:
                self.atributos[contador].expresion = i
                self.atributos[contador].ejecutar(entorno)
                contador += 1
        else:
            global_utils.registrySemanticError('Instancia estructura', 'el número de parametros no coincide con la definicion.' + self.id, self.linea, self.columna)
        return instancia




'''Tabla de símbolos -------------------------------------------'''
class TablaSimbolo():
    def __init__(self):
        self.tabla = {}
        self.consola = []
        self.contadorSimbolos = 0

    def registrarSimbolo(self, simbolo):        
        tmp_simbolo = self.tabla.get(simbolo.id)
        if tmp_simbolo is not None:
            if tmp_simbolo.rol == simbolo.rol:
                if tmp_simbolo.rol == Rol.VAR:
                    global_utils.registrySemanticError('Declaracion', 'Ya se ha declarado previamente una variable con el nombre '+ simbolo.id, simbolo.linea, simbolo.columna)
                    return 
                else:
                    if simbolo.parametros is None or tmp_simbolo.parametros is None:
                        global_utils.registrySemanticError('Declaracion', 'Ya se ha declarado previamente una función con el nombre '+ simbolo.id + ' con 0 parámetros.', simbolo.linea, simbolo.columna)
                        return                         
                    if len(simbolo.parametros) == len(tmp_simbolo.parametros):                        
                        global_utils.registrySemanticError('Declaracion', 'Ya se ha declarado previamente una función con el nombre '+ simbolo.id + ' con ' +str(len(simbolo.parametros)) + ' parámetros.', simbolo.linea, simbolo.columna)
                        return                     
                    else:   
                        simbolo.posicion = self.contadorSimbolos
                        self.contadorSimbolos +=1                     
                        self.tabla[simbolo.id] = simbolo                    
            else:
                simbolo.posicion = self.contadorSimbolos
                self.contadorSimbolos +=1                
                self.tabla[simbolo.id] = simbolo

        else:
            simbolo.posicion = self.contadorSimbolos
            self.contadorSimbolos +=1            
            self.tabla[simbolo.id] = simbolo
    
    def getSimbolo(self, id):
        entornoActual = self
        return self.tabla.get(id)

    def getFuncion(self, id, numero_parametros):
        entornoActual = self
        return self.tabla.get(id)        
    
    def imprimirln(self, valor):        
        global consola
        if isinstance(valor, list):
            consola.append(str(valor))
        else:
            consola.append(str(valor))
    def imprimir(self, valor):
        global consola                
        if isinstance(valor, list):       
            cadena = ''
            for i in valor:
                if isinstance(i, Simbolo):
                    cadena = cadena + str(i.valor)
                else:
                    cadena = cadena + str
            if len(consola) > 0:
                texto = consola[len(consola)-1]        
                consola[len(consola)-1] = texto+str(valor)
            else:             
                consola.append(str(valor))
        else:            
            if len(consola) > 0:
                texto = consola[len(consola)-1]        
                consola[len(consola)-1] = texto+str(valor)
            else:             
                consola.append(str(valor))    

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)          

'''Entorno -------------------------------------------------------'''
class Entorno():
    def __init__(self, padre):
        self.tabla = TablaSimbolo()
        self.padre = padre
    
    def getSimbolo(self, id):
        '''Buscamos en el entorno actual y si no está, buscamos en el entorno superior'''
        entornoActual = self
        while entornoActual is not None:
            tmpValor = entornoActual.tabla.getSimbolo(id)
            if tmpValor is None:
                entornoActual = entornoActual.padre
            else: 
                return tmpValor
        return None        
    
    def insertSimbolo(self, simbolo):
        self.tabla.registrarSimbolo(simbolo)
    
    def imprimir(self, valor):
        self.tabla.imprimir(valor)
    
    def imprimirln(self, valor):
        self.tabla.imprimirln(valor)

    def tamanioEntorno(self):
        return len(self.tabla.tabla)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=2)  

    def obtenerTipo(self, valor):
        if valor is None:
            return Tipo(TipoPrimitivo.NULO)
        if isinstance(valor, int):
            return Tipo(TipoPrimitivo.ENTERO)
        if isinstance(valor, float):
            return Tipo(TipoPrimitivo.FLOAT)
        if isinstance(valor, bool):
            return Tipo(TipoPrimitivo.BOOL)
        if isinstance(valor, str):
            return Tipo(TipoPrimitivo.STRING)            
        if isinstance(valor, Simbolo):
            return valor.tipo
        if isinstance(valor, list):
            return Tipo(TipoPrimitivo.DINAMICO)
        return Tipo(TipoPrimitivo.ERROR)
### AST 
class NodoAST(ABC):
    pass

### Definición de expresion
class Expresion(NodoAST):

    @abstractmethod
    def getValor(self, entorno):
        pass

    @abstractmethod
    def getTipo(self, entorno):
        pass

    @abstractmethod
    def graficar(self, padre, grafo):
        pass    


## Definición de instruccion
class Instruccion(NodoAST):
    @abstractmethod
    def ejecutar(self, entorno):
        pass

    @abstractmethod
    def graficar(self, padre, grafo):
        pass       

class Raiz(Instruccion):
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
    
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, 'S')
        grafo.edge(padre, id)
        for inst in self.instrucciones:
            inst.graficar(id, grafo)
    
    def ejecutar(self, entorno):
        #Primero hacemos la primer pasada
        self.limpiarTodo()
        agregarFuncionesNativas()
        self.primeraPasada(entorno)
        self.segundaPasada(entorno)
    
    def limpiarTodo(self):
        global consola
        consola = []
        global_utils.iniciar()

    def primeraPasada(self, entorno):        
        '''En esta primera pasada genramos el código de todos los métodos y estructuras'''        
        global_utils.iniciar
        for inst in self.instrucciones.instrucciones:
            if isinstance(inst, Funcion):  
                inst.ejecutar(entorno)        

    def segundaPasada(self, entorno):
        '''En esta segunda pasada generamos el código del main.'''
        consola.append('func main(){')
        for inst in self.instrucciones.instrucciones:
            if not isinstance(inst, Funcion): 
                if isinstance(inst, Llamada):
                    inst.getValor(entorno)
                elif isinstance(inst, Declaracion):
                    inst.ejecutar(entorno)
                else:                    
                    inst.ejecutar(entorno)        
        consola.append('}')

## Instrucciones ------------------------------------------------
class Bloque(Instruccion):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
        self.instrucciones = []
    
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '(Inst)Bloque_Instrucciones')
        grafo.edge(padre, id)
        for inst in self.instrucciones:
            inst.graficar(id, grafo)
        


    def agregarInstruccion(self, instruccion):
        self.instrucciones.append(instruccion)
    
    def ejecutar(self, entorno):
        for inst in self.instrucciones:
            if isinstance(inst, Break):
                return inst
            elif isinstance(inst, Continue):
                return inst
            elif isinstance(inst, Retorno):
                return inst.ejecutar(entorno)
            else:
                if isinstance(inst, Instruccion):
                    val = inst.ejecutar(entorno)
                    if val is not None:
                        if isinstance(val, Break):
                            return val
                        if isinstance(val, Continue):
                            return val
                        return val
                elif isinstance(inst, Expresion):
                    val = inst.getValor(entorno)
                    if val is not None:
                        if isinstance(val, Break):
                            return val
                        if isinstance(val, Continue):
                            return val                    


class Imprimir(Instruccion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '(Inst)Imprimir')
        grafo.edge(padre, id)
        for inst in self.lista_expresiones:
            inst.graficar(id, grafo)        
    
    def ejecutar(self, entorno):
        tipo = self.expresion.getTipo(entorno)
        valor = self.expresion.getValor(entorno) 
        if tipo is None:
            return       
        if tipo.esEntero():    
            entorno.imprimirln('fmt.Printf("%d", int(' + str(valor) +'));')            
        if tipo.esFloat():
            entorno.imprimirln('fmt.Printf("%f",' + str(valor) +');') 
        if tipo.esNulo():
            nodoAuxiliar = String("nothing",0,0)
            valorAuxiliar = nodoAuxiliar.getValor(entorno)
            ##Impresion etiqueta nothing
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()            
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+';// Paso de inicio de cadena.')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('imprimir_sn_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
        if tipo.esBool():
            '''
            if valor==1 goto L1 
            goto L2
            L1:
            imprimir verdadero
            goto L3
            L2:    
            imprimir falso
            L3:        
            '''
            if isinstance(valor, int) or isinstance(valor,str):
                L1 = global_utils.generarEtiqueta()
                L2 = global_utils.generarEtiqueta()
                L3 = global_utils.generarEtiqueta()
                entorno.imprimirln('if ('+str(valor)+'==1){goto '+L1+';}')
                entorno.imprimirln('goto '+L2+';')
                #Etiqueta verdadera
                entorno.imprimirln(L1+":")
                nodoAuxiliar = String("true",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno)  
                ##Impresion etiqueta verdadera
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+'; // Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_sn_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno') 
                entorno.imprimirln('goto '+L3+';')
                ## Etiqueta false
                entorno.imprimirln(L2+":")
                nodoAuxiliar = String("false",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno) 
                ##Impresion etiqueta falso
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+';// Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_sn_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')                        
                entorno.imprimirln(L3+":") 
            elif (valor.lv is not None):
                L1 = global_utils.generarEtiqueta()
                L2 = global_utils.generarEtiqueta()
                L3 = global_utils.generarEtiqueta()
                #Etiqueta verdadera
                entorno.imprimirln(valor.lv+":")
                nodoAuxiliar = String("true",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno)  
                ##Impresion etiqueta verdadera
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+'; // Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_sn_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno') 
                entorno.imprimirln('goto '+L3+';')
                ## Etiqueta false
                entorno.imprimirln(valor.lf+":")
                nodoAuxiliar = String("false",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno) 
                ##Impresion etiqueta falso
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+';// Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_sn_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')                        
                entorno.imprimirln(L3+":")                 
                pass
        if tipo.esCadena():
            '''
            t0=P+size(entorno.tabla) // Simulacion de cambio de entorno
            t1=P+0  // Dirección parametro 1
            stack[int(t1)]=valor // Paso de inicio de cadena.
            P=P+size(entorno.tabla) // Cambio de entorno
            imprimir_Nativa()
            P=P-size(entorno.tabla) // Retomar entorno
            '''
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()

            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(valor)+';// Paso de inicio de cadena.')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('imprimir_sn_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')  
        ##Salto para todos.        

class ImprimirLn(Instruccion):
    def __init__(self, expresion, linea, columna): 
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '(Inst)ImprimirLn')
        grafo.edge(padre, id)
        for inst in self.lista_expresiones:
            inst.graficar(id, grafo)  

    def ejecutar(self, entorno):
        tipo = self.expresion.getTipo(entorno)
        valor = self.expresion.getValor(entorno)        
        if tipo.esEntero():    
            entorno.imprimirln('fmt.Printf("%d", int(' + str(valor) +'));')            
        if tipo.esFloat():
            entorno.imprimirln('fmt.Printf("%f",' + str(valor) +');') 
        if tipo.esNulo():
            nodoAuxiliar = String("nothing",0,0)
            valorAuxiliar = nodoAuxiliar.getValor(entorno)
            ##Impresion etiqueta nothing
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()            
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+';// Paso de inicio de cadena.')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('imprimir_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
        if tipo.esBool():
            '''
            if valor==1 goto L1 
            goto L2
            L1:
            imprimir verdadero
            goto L3
            L2:    
            imprimir falso
            L3:        
            '''
            if isinstance(valor, int) or isinstance(valor,str):
                L1 = global_utils.generarEtiqueta()
                L2 = global_utils.generarEtiqueta()
                L3 = global_utils.generarEtiqueta()
                entorno.imprimirln('if ('+str(valor)+'==1){goto '+L1+';}')
                entorno.imprimirln('goto '+L2+';')
                #Etiqueta verdadera
                entorno.imprimirln(L1+":")
                nodoAuxiliar = String("true",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno)  
                ##Impresion etiqueta verdadera
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+'; // Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno') 
                entorno.imprimirln('goto '+L3+';')
                ## Etiqueta false
                entorno.imprimirln(L2+":")
                nodoAuxiliar = String("false",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno) 
                ##Impresion etiqueta falso
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+';// Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')                        
                entorno.imprimirln(L3+":") 
            elif (valor.lv is not None):
                L1 = global_utils.generarEtiqueta()
                L2 = global_utils.generarEtiqueta()
                L3 = global_utils.generarEtiqueta()
                #Etiqueta verdadera
                entorno.imprimirln(valor.lv+":")
                nodoAuxiliar = String("true",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno)  
                ##Impresion etiqueta verdadera
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+'; // Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno') 
                entorno.imprimirln('goto '+L3+';')
                ## Etiqueta false
                entorno.imprimirln(valor.lf+":")
                nodoAuxiliar = String("false",0,0)
                valorAuxiliar = nodoAuxiliar.getValor(entorno) 
                ##Impresion etiqueta falso
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorAuxiliar)+';// Paso de inicio de cadena.')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_Nativa();')            
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')                        
                entorno.imprimirln(L3+":")                 
                pass
        if tipo.esCadena():
            '''
            t0=P+size(entorno.tabla) // Simulacion de cambio de entorno
            t1=P+0  // Dirección parametro 1
            stack[int(t1)]=valor // Paso de inicio de cadena.
            P=P+size(entorno.tabla) // Cambio de entorno
            imprimir_Nativa()
            P=P-size(entorno.tabla) // Retomar entorno
            '''
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()

            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+0;// Dirección parametro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(valor)+';// Paso de inicio de cadena.')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('imprimir_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')  
        ##Salto para todos.
        #entorno.imprimirln('fmt.Printf("%c", 10);// Salto de linea')
        
class Declaracion(Instruccion):
    def __init__(self, id, expresion, tipo , linea, columna):
        self.id = id
        self.expresion = expresion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '(Inst)Declaracion')
        grafo.node(id+self.id,'Id '+ self.id)                
        grafo.edge(id,id+self.id)
        grafo.edge(padre, id) 
        if self.tipo is not None:
            grafo.node(id+'tipo', '[Tipo]: ' + self.tipo.getNombre())
            grafo.edge(id, id+'tipo')
        if self.expresion is not None:
            self.expresion.graficar(id, grafo)          
    
    def ejecutar(self, entorno):                
        val_tmp = entorno.tabla.getSimbolo(self.id)              
        if val_tmp is not None:            
            '''
            La variable no está registrada aún
            '''
            if self.tipo is not None:                
                '''
                Se ha indicado el tipo espeado
                Se realiza esa verificación
                '''
                tipo_tmp = self.expresion.getTipo(entorno)
                if tipo_tmp is not None:
                    if not tipo_tmp.compararTipo(self.tipo):
                        global_utils.registrySemanticError('Declaracion',  self.id + '. Se esperaba un valor de tipo ' + self.tipo.getNombre() + ', se obtuvo un valor de tipo ' + tipo_tmp.getNombre(), self.linea, self.columna)
                        return
                    '''
                    Si los tipos coinciden, realizamos la asignación
                    '''
                    valor = self.expresion.getValor(entorno)
                    nuevo_simbolo = val_tmp
                    val_tmp.tipo=tipo_tmp                    
                    if self.tipo.esNumerico():
                        t0=global_utils.generarTemporal()
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';// direccion '+nuevo_simbolo.id)
                        entorno.imprimirln('stack[int('+t0 +')]='+valor+';')
                else:
                    '''
                    Error en valor tratado de asignar
                    '''
                    global_utils.registrySemanticError('Declaracion', self.id + '. Se esperaba un valor de tipo ' + self.tipo.getNombre() + ' y no se ha obtenido valor. ', self.linea, self.columna) 
            
            else: 
                '''
                No se ha indicado tipo del valor a asignar.
                No se realiza esa verificación
                '''           
                if isinstance(self.expresion, Llamada):
                    '''
                    Caso especial para llamada de métodos
                    '''
                    valor = self.expresion.getValor(entorno)
                    if isinstance(valor, int):
                        tipo = entorno.obtenerTipo(valor)                    
                        nuevo_simbolo = val_tmp
                        val_tmp.tipo=tipo_tmp                  
                else:
                    '''
                    Caso normal
                    '''
                    tipo_tmp = self.expresion.getTipo(entorno)
                    valor = self.expresion.getValor(entorno)
                    if isinstance(valor, int):                        
                        nuevo_simbolo = val_tmp
                        val_tmp.tipo=tipo_tmp
                        t0 = global_utils.generarTemporal()            
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]='+str(valor)+';//Asignar valor')                        

                    elif isinstance(valor, str):
                        nuevo_simbolo = val_tmp
                        val_tmp.tipo=tipo_tmp     
                        t0 = global_utils.generarTemporal()
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]='+str(valor)+';//Asignar valor')
                    else:
                        '''
                        Se asume que valor viene después de un expresion booleana, o relacional
                        '''
                        nuevo_simbolo = val_tmp
                        val_tmp.tipo=tipo_tmp

                        t0 = global_utils.generarTemporal()
                        L1 = global_utils.generarEtiqueta()                      
                        entorno.imprimirln(valor.lv+':')
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]=1;//Asignar valor verdadero')
                        entorno.imprimirln('goto '+L1+';')
                        entorno.imprimirln(valor.lf+':')
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]=0;//Asignar valor falso')
                        entorno.imprimirln(L1+':') 
        else:
            '''
            La variable no está registrada aún
            '''
            if self.tipo is not None:                
                '''
                Se ha indicado el tipo espeado
                Se realiza esa verificación
                '''
                tipo_tmp = self.expresion.getTipo(entorno)
                if tipo_tmp is not None:
                    if not tipo_tmp.compararTipo(self.tipo):
                        global_utils.registrySemanticError('Declaracion',  self.id + '. Se esperaba un valor de tipo ' + self.tipo.getNombre() + ', se obtuvo un valor de tipo ' + tipo_tmp.getNombre(), self.linea, self.columna)
                        return
                    '''
                    Si los tipos coinciden, realizamos la asignación
                    '''
                    valor = self.expresion.getValor(entorno)
                    nuevo_simbolo = Simbolo(self.id, self.tipo, self.linea, self.columna)
                    entorno.tabla.registrarSimbolo(nuevo_simbolo)
                    if self.tipo.esNumerico():
                        t0=global_utils.generarTemporal()
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';// direccion '+nuevo_simbolo.id)
                        entorno.imprimirln('stack[int('+t0 +')]='+valor+';')
                else:
                    '''
                    Error en valor tratado de asignar
                    '''
                    global_utils.registrySemanticError('Declaracion', self.id + '. Se esperaba un valor de tipo ' + self.tipo.getNombre() + ' y no se ha obtenido valor. ', self.linea, self.columna) 
            
            else: 
                '''
                No se ha indicado tipo del valor a asignar.
                No se realiza esa verificación
                '''           
                if isinstance(self.expresion, Llamada):
                    '''
                    Caso especial para llamada de métodos
                    '''
                    valor = self.expresion.getValor(entorno)
                    if isinstance(valor, int):
                        tipo = entorno.obtenerTipo(valor)                    
                        nuevo_simbolo = Simbolo(self.id, tipo, valor, self.linea, self.columna)            
                        entorno.tabla.registrarSimbolo(nuevo_simbolo)                      
                else:
                    '''
                    Caso normal
                    '''
                    tipo_tmp = self.expresion.getTipo(entorno)
                    valor = self.expresion.getValor(entorno)
                    if isinstance(valor, int):
                        nuevo_simbolo = Simbolo(self.id, tipo_tmp, self.linea, self.columna)            
                        entorno.tabla.registrarSimbolo(nuevo_simbolo)
                        t0 = global_utils.generarTemporal()            
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]='+str(valor)+';//Asignar valor')                        

                    elif isinstance(valor, str):
                        nuevo_simbolo = Simbolo(self.id, tipo_tmp, self.linea, self.columna)            
                        entorno.tabla.registrarSimbolo(nuevo_simbolo)      
                        t0 = global_utils.generarTemporal()
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]='+str(valor)+';//Asignar valor')
                    else:
                        '''
                        Se asume que valor viene después de un expresion booleana, o relacional
                        '''
                        nuevo_simbolo = Simbolo(self.id, tipo_tmp, self.linea, self.columna)            
                        entorno.tabla.registrarSimbolo(nuevo_simbolo)  

                        t0 = global_utils.generarTemporal()
                        L1 = global_utils.generarEtiqueta()                      
                        entorno.imprimirln(valor.lv+':')
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]=1;//Asignar valor verdadero')
                        entorno.imprimirln('goto '+L1+';')
                        entorno.imprimirln(valor.lf+':')
                        entorno.imprimirln(t0+'=P+'+str(nuevo_simbolo.posicion)+';//Direccion variables')
                        entorno.imprimirln('stack[int('+t0+')]=0;//Asignar valor falso')
                        entorno.imprimirln(L1+':')                                                             

class If(Instruccion):
    def __init__(self, expresion, bloque, sino, linea, columna):
        self.expresion = expresion
        self.bloque = bloque 
        self.sino = sino
        self.linea = linea 
        self.columna = columna
        
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'if')
        grafo.edge(padre, id) 
        self.expresion.graficar(id, grafo)
        self.bloque.graficar(id,grafo)
        if self.sino is not None:
            self.sino.graficar(id,grafo)
        

    def ejecutar(self, entorno):
        #print('Ejecutando IF')
        tipo_tmp = self.expresion.getTipo(entorno)
        
        if tipo_tmp is None:
            global_utils.registrySemanticError('if', 'Valor inválido de la expresión condicional.', self.linea, self.columna) 
            return
        if tipo_tmp.esError():
            global_utils.registrySemanticError('if', 'Valor inválido de la expresión condicional.', self.linea, self.columna)             
            #global_utils.registrySemanticError('if', 'Tipo expresión condicional inválido. ' + tipo_tmp.getNombre() , self.linea, self.columna) 
            return 
        valor_condicion = self.expresion.getValor(entorno)
        if isinstance(valor_condicion, (int, str)):
            L1=global_utils.generarEtiqueta()
            L2=global_utils.generarEtiqueta()
            L3=global_utils.generarEtiqueta()
            entorno.imprimirln('if('+str(valor_condicion)+'==1){goto '+L1+';}')
            entorno.imprimirln('goto '+L2+';')
            entorno.imprimirln(L1+'://Verdadero')
            val = self.bloque.ejecutar(entorno)
            entorno.imprimirln('goto '+L3+';')
            entorno.imprimirln(L2+'://FALSO')
            if self.sino != None:
                val  = self.sino.ejecutar(entorno)
            entorno.imprimirln(L3+'://FALSO')
        else:
            '''
            Tenemos etiquetas.
            '''                              
            L3=global_utils.generarEtiqueta() 
            entorno.imprimirln(valor_condicion.lv+'://Verdadero')
            val = self.bloque.ejecutar(entorno)
            entorno.imprimirln('goto '+L3+';')
            entorno.imprimirln(valor_condicion.lf+'://FALSO')
            if self.sino != None:
                val  = self.sino.ejecutar(entorno)
            entorno.imprimirln(L3+'://FALSO')                         

class While(Instruccion):
    def __init__(self, expresion, bloque, linea, columna):
        self.expresion = expresion
        self.bloque = bloque         
        self.linea = linea 
        self.columna = columna  

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, 'while')
        grafo.edge(padre, id) 
        self.expresion.graficar(id, grafo)
        self.bloque.graficar(id, grafo)
    
    def ejecutar(self, entorno):
        tipo_tmp = self.expresion.getTipo(entorno)
        if tipo_tmp is None:
            global_utils.registrySemanticError('while', 'Valor inválido de la expresión condicional.', self.linea, self.columna) 
            return  
        if tipo_tmp.esError():
            global_utils.registrySemanticError('while', 'Valor inválido de la expresión condicional.', self.linea, self.columna)
            return                   

        L0=global_utils.generarEtiqueta()
        entorno.imprimirln(L0+'://Ciclo')
        valor_condicion = self.expresion.getValor(entorno)        
        if isinstance(valor_condicion, (int, str)):
            L1=global_utils.generarEtiqueta()
            L2=global_utils.generarEtiqueta()
            L3=global_utils.generarEtiqueta()
            entorno.imprimirln('if('+str(valor_condicion)+'==1){goto '+L1+';}')
            entorno.imprimirln('goto '+L2+';')
            entorno.imprimirln(L1+'://Verdadero')
            val = self.bloque.ejecutar(entorno)
            entorno.imprimirln('goto '+L0+';')
            entorno.imprimirln(L2+'://FALSO')

        else:
            '''
            Tenemos etiquetas.
            '''                              
            L3=global_utils.generarEtiqueta() 
            entorno.imprimirln(valor_condicion.lv+'://Verdadero')
            val = self.bloque.ejecutar(entorno)
            entorno.imprimirln('goto '+L0+';')
            entorno.imprimirln(valor_condicion.lf+'://FALSO')            

class For(Instruccion):
    def __init__(self, id, expresion, bloque, linea, columna ):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        self.bloque = bloque

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))   
        grafo.node(id, 'for')
        grafo.edge(padre, id)
        grafo.node(id+self.id,'[id] ' +self.id)
        grafo.edge(id,id+self.id) 
        self.expresion.graficar(id, grafo)
        self.bloque.graficar(id, grafo)             
    
    def ejecutar(self, entorno):
        if isinstance(self.expresion, Rango):
            tipo_tmp = self.expresion.getTipo(entorno)
            if not tipo_tmp.esError():
                variableAux = Simbolo(self.id, Tipo(TipoPrimitivo.ENTERO),0,0)
                variableAux.posicion = -1
                entorno.insertSimbolo(variableAux)
                if(variableAux.posicion == -1 ):
                    '''
                    Existe la variable                
                    '''
                    variableAux = entorno.getSimbolo(self.id)

                valor_condicion = self.expresion.getValor(entorno)        
                L0=global_utils.generarEtiqueta()
                L1=global_utils.generarEtiqueta()
                L2=global_utils.generarEtiqueta()
                L3=global_utils.generarEtiqueta()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()                
                entorno.imprimirln(t1+'='+str(valor_condicion.valorI)+';')
                entorno.imprimirln(t2+'='+str(valor_condicion.valorD)+';')                
                entorno.imprimirln(L1+':')
                entorno.imprimirln(t3+'=P+'+str(variableAux.posicion)+';//Posicion variable '+self.id)
                entorno.imprimirln('stack[int('+t3+')]='+t1+';')
                entorno.imprimirln('if('+t1+'<='+t2+'){goto '+L2+';} // Verdadero')
                entorno.imprimirln('goto '+L3+';//Salida')
                entorno.imprimirln(L2+':')
                valor = self.bloque.ejecutar(entorno)
                entorno.imprimirln(t1+'='+t1+'+1;')
                entorno.imprimirln('goto '+L1+';')
                entorno.imprimirln(L3+':')                                          
        else:
            tipo_tmp = self.expresion.getTipo(entorno)            
            if tipo_tmp is not None:
                #Cadena
                if tipo_tmp.esCadena():
                    valor = self.expresion.getValor(entorno) 
                    entornoLocal = Entorno(None)
                    #Creamos la variable temporal
                    variable = Simbolo(self.id, Tipo(TipoPrimitivo.STRING),'',self.linea, self.columna)
                    entornoLocal.insertSimbolo(variable)
                    for i in valor:
                            variable.valor = i
                            resultado_ejecucion = self.bloque.ejecutar(entornoLocal)
                            if resultado_ejecucion is not None:
                                if isinstance(resultado_ejecucion, Break):
                                    return resultado_ejecucion
                                if isinstance(resultado_ejecucion, Continue):
                                    return resultado_ejecucion
                #Arrelgo
                if tipo_tmp.esArreglo():
                    # Esto nos devuelve un arreglo
                    valor = self.expresion.getValor(entorno)                                                            
                    entornoLocal = Entorno(None)
                    #Creamos la variable temporal                                           
                    simbolo = Simbolo(self.id, None, None, self.linea, self.columna)
                    entornoLocal.insertSimbolo(simbolo)
                    for i in valor:       
                        tipo_tmp = i.tipo
                        if tipo_tmp is not None:
                            valor_tmp = i.valor
                            simbolo.valor = valor_tmp
                            simbolo.tipo = tipo_tmp                                                 
                            resultado_ejecucion = self.bloque.ejecutar(entornoLocal)
                            if resultado_ejecucion is not None:
                                if isinstance(resultado_ejecucion, Break):
                                    return resultado_ejecucion
                                if isinstance(resultado_ejecucion, Continue):
                                    return resultado_ejecucion                    
                        
class Break(Instruccion):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'break')     
        grafo.edge(padre, id)
    
    def ejecutar(self, entorno):
        return self

class Continue(Instruccion):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id,'continue') 
        grafo.edge(padre, id)
              
    
    def ejecutar(self, entorno):
        return self

class Retorno(Instruccion):
    def __init__(self,expresion, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'retorno')
        grafo.edge(padre, id) 
        self.expresion.graficar(id, grafo)
              
    
    def ejecutar(self, entorno):
        if self.expresion is None:
            return self
        tipo_valor = self.expresion.getTipo(entorno)
        if tipo_valor is not None:
            if not tipo_valor.esError():
                '''
                t0=P+0; // Direccion retorno
                stack[int(t0)]=str(valor_tmp);//Valor de retorno
                '''
                t0=global_utils.generarTemporal()
                entorno.imprimirln(t0+'=P+0; // Direccion retorno')
                valor_tmp = self.expresion.getValor(entorno)
                entorno.imprimirln('stack[int('+t0+')]='+str(valor_tmp)+';//Valor de retorno')  
                entorno.imprimirln('goto '+global_utils.Salida()+';')  
                #return self
            else:
                global_utils.registrySemanticError('return', 'valor de retorno inválido. Verifique variables', self.linea, self.columna)            

class Funcion(Instruccion):
    def __init__(self, nombre, parametros_formales, instrucciones, tipo, linea, columna):
        self.id = nombre
        self.parametros_formales = parametros_formales
        self.instrucciones = instrucciones 
        self.linea = linea
        self.columna = columna 
        self.tipo = tipo

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, '[Dec] Funcion [ID]' + self.id)      
        grafo.edge(padre, id)
        if self.parametros_formales is not None:
            for i in self.parametros_formales:
                i.graficar(id, grafo)
        if self.instrucciones is not None:
            self.instrucciones.graficar(id, grafo)


    def ejecutar(self, entorno):
        # Creamos el símbolo de tipo funcion
        etiquetaSalida=global_utils.generarEtiqueta()
        global_utils.establecerSalida(etiquetaSalida)
        nombre = self.id 
        if self.parametros_formales is not None:
            for i in self.parametros_formales:
                nombre = nombre +'_var'
        self.id = nombre
        entorno.imprimirln('func '+self.id +'() {')
        funcion = FuncionSimbolo(self.id, self.parametros_formales, self.instrucciones, self.linea, self.columna)
        funcion.entorno = Entorno(entorno)
        nuevo_simbolo = Simbolo('retorno', Tipo(TipoPrimitivo.DINAMICO), self.linea, self.columna)
        funcion.entorno.tabla.registrarSimbolo(nuevo_simbolo)
        if self.parametros_formales is not None:
            for i in self.parametros_formales:                
                if(i.tipo is not None):
                    nuevo_simbolo = Simbolo(i.id, i.tipo, i.linea, i.columna)                    
                    funcion.entorno.tabla.registrarSimbolo(nuevo_simbolo)
        entorno.insertSimbolo(funcion)  
        global_utils.apilarMetodo(funcion.id)
        funcion.tipo = self.tipo              
        self.instrucciones.ejecutar(funcion.entorno)
        global_utils.desapilarMetodo()
        entorno.imprimirln('goto '+etiquetaSalida+';')
        entorno.imprimirln(etiquetaSalida+':')
        '''
        self.instrucciones = self.instrucciones.instrucciones
        #Ejecutamos las instruccioens
        
        for inst in self.instrucciones:
            if isinstance(inst, Break):
                pass
            elif isinstance(inst, Continue):
                pass
            elif isinstance(inst, Retorno):
                inst.ejecutar(funcion.entorno)
            else:
                if isinstance(inst, Instruccion):
                    val = inst.ejecutar(funcion.entorno)
                    if val is not None:
                        if isinstance(val, Break):
                            pass
                            #return val
                        if isinstance(val, Continue):
                            pass
                            #return val
                        #return val
                elif isinstance(inst, Expresion):
                    val = inst.getValor(funcion.entorno)
                    if val is not None:
                        if isinstance(val, Break):
                            return val
                        if isinstance(val, Continue):
                            return val
        '''
                     


        entorno.imprimirln('}')

## Expresion -----------------------------------------------------

class Suma(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'suma')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        if tipoI== None or tipoD == None:
            global_utils.registrySemanticError('+','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR) 

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)                      

        if(tipoI.esCadena() or tipoD.esCadena()):        
            global_utils.registrySemanticError('+',' No es posible realizar la operación ' + tipoI.getNombre() + " + " + tipoD.getNombre() , self.linea, self.columna)
            return Tipo(TipoPrimitivo.ERROR)
        if(tipoI.esFloat() or tipoD.esFloat()):
            return Tipo(TipoPrimitivo.FLOAT)
        return Tipo(TipoPrimitivo.ENTERO)
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)

        if tipo_actual.esError():
            return None

        valorI = self.expresionI.getValor(entorno)
        valorD = self.expresionD.getValor(entorno)

        valorI = str(valorI)
        valorD = str(valorD)

        if tipo_actual.esFloat():
            valor = global_utils.generarTemporal()
            self.valor = valor
            entorno.tabla.imprimirln(valor + ' = '+ valorI + '+' + valorD +';')
            return self.valor
            
        if tipo_actual.esEntero():                        
            valor = global_utils.generarTemporal()
            self.valor = valor
            entorno.tabla.imprimirln(valor + ' = '+ valorI + '+' + valorD+';')
            return self.valor        
        return None

class Concatenacion(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'concatenacion')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)              
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        
        if tipoI == None or tipoD == None :
            global_utils.registrySemanticError('Concatenación','Error al realizar la conctaneación, se ha recibido una variable no declarada.' , self.linea, self.columna)
            return Tipo(TipoPrimitivo.ERROR)  

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.STRING)                       

        if tipoI.esError() or tipoD.esError():
            return Tipo(TipoPrimitivo.ERROR)
        return Tipo(TipoPrimitivo.STRING)
    
    def getValor(self, entorno):
        cadena = ''
        tipo_tmp = self.getTipo(entorno)        
        if tipo_tmp.esError():
            return None
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        
        ## Operador izquierdo
        if tipoI.esCadena():
            valorI = self.expresionI.getValor(entorno)

        if tipoI.esBool():
            valorI = self.expresionI.getValor(entorno)
            if isinstance(valorI, int) or isinstance(valorI, str):
                '''
                t0=P+size() // Simulacion de cambio de entorno
                t1=t0+1  // dirección parámetro 1
                stack[int(t1)]=valorI // paso de parámetro
                P=P+size()   // Cambio de entorno
                IntToString_Nativa()
                P=P-size()  // Retomar entorno
                t2=t0+0 // Dirección valor de retorno
                t3=stack[t2] // Valor de retorno
                '''            
                t0 = global_utils.generarTemporal()
                t1 = global_utils.generarTemporal()
                t2 = global_utils.generarTemporal()            
                t3 = global_utils.generarTemporal()   
                valorI = self.expresionI.getValor(entorno)         
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno()) +';// Simulacion de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+1;// dirección parámetro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';// paso de parámetro')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                if tipoI.esEntero():
                    entorno.imprimirln('IntToString_Nativa();')
                elif tipoI.esFloat():
                    entorno.imprimirln('FloatToString_Nativa();')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
                entorno.imprimirln(t2+'='+t0+'+0;// Dirección valor de retorno')
                entorno.imprimirln(t3+'=stack[int('+t2+')];// Valor de retorno')                        
                valorI = t3
            else:
                '''
                if()
                '''



        if tipoI.esNumerico():
            '''
            t0=P+size() // Simulacion de cambio de entorno
            t1=t0+1  // dirección parámetro 1
            stack[int(t1)]=valorI // paso de parámetro
            P=P+size()   // Cambio de entorno
            IntToString_Nativa()
            P=P-size()  // Retomar entorno
            t2=t0+0 // Dirección valor de retorno
            t3=stack[t2] // Valor de retorno
            '''            
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()
            t2 = global_utils.generarTemporal()            
            t3 = global_utils.generarTemporal()   
            valorI = self.expresionI.getValor(entorno)         
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno()) +';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// dirección parámetro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';// paso de parámetro')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            if tipoI.esEntero():
                entorno.imprimirln('IntToString_Nativa();')
            elif tipoI.esFloat():
                entorno.imprimirln('FloatToString_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
            entorno.imprimirln(t2+'='+t0+'+0;// Dirección valor de retorno')
            entorno.imprimirln(t3+'=stack[int('+t2+')];// Valor de retorno')                        
            valorI = t3
          


        ## Operador derecho
        if tipoD.esCadena() or tipoD.esBool():
            valorD = self.expresionD.getValor(entorno)

        if tipoD.esNumerico():
            '''
            t0=P+size() // Simulacion de cambio de entorno
            t1=t0+1  // dirección parámetro 1
            stack[int(t1)]=valorI // paso de parámetro
            P=P+size()   // Cambio de entorno
            IntToString_Nativa()
            P=P-size()  // Retomar entorno
            t2=t0+0 // Dirección valor de retorno
            t3=stack[t2] // Valor de retorno
            '''
            valorD = self.expresionD.getValor(entorno)
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()
            t2 = global_utils.generarTemporal()            
            t3 = global_utils.generarTemporal()            
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno()) +';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// dirección parámetro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(valorD)+';// paso de parámetro')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            if tipoD.esEntero():
                entorno.imprimirln('IntToString_Nativa();')
            elif tipoD.esFloat():
                entorno.imprimirln('FloatToString_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
            entorno.imprimirln(t2+'='+t0+'+0;// Dirección valor de retorno')
            entorno.imprimirln(t3+'=stack[int('+t2+')];// Valor de retorno')                        
            valorD = t3   


                  

        t0 = global_utils.generarTemporal()
        t1 = global_utils.generarTemporal()
        t2 = global_utils.generarTemporal()
        t3 = global_utils.generarTemporal()
        t4 = global_utils.generarTemporal()
        
        entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
        entorno.imprimirln(t1+'='+t0+'+1;// Direccion primer parametro')
        entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';')
        entorno.imprimirln(t2+'='+t0+'+2;// Direccion segundo parámetro')
        entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+';')
        entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';')
        entorno.imprimirln('concatenar_Nativa();')
        entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';')
        entorno.imprimirln(t3+'='+t0+'+0;// Direccion retorno')
        entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')
        self.valor = t4
        return self.valor                                       

class Resta(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'resta')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)                
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        if tipoI== None or tipoD == None:
            global_utils.registrySemanticError('-','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR) 

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)                      

        if(tipoI.esCadena() or tipoD.esCadena()):        
            global_utils.registrySemanticError('-',' No es posible realizar la operación ' + tipoI.getNombre() + " - " + tipoD.getNombre() , self.linea, self.columna)
            return Tipo(TipoPrimitivo.ERROR)
        if(tipoI.esFloat() or tipoD.esFloat()):
            return Tipo(TipoPrimitivo.FLOAT)
        return Tipo(TipoPrimitivo.ENTERO)
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)

        if tipo_actual.esError():
            return None

        valorI = self.expresionI.getValor(entorno)
        valorD = self.expresionD.getValor(entorno)

        valorI = str(valorI)
        valorD = str(valorD)

        if tipo_actual.esFloat():
            valor = global_utils.generarTemporal()
            self.valor = valor
            entorno.tabla.imprimirln(valor + ' = '+ valorI + '-' + valorD)
            return self.valor
            
        if tipo_actual.esEntero():                        
            valor = global_utils.generarTemporal()
            self.valor = valor
            entorno.tabla.imprimirln(valor + ' = '+ valorI + '-' + valorD)
            return self.valor        
        return None


class Multiplicacion(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'multiplicacion')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)                 
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        
        if tipoI== None or tipoD == None:
            global_utils.registrySemanticError('*','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR)            

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)
        
        if(tipoI.esCadena() and tipoD.esCadena()):
            return Tipo(TipoPrimitivo.STRING)

        if (tipoI.esNumerico() and tipoD.esNumerico()):
            if (tipoI.esFloat() or tipoD.esFloat()):
                return Tipo(TipoPrimitivo.FLOAT)
            return Tipo(TipoPrimitivo.ENTERO)

        global_utils.registrySemanticError('*',' No es posible realizar la operación ' + tipoI.getNombre() + " * " + tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)        
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)

        if tipo_actual.esError():
            return None
            
        valorI = self.expresionI.getValor(entorno)
        valorD = self.expresionD.getValor(entorno)

        if tipo_actual.esDinamico():
            tipoI = entorno.obtenerTipo(valorI)
            tipoD = entorno.obtenerTipo(valorD)
            if tipoI.esCadena() or tipoD.esCadena():
                #Hacer concatenacion
                self.valor = str(valorI) + str(valorD)
                return self.valor
            if tipoI.esFloat() or tipoD.esFloat():
                self.valor = float(valorI) * float(valorD)
                return self.valor                
            if tipoI.esEntero() and tipoD.esEntero():
                self.valor = int(valorI) * int(valorD)
                return self.valor   
            global_utils.registrySemanticError('*',' No es posible realizar la operación ' + tipoI.getNombre() + " * " + tipoD.getNombre() , self.linea, self.columna)                             
            return None

        if tipo_actual.esCadena():
            '''
            entorno.imprimirln('t0=P+str(entorno.tamanioEntorno()) // Simulacion de cambio de entorno
            t1=t0+1 // Direccion primer parametro
            stack[t1]=valorI
            t2=t0+2 // Direccion segundo parámetro
            stack[t2]=valorD
            P=P+str(entorno.tamanioEntorno())
            concatenar_Nativa()
            P=P-str(entorno.tamanioEntorno())
            t3=t0+0 // Direccion retorno
            t4=stack[t3] // Valor retorno            
            '''
            t0 = global_utils.generarTemporal()
            t1 = global_utils.generarTemporal()
            t2 = global_utils.generarTemporal()
            t3 = global_utils.generarTemporal()
            t4 = global_utils.generarTemporal()
            
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// Direccion primer parametro')
            entorno.imprimirln('stack[int('+t1+')]='+valorI+';')
            entorno.imprimirln(t2+'='+t0+'+2;// Direccion segundo parámetro')
            entorno.imprimirln('stack[int('+t2+')]='+valorD+';')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';')
            entorno.imprimirln('concatenar_Nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';')
            entorno.imprimirln(t3+'='+t0+'+0;// Direccion retorno')
            entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')
            self.valor = t4
            return self.valor

        if tipo_actual.esFloat():
            self.valor = global_utils.generarTemporal()            
            entorno.imprimirln(self.valor+'='+str(valorI)+'*'+str(valorD)+';');
            return self.valor
            
        if tipo_actual.esEntero():            
            self.valor = global_utils.generarTemporal()            
            entorno.imprimirln(self.valor+'='+str(valorI)+'*'+str(valorD)+';');            
            return self.valor
        
        return None 


class Division(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, 'division')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)                 
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)

        if tipoI== None or tipoD == None:
            global_utils.registrySemanticError('/','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR)         

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)
                
        if (tipoI.esNumerico() and tipoD.esNumerico()):
            return Tipo(TipoPrimitivo.FLOAT)

        global_utils.registrySemanticError('/',' No es posible realizar la operación ' + tipoI.getNombre() + " / " + tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)        
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)
        valorI = self.expresionI.getValor(entorno)
        valorD = self.expresionD.getValor(entorno)        

        if tipo_actual.esError():
            return None

        if tipo_actual.esDinamico():
            tipoI = entorno.obtenerTipo(valorI)
            tipoD = entorno.obtenerTipo(valorD)

            if tipoI.esFloat() or tipoD.esFloat():                
                L1 = global_utils.generarEtiqueta()
                L2 = global_utils.generarEtiqueta()
                L3 = global_utils.generarEtiqueta()
                t0=global_utils.generarTemporal()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                entorno.imprimirln('if('+str(valorD)+'==0){ goto '+L1+';} // Valor inválido')
                entorno.imprimirln('goto '+L2+'; // Valor válido')
                entorno.imprimirln(L1+':')
                mensajeErrorNodo = String('ERROR',0,0)
                mensaje = mensajeErrorNodo.getValor(entorno)
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulacion cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+1;// Direccion parámetro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(mensaje)+';//Paso de parámetro')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_Nativa()')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln(t2+'=0;// Retorno')
                entorno.imprimirln('goto '+L3+';')
                entorno.imprimirln(L2+':')
                entorno.imprimirln(t2+'='+str(valorI)+'/'+str(valorD)+';// Retorno')
                entorno.imprimirln(L3+':') 
                self.valor = t2                               
                return self.valor     

            if tipoI.esEntero() and tipoD.esEntero():
                L1 = global_utils.generarEtiqueta()
                L2 = global_utils.generarEtiqueta()
                L3 = global_utils.generarEtiqueta()
                t0=global_utils.generarTemporal()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                entorno.imprimirln('if('+str(valorD)+'==0){ goto '+L1+';} // Valor inválido')
                entorno.imprimirln('goto '+L2+'; // Valor válido')
                entorno.imprimirln(L1+':')
                mensajeErrorNodo = String('ERROR',0,0)
                mensaje = mensajeErrorNodo.getValor(entorno)
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulacion cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+1;// Direccion parámetro 1')
                entorno.imprimirln('stack[int('+t1+')]='+str(mensaje)+';//Paso de parámetro')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('imprimir_Nativa()')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln(t2+'=0;// Retorno')
                entorno.imprimirln('goto '+L3+';')
                entorno.imprimirln(L2+':')
                entorno.imprimirln(t2+'='+str(valorI)+'/'+str(valorD)+';// Retorno')
                entorno.imprimirln(L3+':') 
                self.valor = t2                               
                return self.valor   
            global_utils.registrySemanticError('/',' No es posible realizar la operación ' + tipoI.getNombre() + " / " + tipoD.getNombre() , self.linea, self.columna)                              
            return None            
            
        if tipo_actual.esFloat():
            L1 = global_utils.generarEtiqueta()
            L2 = global_utils.generarEtiqueta()
            L3 = global_utils.generarEtiqueta()
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            entorno.imprimirln('if('+str(valorD)+'==0){ goto '+L1+';} // Valor inválido')
            entorno.imprimirln('goto '+L2+'; // Valor válido')
            entorno.imprimirln(L1+':')
            mensajeErrorNodo = String('ERROR',0,0)
            mensaje = mensajeErrorNodo.getValor(entorno)
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulacion cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// Direccion parámetro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(mensaje)+';//Paso de parámetro')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('imprimir_Nativa()')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln(t2+'=0;// Retorno')
            entorno.imprimirln('goto '+L3+';')
            entorno.imprimirln(L2+':')
            entorno.imprimirln(t2+'='+str(valorI)+'/'+str(valorD)+';// Retorno')
            entorno.imprimirln(L3+':') 
            self.valor = t2                               
            return self.valor 
            
            
        if tipo_actual.esEntero():            
            L1 = global_utils.generarEtiqueta()
            L2 = global_utils.generarEtiqueta()
            L3 = global_utils.generarEtiqueta()
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            entorno.imprimirln('if('+str(valorD)+'==0){ goto '+L1+';} // Valor inválido')
            entorno.imprimirln('goto '+L2+'; // Valor válido')
            entorno.imprimirln(L1+':')
            mensajeErrorNodo = String('ERROR',0,0)
            mensaje = mensajeErrorNodo.getValor(entorno)
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulacion cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// Direccion parámetro 1')
            entorno.imprimirln('stack[int('+t1+')]='+str(mensaje)+';//Paso de parámetro')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('imprimir_Nativa()')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln(t2+'=0;// Retorno')
            entorno.imprimirln('goto '+L3+';')
            entorno.imprimirln(L2+':')
            entorno.imprimirln(t2+'='+str(valorI)+'/'+str(valorD)+';// Retorno')
            entorno.imprimirln(L3+':') 
            self.valor = t2                               
            return self.valor             
            return self.valor
        
        return None  

class Potencia(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'potencia')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)                
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)

        if tipoI== None or tipoD == None:
            global_utils.registrySemanticError('^','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR)    

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)                 

        if (tipoI.esNumerico() and tipoD.esNumerico()):
            if(tipoI.esFloat() or tipoD.esFloat()):
                return Tipo(TipoPrimitivo.FLOAT)
            else:
                return Tipo(TipoPrimitivo.ENTERO)

        if (tipoI.esCadena() and tipoD.esEntero()):
            return Tipo(TipoPrimitivo.STRING)

        global_utils.registrySemanticError('^',' No es posible realizar la operación ' + tipoI.getNombre() + " ^ " + tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)        
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)
        valorI = self.expresionI.getValor(entorno)
        valorD = self.expresionD.getValor(entorno)
        if tipo_actual.esError():
            return None

        if tipo_actual.esDinamico():
            tipoI = entorno.obtenerTipo(valorI)
            tipoD = entorno.obtenerTipo(valorD)


            '''
            t0=P+entorno.tamanaio();//Simulación de cambio de entorno
            t1=t0+1; // Direccion argumento base
            stack[int(t1)]=str(valorI);// Paso valor base
            t2=t0+2;// Direccion argumento exponente
            stack[int(t2)]=str(valorD);// Paso valor exponente
            P=P+entorno.tamanaio();//Cambio de entorno
            Potencia_nativa();
            P=P-entorno.tamanaio();//Retomar entorno
            t3=t0+0;// Direccion retorno
            t4=stack[int(t3)];// Valor retorno
            ''' 

            if tipoI.esFloat() or tipoD.esFloat():
                t0=global_utils.generarTemporal()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal()                
                
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulación de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+1; // Direccion argumento base')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';// Paso valor base')
                entorno.imprimirln(t2+'='+t0+'+2;// Direccion argumento exponente')
                entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+';// Paso valor exponente')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';//Cambio de entorno')
                entorno.imprimirln('Potencia_nativa();')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';//Retomar entorno')
                entorno.imprimirln(t3+'='+t0+'+0;// Direccion retorno')
                entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')                           
                self.valor =t4
                return self.valor     

            if tipoI.esEntero() and tipoD.esEntero():
                t0=global_utils.generarTemporal()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal()                
                
                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulación de cambio de entorno')
                entorno.imprimirln(t1+'='+t0+'+1; // Direccion argumento base')
                entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';// Paso valor base')
                entorno.imprimirln(t2+'='+t0+'+2;// Direccion argumento exponente')
                entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+';// Paso valor exponente')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';//Cambio de entorno')
                entorno.imprimirln('Potencia_nativa();')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';//Retomar entorno')
                entorno.imprimirln(t3+'='+t0+'+0;// Direccion retorno')
                entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')                           
                self.valor =t4
                return self.valor              
            
            if tipoI.esCadena() and tipoD.esEntero():
                cadena=self.expresionI.getValor(entorno)
                repeticiones=self.expresionD.getValor(entorno)
                '''
                Concatenar hasta que el contador sea igual al contador indicado
                '''
                t0=global_utils.generarTemporal()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal() 
                t5=global_utils.generarTemporal()
                t6=global_utils.generarTemporal()
                L0=global_utils.generarEtiqueta()
                L1=global_utils.generarEtiqueta()
                L2=global_utils.generarEtiqueta()
                L3=global_utils.generarEtiqueta()
                L4=global_utils.generarEtiqueta()
                L5=global_utils.generarEtiqueta()

                entorno.imprimirln('if('+repeticiones+'==0){goto '+L0+';} // Verificar tamaño de la repeticion')
                entorno.imprimirln('goto '+L2+';// Mayor de 0')
                entorno.imprimirln(L0+':')
                nodoCadena=  String("\nERROR, NO SE PUEDE REPETIR UN CADENA UN NÚMERO NEGATIVO DE VECES.",0,0)
                inicioCadena= nodoCadena.getValor(entorno)                
                entorno.imprimirln(t1+'='+inicioCadena+';// Cadena vacia por error')
                entorno.imprimirln('goto '+L3+';')
                entorno.imprimirln(L2+'://Preparando para concatenar')
                entorno.imprimirln(t2+'=0;// Contador')
                entorno.imprimirln(t1+'='+cadena+';// Inicio de cadena')
                entorno.imprimirln(L3+':')
                entorno.imprimirln('if('+t2+'<'+repeticiones+'){ goto '+L4+';}//Otra concatenacion')
                entorno.imprimirln('goto '+L5+';//Fin de la caden')
                entorno.imprimirln(L4+':')
                entorno.imprimirln(t3+'=P+'+str(entorno.tamanioEntorno())+';// Simulación de cambio de entorno')
                entorno.imprimirln(t4+'='+t3+'+1;//Direccion cadena 1')
                entorno.imprimirln('stack[int('+t4+')]='+cadena+';// Paso cadena como primer parametro')
                entorno.imprimirln(t5+'='+t3+'+2;//Direccion cadena 1')
                entorno.imprimirln('stack[int('+t5+')]='+t1+';// Paso cadena como segundo parametro')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('concatenar_Nativa();// Llamar funcion de concatenacion')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
                entorno.imprimirln(t6+'='+t3+'+0;//Direccion retorno')
                entorno.imprimirln(t1+'=stack[int('+t6+')];// Inicio de la nueva cadena')
                entorno.imprimirln(t2+'='+t2+'+1;// Aumento de contador')
                entorno.imprimirln('goto '+L3+';//Otra iteracion')
                entorno.imprimirln(L5+':// Fin cadena')
                return t1;

            return None        
            
        if tipo_actual.esFloat():
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            t4=global_utils.generarTemporal()                
            
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulación de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1; // Direccion argumento base')
            entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';// Paso valor base')
            entorno.imprimirln(t2+'='+t0+'+2;// Direccion argumento exponente')
            entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+';// Paso valor exponente')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';//Cambio de entorno')
            entorno.imprimirln('Potencia_nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';//Retomar entorno')
            entorno.imprimirln(t3+'='+t0+'+0;// Direccion retorno')
            entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')                           
            self.valor =t4
            return self.valor 
            
        if tipo_actual.esEntero():            
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            t4=global_utils.generarTemporal()                
            
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulación de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1; // Direccion argumento base')
            entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+';// Paso valor base')
            entorno.imprimirln(t2+'='+t0+'+2;// Direccion argumento exponente')
            entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+';// Paso valor exponente')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';//Cambio de entorno')
            entorno.imprimirln('Potencia_nativa();')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';//Retomar entorno')
            entorno.imprimirln(t3+'='+t0+'+0;// Direccion retorno')
            entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')                           
            self.valor =t4
            return self.valor 

        if tipo_actual.esCadena():
                cadena=self.expresionI.getValor(entorno)
                repeticiones=self.expresionD.getValor(entorno)
                '''
                Concatenar hasta que el contador sea igual al contador indicado
                '''
                t0=global_utils.generarTemporal()
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal() 
                t5=global_utils.generarTemporal()
                t6=global_utils.generarTemporal()
                L0=global_utils.generarEtiqueta()
                L1=global_utils.generarEtiqueta()
                L2=global_utils.generarEtiqueta()
                L3=global_utils.generarEtiqueta()
                L4=global_utils.generarEtiqueta()
                L5=global_utils.generarEtiqueta()

                entorno.imprimirln('if('+repeticiones+'<0){goto '+L0+';} // Verificar tamaño de la repeticion')
                entorno.imprimirln('goto '+L2+';// Mayor de 0')
                entorno.imprimirln(L0+':')
                nodoCadena=  String("\nERROR, NO SE PUEDE REPETIR UN CADENA UN NÚMERO NEGATIVO DE VECES.",0,0)
                inicioCadena= nodoCadena.getValor(entorno)                
                entorno.imprimirln(t1+'='+inicioCadena+';// Cadena vacia por error')
                entorno.imprimirln('goto '+L3+';')
                entorno.imprimirln(L2+'://Preparando para concatenar')
                entorno.imprimirln(t2+'=1;// Contador')
                entorno.imprimirln(t1+'='+cadena+';// Inicio de cadena')
                entorno.imprimirln(L3+':')
                entorno.imprimirln('if('+t2+'<'+repeticiones+'){ goto '+L4+';}//Otra concatenacion')
                entorno.imprimirln('goto '+L5+';//Fin de la caden')
                entorno.imprimirln(L4+':')
                entorno.imprimirln(t3+'=P+'+str(entorno.tamanioEntorno())+';// Simulación de cambio de entorno')
                entorno.imprimirln(t4+'='+t3+'+1;//Direccion cadena 1')
                entorno.imprimirln('stack[int('+t4+')]='+cadena+';// Paso cadena como primer parametro')
                entorno.imprimirln(t5+'='+t3+'+2;//Direccion cadena 1')
                entorno.imprimirln('stack[int('+t5+')]='+t1+';// Paso cadena como segundo parametro')
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                entorno.imprimirln('concatenar_Nativa();// Llamar funcion de concatenacion')
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
                entorno.imprimirln(t6+'='+t3+'+0;//Direccion retorno')
                entorno.imprimirln(t1+'=stack[int('+t6+')];// Inicio de la nueva cadena')
                entorno.imprimirln(t2+'='+t2+'+1;// Aumento de contador')
                entorno.imprimirln('goto '+L3+';//Otra iteracion')
                entorno.imprimirln(L5+':// Fin cadena')
                return t1;
        
        return None    

class Modulo(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'modulo')  
        grafo.edge(padre,id)
        self.expresionI.graficar(id,grafo)
        self.expresionD.graficar(id,grafo)              
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)

        if tipoI== None or tipoD == None:
            global_utils.registrySemanticError('%','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR) 

        if tipoI.esDinamico() or tipoD.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)               

        if (tipoI.esNumerico() and tipoD.esNumerico()):
            if (tipoI.esFloat() or tipoD.esFloat()):
                return Tipo(TipoPrimitivo.FLOAT)
            return Tipo(TipoPrimitivo.ENTERO)

        global_utils.registrySemanticError('%',' No es posible realizar la operación ' + tipoI.getNombre() + " % " + tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)        
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)

        if tipo_actual.esError():
            return None
            
        valorI = self.expresionI.getValor(entorno)
        valorD = self.expresionD.getValor(entorno)


        if tipo_actual.esDinamico():
            tipoI = entorno.obtenerTipo(valorI)
            tipoD = entorno.obtenerTipo(valorD)

            if tipoI.esFloat() or tipoD.esFloat():                
                t0=global_utils.generarTemporal()                
                t1=global_utils.generarTemporal()  
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal()

                L1=global_utils.generarEtiqueta()
                L2=global_utils.generarEtiqueta()
                L3=global_utils.generarEtiqueta()

                entorno.imprimirln(t0+'='+valorI)
                entorno.imprimirln(t1+'='+valorD) 
                entorno.imprimirln('if('+t0+'<'+t1+'){ goto '+L1+';}')
                entorno.imprimirln('goto '+L2+';')
                entorno.imprimirln(L1+':')
                entorno.imprimirln(t2+'='+t0+';')
                entorno.imprimirln('goto '+L3+';')
                entorno.imprimirln(L2+':')                      
                entorno.imprimirln(t2+'=float64(int('+t0+')%int('+t1+'));')
                entorno.imprimirln(t3+'=float64(int('+t0+'));')
                entorno.imprimirln(t4+'='+t0+'-'+t3+';//Resuido')
                entorno.imprimirln(t2+'='+t2+'+'+t4+';//Resuido')
                entorno.imprimirln(L3+':')
                self.valor = t2
                return self.valor     

            if tipoI.esEntero() and tipoD.esEntero():
                t0=global_utils.generarTemporal()                
                t1=global_utils.generarTemporal()  
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal()

                L1=global_utils.generarEtiqueta()
                L2=global_utils.generarEtiqueta()
                L3=global_utils.generarEtiqueta()

                entorno.imprimirln(t0+'='+valorI)
                entorno.imprimirln(t1+'='+valorD) 
                entorno.imprimirln('if('+t0+'<'+t1+'){ goto '+L1+';}')
                entorno.imprimirln('goto '+L2+';')
                entorno.imprimirln(L1+':')
                entorno.imprimirln(t2+'='+t0+';')
                entorno.imprimirln('goto '+L3+';')
                entorno.imprimirln(L2+':')                      
                entorno.imprimirln(t2+'=float64(int('+t0+')%int('+t1+'));')
                entorno.imprimirln(t3+'=float64(int('+t0+'));')
                entorno.imprimirln(t4+'='+t0+'-'+t3+';//Resuido')
                entorno.imprimirln(t2+'='+t2+'+'+t4+';//Resuido')
                entorno.imprimirln(L3+':')
                self.valor = t2
                return self.valor 
            global_utils.registrySemanticError('%',' No es posible realizar la operación ' + tipoI.getNombre() + " % " + tipoD.getNombre() , self.linea, self.columna)                                                                  
            return None          

        if tipo_actual.esFloat():            
            t0=global_utils.generarTemporal()                
            t1=global_utils.generarTemporal()  
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            t4=global_utils.generarTemporal()

            L1=global_utils.generarEtiqueta()
            L2=global_utils.generarEtiqueta()
            L3=global_utils.generarEtiqueta()

            entorno.imprimirln(t0+'='+valorI)
            entorno.imprimirln(t1+'='+valorD) 
            entorno.imprimirln('if('+t0+'<'+t1+'){ goto '+L1+';}')
            entorno.imprimirln('goto '+L2+';')
            entorno.imprimirln(L1+':')
            entorno.imprimirln(t2+'='+t0+';')
            entorno.imprimirln('goto '+L3+';')
            entorno.imprimirln(L2+':')                      
            entorno.imprimirln(t2+'=float64(int('+t0+')%int('+t1+'));')
            entorno.imprimirln(t3+'=float64(int('+t0+'));')
            entorno.imprimirln(t4+'='+t0+'-'+t3+';//Resuido')
            entorno.imprimirln(t2+'='+t2+'+'+t4+';//Resuido')
            entorno.imprimirln(L3+':')
            self.valor = t2
            return self.valor 
            
        if tipo_actual.esEntero():                        
            t0=global_utils.generarTemporal()                
            t1=global_utils.generarTemporal()  
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            t4=global_utils.generarTemporal()

            L1=global_utils.generarEtiqueta()
            L2=global_utils.generarEtiqueta()
            L3=global_utils.generarEtiqueta()

            entorno.imprimirln(t0+'='+valorI)
            entorno.imprimirln(t1+'='+valorD) 
            entorno.imprimirln('if('+t0+'<'+t1+'){ goto '+L1+';}')
            entorno.imprimirln('goto '+L2+';')
            entorno.imprimirln(L1+':')
            entorno.imprimirln(t2+'='+t0+';')
            entorno.imprimirln('goto '+L3+';')
            entorno.imprimirln(L2+':')                      
            entorno.imprimirln(t2+'=float64(int('+t0+')%int('+t1+'));')
            entorno.imprimirln(t3+'=float64(int('+t0+'));')
            entorno.imprimirln(t4+'='+t0+'-'+t3+';//Resuido')
            entorno.imprimirln(t2+'='+t2+'+'+t4+';//Resuido')
            entorno.imprimirln(L3+':')
            self.valor = t2
            return self.valor 
        
        return None                                  
        
class Negativo(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion        
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'negativo')  
        grafo.edge(padre,id)
        self.expresion.graficar(id,grafo)                       
    
    def getTipo(self, entorno):
        tipo = self.expresion.getTipo(entorno)  

        if tipo== None:
            global_utils.registrySemanticError('-','Se ha recibido una variable no declarada.' , self.linea, self.columna)  
            return Tipo(TipoPrimitivo.ERROR)   
            
        if tipo.esDinamico():
            return tipo               

        if tipo.esNumerico():
            if tipo.esFloat():
                return Tipo(TipoPrimitivo.FLOAT)
            return Tipo(TipoPrimitivo.ENTERO)

        global_utils.registrySemanticError('-',' No es posible realizar la operación (-) ' + tipo.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)        
    
    def getValor(self, entorno):
        tipo_actual = self.getTipo(entorno)

        if tipo_actual.esError():
            return None
        
        if tipo_actual.esDinamico():
            self.valor = self.expresion.getValor(entorno)
            tipo_real = entorno.obtenerTipo(entorno)    
            if tipo_real.esFloat() or tipo_real.esEntero():                
                valor = global_utils.generarTemporal()                
                entorno.tabla.imprimirln(valor + ' = '+ str(self.valor) + '* -1;')
                self.valor = valor
                return self.valor  
                 
            global_utils.registrySemanticError('-',' No es posible realizar la operación (-) ' + tipo_real.getNombre() , self.linea, self.columna)
            return None         
            
        self.valor = self.expresion.getValor(entorno)
        if tipo_actual.esFloat() or tipo_actual.esEntero():                        
            valor = global_utils.generarTemporal()                
            entorno.tabla.imprimirln(valor + ' = '+ str(self.valor) + '* -1;')
            self.valor = valor
            return self.valor 
        return None  



class Nulo(Expresion):
    def __init__(self, linea, columna):        
        self.linea = linea
        self.columna = columna
        self.valor = None
        self.tipo = Tipo(TipoPrimitivo.NULO,'')

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '[Exp] Nulo')  
        grafo.edge(padre,id)                        
    
    def getValor(self, entorno):
        return self.valor
    
    def getTipo(self, entorno):
        return self.tipo

class Variable(Expresion):
    def __init__(self, id, linea, columna):
        self.id = id 
        self.linea = linea 
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, '[Exp] Variable' + self.id)  
        grafo.edge(padre,id)                 
    
    def getTipo(self, entorno):
        tmp_simbolo = entorno.getSimbolo(self.id)
        if tmp_simbolo is None:
            global_utils.registrySemanticError(self.id,'No se ha encontrado la variable solicitada ' +self.id , self.linea, self.columna)
            return None
        return tmp_simbolo.tipo

    def getValor(self, entorno):
        simbolo = entorno.getSimbolo(self.id)
        if simbolo is None:
            global_utils.registrySemanticError(self.id,'No se ha encontrado la variable solicitada ' +self.id , self.linea, self.columna)
            return None
        '''
        t0=P+simbolo.posicion // Direccion simbolo.id
        t1=stack[t0]  // valor simbolo.id
        '''
        if simbolo.tipo.esNumerico() or simbolo.tipo.esBool() or simbolo.tipo.esCadena():
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            entorno.imprimirln(t0+'=P+'+str(simbolo.posicion)+';// Direccion ' + simbolo.id)
            entorno.imprimirln(t1+'=stack[int('+t0+')];// Valor '+ simbolo.id)
            return t1

class Entero(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = str(valor)
        self.linea = linea
        self.columna = columna
        self.tipo = Tipo(TipoPrimitivo.ENTERO,'')

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, '[Exp] Entero' + str(self.valor))  
        grafo.edge(padre,id)                
    
    def getValor(self, entorno):
        return self.valor
    
    def getTipo(self, entorno):
        return self.tipo        

class Float(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = str(valor)
        self.linea = linea
        self.columna = columna
        self.tipo = Tipo(TipoPrimitivo.FLOAT,'')
    

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '[Exp] Float' + str(self.valor))  
        grafo.edge(padre,id)         

    def getValor(self, entorno):
        return self.valor
    
    def getTipo(self, entorno):
        return self.tipo


class Bool(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.tipo = Tipo(TipoPrimitivo.BOOL,'')
        
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, '[Exp] Bool' + str(self.valor))  
        grafo.edge(padre,id)                   
    
    def getValor(self, entorno):
        if self.valor:
            return 1
        return 0
    
    def getTipo(self, entorno):
        return self.tipo


class Char(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.tipo = Tipo(TipoPrimitivo.CHAR,'')

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, '[Exp] Char' + str(self.valor))  
        grafo.edge(padre,id)                     
    
    def getValor(self, entorno):
        return self.valor
    
    def getTipo(self, entorno):
        return self.tipo

class String(Expresion):
    def __init__(self, valor, linea, columna):
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.tipo = Tipo(TipoPrimitivo.STRING,'')

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, '[Exp] String' + str(self.valor))  
        grafo.edge(padre,id)                    
    
    def getValor(self, entorno):
        '''
        t0 = H 
        t1 = t0
        H = H + (len(self.valor)+1)
        heap[t1] = caracter
        entorno.tabla.imprimirln(valor + ' = '+ valorI + '+' + valorD)
        '''
        t0 = global_utils.generarTemporal()                   
        t1 = global_utils.generarTemporal() 
        entorno.tabla.imprimirln(t0+'=H;')
        entorno.tabla.imprimirln(t1+'='+t0+';')
        entorno.tabla.imprimirln('H=H+'+str(len(self.valor)+1)+';')
        for car in str(self.valor):
            entorno.tabla.imprimirln('heap[int('+t1+')]='+ str(ord(car))+';//' + car)
            entorno.tabla.imprimirln(t1+'='+t1+'+1;')
        entorno.tabla.imprimirln('heap[int('+t1+')]='+str(global_utils.obtenerNulo())+';// Fin cadena')
        return t0
    
    def getTipo(self, entorno):
        return self.tipo        

class Uppercase(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'uppercase')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)          
    
    def getTipo(self, entorno):
        return Tipo(TipoPrimitivo.STRING)
        '''
        tipo_tmp = self.expresion.getTipo(entorno)
        if tipo_tmp.esCadena():
            return Tipo(TipoPrimitivo.STRING)
        return Tipo(TipoPrimitivo.ERROR)
        '''
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esCadena():
            cadena  = self.expresion.getValor(entorno)
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()        
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulación de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// Direccion parametro 1')
            entorno.imprimirln('stack[int('+str(t1)+')]='+str(cadena)+';//Paso de parametro 1')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('uppercase_Nativa()')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
            entorno.imprimirln(t2+'='+t0+'+0;// Direccion retorno')
            entorno.imprimirln(t3+'=stack[int('+t2+')];// Valor de retorno')                                
            return t3
        return None

class Lowercase(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'lowercase')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)                  
    
    def getTipo(self, entorno):
        return Tipo(TipoPrimitivo.STRING)
        '''
        tipo_tmp = self.expresion.getTipo(entorno)
        if tipo_tmp.esCadena():
            return Tipo(TipoPrimitivo.STRING)
        global_utils.registrySemanticError('lowercase','Esta primitiva solo acepta valores de tipo Cadena, se ha recibido un valor de tipo' + tipo_tmp.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)
        '''
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esCadena():
            cadena  = self.expresion.getValor(entorno)
            t0=global_utils.generarTemporal()
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()        
            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulación de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// Direccion parametro 1')
            entorno.imprimirln('stack[int('+str(t1)+')]='+str(cadena)+';//Paso de parametro 1')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            entorno.imprimirln('lowercase_Nativa()')
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
            entorno.imprimirln(t2+'='+t0+'+0;// Direccion retorno')
            entorno.imprimirln(t3+'=stack[int('+t2+')];// Valor de retorno')                                
            return t3
        return None

class Log10(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columan = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))   
        grafo.node(id, 'log10')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)              
    
    def getTipo(self, entorno):
        tipo_tmp = self.expresion.getTipo(entorno)
        if tipo_tmp.esNumerico():
            return tipo_tmp
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esNumerico():
            valor = self.expresion.getValor(entorno)            
            self.valor = math.log10(valor)
            return self.valor
        return None
        

class Log(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columan = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'log')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)              
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        if tipoI.esNumerico() and tipoD.esNumerico():
            return tipoI
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esNumerico():
            valorI = self.expresionI.getValor(entorno)
            valorD = self.expresionD.getValor(entorno)            
            self.valor = math.log(valorD, valorI)
            return self.valor
        return None

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))        
                
class Sin(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion        
        self.linea = linea
        self.columan = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, 'sin')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)                 
    
    def getTipo(self, entorno):
        tipo = self.expresion.getTipo(entorno)        
        if tipo.esNumerico():
            return tipo
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esNumerico():
            valor = self.expresion.getValor(entorno)            
            self.valor = math.sin(valor)
            return self.valor
        return None
                

class Cos(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion        
        self.linea = linea
        self.columan = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'cos')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)                 
    
    def getTipo(self, entorno):
        tipo = self.expresion.getTipo(entorno)        
        if tipo.esNumerico():
            return tipo
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esNumerico():
            valor = self.expresion.getValor(entorno)            
            self.valor = math.cos(valor)
            return self.valor
        return None                

class Tan(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion        
        self.linea = linea
        self.columan = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'tan')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)               
    
    def getTipo(self, entorno):
        tipo = self.expresion.getTipo(entorno)        
        if tipo.esNumerico():
            return tipo
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esNumerico():
            valor = self.expresion.getValor(entorno)            
            self.valor = math.tan(valor)
            return self.valor
        return None     

class Sqrt(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion        
        self.linea = linea
        self.columan = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, 'sqrt')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)                
    
    def getTipo(self, entorno):
        tipo = self.expresion.getTipo(entorno)        
        if tipo.esNumerico():
            return tipo
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esNumerico():
            valor = self.expresion.getValor(entorno)            
            self.valor = math.sqrt(valor)
            return self.valor
        return None     

## Operaciones Relacionales -----------------------------------------------------------------------------------------------------------------
class Mayor(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'mayor')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo) 
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionI.getTipo(entorno)
        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.esCadena() and tipoD.esCadena():
            return Tipo(TipoPrimitivo.BOOL)
        global_utils.registrySemanticError('>','No es posible realizar la operación ' + tipoI.getNombre() + ' > '+ tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)

    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        valorI = self.expresionI.getValor(entorno)      
        valorD = self.expresionD.getValor(entorno)
        if tipo_tmp.esBool():            
            self.lv=global_utils.generarEtiqueta()
            self.lf=global_utils.generarEtiqueta()              
            entorno.imprimirln('if('+str(valorI)+'>'+str(valorD)+'){ goto '+self.lv+';} // Lv')
            entorno.imprimirln('goto '+self.lf+'; // Lf')
            return self

class MayorIgual(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'mayor-igual')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)                
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionI.getTipo(entorno)
        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.esCadena() and tipoD.esCadena():
            return Tipo(TipoPrimitivo.BOOL)
        global_utils.registrySemanticError('>=','No es posible realizar la operación ' + tipoI.getNombre() + ' >= '+ tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)

    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        valorI = self.expresionI.getValor(entorno)      
        valorD = self.expresionD.getValor(entorno)
        if tipo_tmp.esBool():            
            self.lv=global_utils.generarEtiqueta()
            self.lf=global_utils.generarEtiqueta()              
            entorno.imprimirln('if('+str(valorI)+'>='+str(valorD)+'){ goto '+self.lv+';} // Lv')
            entorno.imprimirln('goto '+self.lf+'; // Lf')
            return self                       

class Menor(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'menor')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)                
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionI.getTipo(entorno)
        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.esCadena() and tipoD.esCadena():
            return Tipo(TipoPrimitivo.BOOL)
        global_utils.registrySemanticError('<','No es posible realizar la operación ' + tipoI.getNombre() + ' < '+ tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)

    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        valorI = self.expresionI.getValor(entorno)      
        valorD = self.expresionD.getValor(entorno)
        if tipo_tmp.esBool():            
            self.lv=global_utils.generarEtiqueta()
            self.lf=global_utils.generarEtiqueta()              
            entorno.imprimirln('if('+str(valorI)+'<'+str(valorD)+'){ goto '+self.lv+';} // Lv')
            entorno.imprimirln('goto '+self.lf+'; // Lf')
            return self             


class MenorIgual(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'menor-igual')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)                
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionI.getTipo(entorno)
        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.esCadena() and tipoD.esCadena():
            return Tipo(TipoPrimitivo.BOOL)            
        global_utils.registrySemanticError('<=','No es posible realizar la operación ' + tipoI.getNombre() + ' <= '+ tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)

    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        if tipo_tmp.esBool():
            if esExpresionBasica(self.expresionI) and  esExpresionBasica(self.expresionD):
                valorI = self.expresionI.getValor(entorno)
                valorD = self.expresionD.getValor(entorno)
                self.lv=global_utils.generarEtiqueta()
                self.lf=global_utils.generarEtiqueta()              
                entorno.imprimirln('if('+str(valorI)+'<='+str(valorD)+'){ goto '+self.lv+';} // Lv')
                entorno.imprimirln('goto '+self.lf+'; // Lf')  
                return self              
            else:
                if esRelacional(self.expresionI):
                    valorI = self.expresionI.getValor(entorno)
                    t0=global_utils.generarTemporal()
                    L1=global_utils.generarEtiqueta()
                    entorno.imprimirln(valorI.lv+':') 
                    entorno.imprimirln(t0+'=1;// Valor verdadero') 
                    entorno.imprimirln('goto '+L1+'; // Salida') 
                    entorno.imprimirln(valorI.lf+':') 
                    entorno.imprimirln(t0+'=0;// Valor negativo')
                    entorno.imprimirln(L1+':') 
                    if esExpresionBasica(self.expresionD):
                        valorD = self.expresionD.getValor(entorno)
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+t0+'=='+str(valorD)+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self
                    else:
                        valorD = self.expresionD.getValor(entorno)
                        t1=global_utils.generarTemporal()
                        L2=global_utils.generarEtiqueta()
                        entorno.imprimirln(valorD.lv+':') 
                        entorno.imprimirln(t1+'=1;// Valor verdadero') 
                        entorno.imprimirln('goto '+L2+'; // Salida') 
                        entorno.imprimirln(valorD.lf+':') 
                        entorno.imprimirln(t1+'=0;// Valor negativo')
                        entorno.imprimirln(L2+':')  
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+t0+'<='+t1+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self 
                else:
                    if isinstance(self.expresionI, String) and isinstance(self.expresionD, String):
                        valorI = self.expresionI.getValor(entorno)
                        valorD = self.expresionD.getValor(entorno)
                        '''
                        t0=P+str(entorno.tamanio());// Simulación de cambio de entorno
                        t1=t0+1; // Direccion cadena 1
                        stack[int(t1)]=str(valorI); // Paso de cadena 1
                        t2=t0+2; // Direccion cadena 2
                        stack[int(t2)]=str(valorD); // Direccion cadena 2
                        P=P+str(entorno.tamanio());// Cambio de entorno
                        CompararCadenas_Nativa(); 
                        P=P-str(entorno.tamanio());// Retomar entorno
                        t3=t0+0; // Direccion retorno
                        t4=stack[int(t3)];// Valor retorno
                        if(t4==1){goto lv;}
                        goto lf;
                        '''
                        t0=global_utils.generarTemporal()
                        t1=global_utils.generarTemporal()
                        t2=global_utils.generarTemporal()
                        t3=global_utils.generarTemporal()
                        t4=global_utils.generarTemporal()
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()                        
                        entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulación de cambio de entorno')
                        entorno.imprimirln(t1+'='+t0+'+1; // Direccion cadena 1')
                        entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+'; // Paso de cadena 1')
                        entorno.imprimirln(t2+'='+t0+'+2; // Direccion cadena 2')
                        entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+'; // Direccion cadena 2')
                        entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                        entorno.imprimirln('ComparacionCadenas_nativa();') 
                        entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
                        entorno.imprimirln(t3+'='+t0+'+0; // Direccion retorno')
                        entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')
                        entorno.imprimirln('if('+t4+'<=1){goto '+self.lv+';}') 
                        entorno.imprimirln('goto '+self.lf+';') 
                        return self
                        
                    else:
                        valorI = self.expresionI.getValor(entorno) 
                        valorD = self.expresionD.getValor(entorno)
                        t2=global_utils.generarTemporal()
                        L3=global_utils.generarEtiqueta()
                        entorno.imprimirln(valorD.lv+':') 
                        entorno.imprimirln(t2+'=1;// Valor verdadero') 
                        entorno.imprimirln('goto '+L3+'; // Salida') 
                        entorno.imprimirln(valorD.lf+':') 
                        entorno.imprimirln(t2+'=0;// Valor negativo')
                        entorno.imprimirln(L3+':')  
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+str(valorI)+'<='+t2+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self            

class Igualigual(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'igual')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)                
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionI.getTipo(entorno)
        if tipoI == None or tipoD == None:
            return Tipo(TipoPrimitivo.ERROR)    
        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.esCadena() and tipoD.esCadena():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.compararTipo(tipoD):
            return Tipo(TipoPrimitivo.BOOL)
        global_utils.registrySemanticError('==','No es posible realizar la operación ' + tipoI.getNombre() + ' == '+ tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)

    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        if tipo_tmp.esBool():
            if esExpresionBasica(self.expresionI) and  esExpresionBasica(self.expresionD):
                valorI = self.expresionI.getValor(entorno)
                valorD = self.expresionD.getValor(entorno)
                self.lv=global_utils.generarEtiqueta()
                self.lf=global_utils.generarEtiqueta()              
                entorno.imprimirln('if('+str(valorI)+'=='+str(valorD)+'){ goto '+self.lv+';} // Lv')
                entorno.imprimirln('goto '+self.lf+'; // Lf')  
                return self              
            else:
                if esRelacional(self.expresionI):
                    valorI = self.expresionI.getValor(entorno)
                    t0=global_utils.generarTemporal()
                    L1=global_utils.generarEtiqueta()
                    entorno.imprimirln(valorI.lv+':') 
                    entorno.imprimirln(t0+'=1;// Valor verdadero') 
                    entorno.imprimirln('goto '+L1+'; // Salida') 
                    entorno.imprimirln(valorI.lf+':') 
                    entorno.imprimirln(t0+'=0;// Valor negativo')
                    entorno.imprimirln(L1+':') 
                    if esExpresionBasica(self.expresionD):
                        valorD = self.expresionD.getValor(entorno)
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+t0+'=='+str(valorD)+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self
                    else:
                        valorD = self.expresionD.getValor(entorno)
                        t1=global_utils.generarTemporal()
                        L2=global_utils.generarEtiqueta()
                        entorno.imprimirln(valorD.lv+':') 
                        entorno.imprimirln(t1+'=1;// Valor verdadero') 
                        entorno.imprimirln('goto '+L2+'; // Salida') 
                        entorno.imprimirln(valorD.lf+':') 
                        entorno.imprimirln(t1+'=0;// Valor negativo')
                        entorno.imprimirln(L2+':')  
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+t0+'=='+t1+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self 
                else:
                    if isinstance(self.expresionI, String) and isinstance(self.expresionD, String):
                        valorI = self.expresionI.getValor(entorno)
                        valorD = self.expresionD.getValor(entorno)
                        '''
                        t0=P+str(entorno.tamanio());// Simulación de cambio de entorno
                        t1=t0+1; // Direccion cadena 1
                        stack[int(t1)]=str(valorI); // Paso de cadena 1
                        t2=t0+2; // Direccion cadena 2
                        stack[int(t2)]=str(valorD); // Direccion cadena 2
                        P=P+str(entorno.tamanio());// Cambio de entorno
                        CompararCadenas_Nativa(); 
                        P=P-str(entorno.tamanio());// Retomar entorno
                        t3=t0+0; // Direccion retorno
                        t4=stack[int(t3)];// Valor retorno
                        if(t4==1){goto lv;}
                        goto lf;
                        '''
                        t0=global_utils.generarTemporal()
                        t1=global_utils.generarTemporal()
                        t2=global_utils.generarTemporal()
                        t3=global_utils.generarTemporal()
                        t4=global_utils.generarTemporal()
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()                        
                        entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';// Simulación de cambio de entorno')
                        entorno.imprimirln(t1+'='+t0+'+1; // Direccion cadena 1')
                        entorno.imprimirln('stack[int('+t1+')]='+str(valorI)+'; // Paso de cadena 1')
                        entorno.imprimirln(t2+'='+t0+'+2; // Direccion cadena 2')
                        entorno.imprimirln('stack[int('+t2+')]='+str(valorD)+'; // Direccion cadena 2')
                        entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                        entorno.imprimirln('ComparacionCadenas_nativa();') 
                        entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
                        entorno.imprimirln(t3+'='+t0+'+0; // Direccion retorno')
                        entorno.imprimirln(t4+'=stack[int('+t3+')];// Valor retorno')
                        entorno.imprimirln('if('+t4+'==1){goto '+self.lv+';}') 
                        entorno.imprimirln('goto '+self.lf+';') 
                        return self
                        
                    else:
                        valorI = self.expresionI.getValor(entorno) 
                        valorD = self.expresionD.getValor(entorno)
                        t2=global_utils.generarTemporal()
                        L3=global_utils.generarEtiqueta()
                        entorno.imprimirln(valorD.lv+':') 
                        entorno.imprimirln(t2+'=1;// Valor verdadero') 
                        entorno.imprimirln('goto '+L3+'; // Salida') 
                        entorno.imprimirln(valorD.lf+':') 
                        entorno.imprimirln(t2+'=0;// Valor negativo')
                        entorno.imprimirln(L3+':')  
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+str(valorI)+'=='+t2+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self 
                              
class Diferente(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'diferente')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)              
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionI.getTipo(entorno)
        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.esCadena() and tipoD.esCadena():
            return Tipo(TipoPrimitivo.BOOL)
        if tipoI.compararTipo(tipoD):
            return Tipo(TipoPrimitivo.BOOL)            
        global_utils.registrySemanticError('!=','No es posible realizar la operación ' + tipoI.getNombre() + ' != '+ tipoD.getNombre() , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)

    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        if tipo_tmp.esBool():
            if esExpresionBasica(self.expresionI) and  esExpresionBasica(self.expresionD):
                valorI = self.expresionI.getValor(entorno)
                valorD = self.expresionD.getValor(entorno)
                self.lv=global_utils.generarEtiqueta()
                self.lf=global_utils.generarEtiqueta()              
                entorno.imprimirln('if('+str(valorI)+'!='+str(valorD)+'){ goto '+self.lv+';} // Lv')
                entorno.imprimirln('goto '+self.lf+'; // Lf')  
                return self              
            else:
                if esRelacional(self.expresionI):
                    valorI = self.expresionI.getValor(entorno)
                    t0=global_utils.generarTemporal()
                    L1=global_utils.generarEtiqueta()
                    entorno.imprimirln(valorI.lv+':') 
                    entorno.imprimirln(t0+'=1;// Valor verdadero') 
                    entorno.imprimirln('goto '+L1+'; // Salida') 
                    entorno.imprimirln(valorI.lf+':') 
                    entorno.imprimirln(t0+'=0;// Valor negativo')
                    entorno.imprimirln(L1+':') 
                    if esExpresionBasica(self.expresionD):
                        valorD = self.expresionD.getValor(entorno)
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+t0+'!='+str(valorD)+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self
                    else:
                        valorD = self.expresionD.getValor(entorno)
                        t1=global_utils.generarTemporal()
                        L2=global_utils.generarEtiqueta()
                        entorno.imprimirln(valorD.lv+':') 
                        entorno.imprimirln(t1+'=1;// Valor verdadero') 
                        entorno.imprimirln('goto '+L2+'; // Salida') 
                        entorno.imprimirln(valorD.lf+':') 
                        entorno.imprimirln(t1+'=0;// Valor negativo')
                        entorno.imprimirln(L2+':')  
                        self.lv=global_utils.generarEtiqueta()
                        self.lf=global_utils.generarEtiqueta()              
                        entorno.imprimirln('if('+t0+'!='+t1+'){ goto '+self.lv+';} // Lv')
                        entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                        return self 
                else:
                    valorI = self.expresionI.getValor(entorno) 
                    valorD = self.expresionD.getValor(entorno)
                    t2=global_utils.generarTemporal()
                    L3=global_utils.generarEtiqueta()
                    entorno.imprimirln(valorD.lv+':') 
                    entorno.imprimirln(t2+'=1;// Valor verdadero') 
                    entorno.imprimirln('goto '+L3+'; // Salida') 
                    entorno.imprimirln(valorD.lf+':') 
                    entorno.imprimirln(t2+'=0;// Valor negativo')
                    entorno.imprimirln(L3+':')  
                    self.lv=global_utils.generarEtiqueta()
                    self.lf=global_utils.generarEtiqueta()              
                    entorno.imprimirln('if('+str(valorI)+'!='+t2+'){ goto '+self.lv+';} // Lv')
                    entorno.imprimirln('goto '+self.lf+'; // Lf')                          
                    return self           

class Or(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI 
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))  
        grafo.node(id, 'OR')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)              
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        if tipoI.esBool() and tipoD.esBool():
            return Tipo(TipoPrimitivo.BOOL)
        return Tipo(TipoPrimitivo.Error)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        if tipo_tmp.esBool():            
            lv=global_utils.generarEtiqueta()
            lf=global_utils.generarEtiqueta()
            L1=global_utils.generarEtiqueta()
            valorI = self.expresionI.getValor(entorno)            
            if isinstance(valorI,int):                
                '''bool || bool'''
                '''
                if(valorI==1){goto L1;}
                goto L2;
                L2:
                if(valorD==1){goto L3;}
                goto L4;
                '''            
                entorno.imprimirln('if('+str(valorI)+'==1){ goto '+lv+';} // Lv')
                entorno.imprimirln('goto '+L1+'; // Lf')
                entorno.imprimirln(L1+':')
                valorD = self.expresionD.getValor(entorno)                                                
                if isinstance(valorD, int):
                    entorno.imprimirln('if('+str(valorD)+'==1){ goto '+lv+';} // Lv')
                    entorno.imprimirln('goto '+lf+'; // Lf')     
                    self.lv=lv
                    self.lf=lf          
                else:
                    self.lv=lv + ':\n' + valorD.lv
                    self.lf=valorD.lf                         
                return self                

            else:                                             
                '''etiqueta || bool'''
                '''
                valorI.lf:
                if(valorD==1){ goto L1;}
                goto L2;
                '''
                L2=global_utils.generarEtiqueta()
                entorno.imprimirln(valorI.lf+': // Lf')
                valorD = self.expresionD.getValor(entorno)
                if isinstance(valorD, int):
                    entorno.imprimirln('if('+str(valorD)+'==1){ goto '+lv+';} // Lv')
                    entorno.imprimirln('goto '+lf+'; // Lf')     
                    self.lv=valorI.lv + ':\n' +lv
                    self.lf=lf          
                else:
                    self.lv=valorI.lv + ':\n' + valorD.lv
                    self.lf=valorD.lf
                return self                 

class And(Expresion):
    def __init__(self, expresionI, expresionD, linea, columna):
        self.expresionI = expresionI 
        self.expresionD = expresionD
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'AND')  
        grafo.edge(padre,id)      
        self.expresionI.graficar(id, grafo)               
        self.expresionD.graficar(id, grafo)             
    
    def getTipo(self, entorno):
        tipoI = self.expresionI.getTipo(entorno)
        tipoD = self.expresionD.getTipo(entorno)
        if tipoI.esBool() and tipoD.esBool():
            return Tipo(TipoPrimitivo.BOOL)
        return Tipo(TipoPrimitivo.Error)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError() or tipo_tmp.esCadena() or tipo_tmp.esNumerico():
            return None
        if tipo_tmp.esBool():            
            lv=global_utils.generarEtiqueta()
            lf=global_utils.generarEtiqueta()
            L1=global_utils.generarEtiqueta()
            valorI = self.expresionI.getValor(entorno)            
            if isinstance(valorI,int) or isinstance(valorI,str):                
                '''bool && bool'''
                '''
                if(valorI==1){goto L1;}
                goto L2;
                L2:
                if(valorD==1){goto L3;}
                goto L4;
                '''            
                entorno.imprimirln('if('+str(valorI)+'==1){ goto '+L1+';} // Lv')
                entorno.imprimirln('goto '+lf+'; // Lf')
                entorno.imprimirln(L1+':')
                valorD = self.expresionD.getValor(entorno)                                                
                if isinstance(valorD, int):
                    entorno.imprimirln('if('+str(valorD)+'==1){ goto '+lv+';} // Lv')
                    entorno.imprimirln('goto '+lf+'; // Lf')     
                    self.lv=lv
                    self.lf=lf          
                else:
                    self.lv=valorD.lv
                    self.lf=lf +':\n'+valorD.lf                         
                return self                

            else:                                             
                '''etiqueta and bool'''
                '''
                valorI.lf:
                if(valorD==1){ goto L1;}
                goto L2;
                '''
                L2=global_utils.generarEtiqueta()
                entorno.imprimirln(valorI.lv+': // Lv')
                valorD = self.expresionD.getValor(entorno)
                if isinstance(valorD, int):
                    entorno.imprimirln('if('+str(valorD)+'==1){ goto '+lv+';} // Lv')
                    entorno.imprimirln('goto '+lf+'; // Lf')     
                    self.lv=lv
                    self.lf=valorI.lf + ':\n' +lf
                else:
                    self.lv=valorD.lv
                    self.lf=valorI.lf + ':\n' +valorD.lf
                return self      

class Not(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'NOT')  
        grafo.edge(padre,id)      
        self.expresion.graficar(id, grafo)        
    
    def getTipo(self, entorno):
        tipo = self.expresion.getTipo(entorno)
        if tipo.esBool():
            return Tipo(TipoPrimitivo.BOOL)
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esBool():
            valor = self.expresion.getValor(entorno)
            if isinstance(valor, int):
                '''
                if(valor==1){goto lf;}
                goto lv;
                '''
                self.lv=global_utils.generarEtiqueta()
                self.lf=global_utils.generarEtiqueta()
                entorno.imprimirln('if('+str(valor)+'==1){goto '+self.lf+';}')
                entorno.imprimirln('goto '+self.lv+';')
            else:
                '''
                Solo le damos la vuelta a las etiquetas
                '''
                self.lv=valor.lf
                self.lf=valor.lv
            return self
        return None

class Rango(Expresion):
    def __init__(self, expresionInicio, expresionFinal, linea, columna):
        self.expresionInicio = expresionInicio
        self.expresionFinal = expresionFinal
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'rango')  
        grafo.edge(padre,id)      
        self.expresionInicio.graficar(id, grafo)               
        self.expresionFinal.graficar(id, grafo)               
    
    def getTipo(self, entorno):
        tipoI = self.expresionInicio.getTipo(entorno)
        tipoD = self.expresionFinal.getTipo(entorno)

        if (tipoI is None) or (tipoD is None):
            global_utils.registrySemanticError('rango for','Variable no definida.' , self.linea, self.columna)
            return Tipo(TipoPrimitivo.ERROR)

        if tipoI.esNumerico() and tipoD.esNumerico():
            return Tipo(TipoPrimitivo.ENTERO)
        global_utils.registrySemanticError('rango for','Valor inválido para rangos en ciclo for' , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)
    
    def getValor(self, entorno):
        tipo = self.getTipo(entorno)
        if not tipo.esError():
            self.valorI = self.expresionInicio.getValor(entorno)
            self.valorD = self.expresionFinal.getValor(entorno)
            return self

class Arreglo(Expresion):
    def __init__(self, lista_expresiones, linea, columna):
        self.lista = lista_expresiones
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'arreglo')  
        grafo.edge(padre,id)   
        for exp in self.lista:   
            exp.graficar(id, grafo)        
    
    def getTipo(self, entorno):
        return Tipo(TipoPrimitivo.ARREGLO)
    
    def getValor(self, entorno):
        arreglo_simbolos = []
        for exp in self.lista:
            tipo_actual = exp.getTipo(entorno)
            if tipo_actual is None:
                global_utils.registrySemanticError('elemento arreglo','Valor inválido, variable no declarada.' , self.linea, self.columna)
            elif tipo_actual.esError():
                global_utils.registrySemanticError('elemento arreglo','Valor inválido, variable no declarada.' , self.linea, self.columna)
            else:
                valor = exp.getValor(entorno)
                simbolo = Simbolo('', tipo_actual, valor, self.linea, self.columna)
                arreglo_simbolos.append(simbolo)
        return arreglo_simbolos

class Ternario(Expresion):
    def __init__(self, condicion , expV, expF , linea, columna):
        self.condicion = condicion
        self.expV = expV 
        self.expF = expF 
        self.linea = linea 
        self.columna = columna 

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'ternario')  
        grafo.edge(padre,id)    
        self.condicion.graficar(id, grafo)
        self.expV.graficar(id, grafo)
        self.expF.graficar(id, grafo)

    def getTipo(self, entorno):
        tipo_valor = self.condicion.getTipo(entorno)
        if tipo_valor is None:
           global_utils.registrySemanticError('Ternario','Valor erroneo condición.' , self.linea, self.columna) 
           return Tipo(TipoPrimitivo.ERROR)
        if not tipo_valor.esBool():
           global_utils.registrySemanticError('Ternario','Valor erroneo condición.' , self.linea, self.columna) 
           return Tipo(TipoPrimitivo.ERROR)        
        valor = self.condicion.getValor(entorno)
        if valor:
            return self.expV.getTipo(entorno)
        else:
            return self.expF.getTipo(entorno)

    def getValor(self, entorno):
        tipo_valor = self.condicion.getTipo(entorno)
        if tipo_valor is None:
           global_utils.registrySemanticError('Ternario','Valor erroneo condición.' , self.linea, self.columna) 
           return Tipo(TipoPrimitivo.ERROR)
        if not tipo_valor.esBool():
           global_utils.registrySemanticError('Ternario','Valor erroneo condición.' , self.linea, self.columna) 
           return Tipo(TipoPrimitivo.ERROR)        
        valor = self.condicion.getValor(entorno)
        if valor:
            return self.expV.getValor(entorno)
        else:
            return self.expF.getValor(entorno)      

class Llamada(Expresion):
    def __init__(self, id, parametros_actuales, linea, columna):
        self.id = id
        self.parametros = parametros_actuales 
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'llamada [ID] ' +self.id)  
        grafo.edge(padre,id)
        if self.parametros is not None:
            for i in self.parametros:
                i.graficar(id, grafo)



    def getTipo(self, entorno):
        if self.id=='string':
            return Tipo(TipoPrimitivo.STRING)
        nombre_funcion_buscada = self.id 
        if self.parametros is not None:
            for i in self.parametros:
                nombre_funcion_buscada = nombre_funcion_buscada +'_var'            
        simbolo = entorno.getSimbolo(nombre_funcion_buscada)
        return simbolo.tipo
    
    def getValor(self, entorno):
        nuevoEntorno = Entorno(entorno)
        #Creamos las nuevas variables. 
        nombre_funcion_buscada = self.id 
        if self.parametros is not None:
            for i in self.parametros:
                nombre_funcion_buscada = nombre_funcion_buscada +'_var'
        #buscamos la funcion
        if nombre_funcion_buscada == 'string_var':  
            t0=global_utils.generarTemporal()                      
            t1=global_utils.generarTemporal()
            t2=global_utils.generarTemporal()
            t3=global_utils.generarTemporal()
            t4=global_utils.generarTemporal()
            t5=global_utils.generarTemporal()

            entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulacion de cambio de entorno')
            entorno.imprimirln(t1+'='+t0+'+1;// Direccion parametro 1')
            for i in self.parametros:
                expresion = i
            tipo = expresion.getTipo(entorno)
            valor = expresion.getValor(entorno)            
            entorno.imprimirln('stack[int('+t1+')]='+str(valor)+';// paso parametro')
            entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
            if tipo.esBool():
                entorno.imprimirln('BoolToString_Nativa();')    
            if tipo.esEntero():
                entorno.imprimirln('IntToString_Nativa();')    
            if tipo.esFloat():
                entorno.imprimirln('FloatToString_Nativa();')                                    
            entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
            entorno.imprimirln(t2+'='+t0+'+0;// Direccion retorno')
            entorno.imprimirln(t3+'=stack[int('+t2+')]; // Valor de retorno')            
            return t3
        else:
            funcion_a_llamar = entorno.getSimbolo(nombre_funcion_buscada)
            if funcion_a_llamar is not None:
                t0=global_utils.generarTemporal()                      
                t1=global_utils.generarTemporal()
                t2=global_utils.generarTemporal()
                t3=global_utils.generarTemporal()
                t4=global_utils.generarTemporal()
                t5=global_utils.generarTemporal()

                entorno.imprimirln(t0+'=P+'+str(entorno.tamanioEntorno())+';//Simulacion de cambio de entorno')
                if self.parametros is not None:
                    contador = 1; 
                    if self.parametros is not None:
                        for i in self.parametros:
                            t1=global_utils.generarTemporal()
                            entorno.imprimirln(t1+'='+t0+'+'+str(contador)+';// Direccion parametro '+str(contador))                                    
                            expresion = i                        
                            tipo = expresion.getTipo(entorno)
                            valor = expresion.getValor(entorno)                                    
                            entorno.imprimirln('stack[int('+t1+')]='+str(valor)+';// paso parametro')   
                            contador = contador+1   
                if nombre_funcion_buscada==global_utils.metodoActual():
                    '''
                    Guardamos los temporales en la pila
                    '''
                    t11=global_utils.generarTemporal()
                    t12=global_utils.generarTemporal()
                    t13=global_utils.generarTemporal()
                    t14=global_utils.generarTemporal()
                    t15=global_utils.generarTemporal()                    
                    entorno.imprimirln(t11+'=P+'+str(entorno.tamanioEntorno())+';// Inicio nuevos temporales')
                    for simbolo in entorno.tabla.tabla:
                        simbolo= entorno.getSimbolo(simbolo)
                        entorno.imprimirln(t12+'=P+'+str(simbolo.posicion)+';//Direccion variable')
                        entorno.imprimirln(t13+'=stack[int('+t12+')];//Valor variable')
                        entorno.imprimirln(t14+'='+t12+'+'+str(simbolo.posicion)+';//Direccion variable')
                        entorno.imprimirln('stack[int('+t14+')]='+t13+';')
                        entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')
                                    
                entorno.imprimirln('P=P+'+str(entorno.tamanioEntorno())+';// Cambio de entorno')                
                entorno.imprimirln(nombre_funcion_buscada+'();')                                     
                entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')

                if nombre_funcion_buscada==global_utils.metodoActual():
                    entorno.imprimirln('P=P-'+str(entorno.tamanioEntorno())+';// Retomar entorno')
                    '''
                    Obtenemos de nuevo los temporales
                    '''
                    t21=global_utils.generarTemporal()
                    t22=global_utils.generarTemporal()
                    t23=global_utils.generarTemporal()
                    t24=global_utils.generarTemporal()
                    t25=global_utils.generarTemporal()                     
                    entorno.imprimirln(t21+'=P+'+str(entorno.tamanioEntorno())+';// Inicio nuevos temporales')
                    for simbolo in entorno.tabla.tabla:
                        simbolo= entorno.getSimbolo(simbolo)
                        entorno.imprimirln(t24+'='+t12+'+'+str(simbolo.posicion)+';//Direccion variable')
                        entorno.imprimirln(t23+'=stack[int('+t24+')];')                        
                        entorno.imprimirln(t22+'=P+'+str(simbolo.posicion)+';//Direccion variable')
                        entorno.imprimirln('stack[int('+t22+')]='+t23+';//Valor variable')                        

                entorno.imprimirln(t2+'='+t0+'+0;// Direccion retorno')
                entorno.imprimirln(t3+'=stack[int('+t2+')]; // Valor de retorno')            
                return t3  

     
            else:
                contructor_estructura = entorno.getSimbolo(self.id)
                if contructor_estructura is None:
                    global_utils.registrySemanticError('llamada','función ' +self.id + ' no declarada.' , self.linea, self.columna) 
                    return None
                else:
                    if isinstance(contructor_estructura, EstructuraSimbolo):
                        #(self, id, valores):
                        instancia = contructor_estructura.generarInstancia('',self.parametros, entorno)
                        return instancia

        
class Acceso(Expresion):
    def __init__(self, expresion, dim_lista, linea, columna):
        self.expresion = expresion
        self.dim_lista = dim_lista
        self.linea = linea
        self.columna = columna
    
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'Acceso-Arreglo')  
        grafo.edge(padre,id)        
        self.expresion.graficar(id, grafo)
        grafo.node(id+'posicion', 'Posicion')
        grafo.edge(id,id+'posicion')        
        for dim in self.dim_lista:
            dim.graficar(id+'posicion', grafo)
        
    def getTipo(self, entorno):
        tipo_exp = self.expresion.getTipo(entorno)
        if tipo_exp is None:
            global_utils.registrySemanticError('Acceso','Valor no válido de arreglo' , self.linea, self.columna)
            return Tipo(TipoPrimitivo.ERROR)
        #if tipo_exp.esCadena():
        #    return tipo_exp
        if tipo_exp.esDinamico():
            return Tipo(TipoPrimitivo.DINAMICO)
        global_utils.registrySemanticError('Acceso','Valor no válido de arreglo' , self.linea, self.columna)
        return Tipo(TipoPrimitivo.ERROR)        
    
    def getValor(self, entorno):
        tipo_tmp = self.getTipo(entorno)
        if tipo_tmp.esError():
            return None
        simbolo = self.expresion.getValor(entorno)
        valor = simbolo ##Tenemos el arreglo de valores
        val = None
        for dim in self.dim_lista:
            tipo_dim = dim.getTipo(entorno)
            if tipo_dim.esDinamico():
                valor_dim = dim.getValor(entorno)
                tipo_real = entorno.obtenerTipo(valor)
                if tipo_real.esEntero():
                    if isinstance(valor, list): 
                        if valor_dim < len(valor):
                            valor  = valor[valor_dim]                        
                            val  = valor[valor_dim]
                        else:
                            global_utils.registrySemanticError('Acceso','El arreglo tiene un máximo de ' +str(len(valor)) , self.linea, self.columna)                        
                    else:
                        global_utils.registrySemanticError('Acceso','El elemento no es un arreglo ' , self.linea, self.columna)
                        return None
            elif tipo_dim.esEntero():
                valor_dim = dim.getValor(entorno)
                if isinstance(valor, list):                    
                    if valor_dim < len(valor):                                        
                        val  = valor[valor_dim].valor                                        
                        valor = val
                    else:
                        global_utils.registrySemanticError('Acceso','El arreglo tiene un máximo de ' +str(len(valor)) , self.linea, self.columna)
                        return None
                else:
                    global_utils.registrySemanticError('Acceso','El elemento no es un arreglo ' , self.linea, self.columna)
                    return None
        return val                

class AsignacionArreglo(Instruccion):
    def __init__(self, acceso, expresion, linea, columna):
        self.acceso = acceso
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self))
        grafo.node(id, 'asignacion-arreglo')  
        grafo.edge(padre,id)        
        self.acceso.graficar(id, grafo)
        self.expresion.graficar(id, grafo)

    def ejecutar(self, entorno):
        tipo_expresion = self.expresion.getTipo(entorno)
        if tipo_expresion is None:
            global_utils.registrySemanticError('Asignacion-arreglo','Error al obtener el valor de la expresión.' , self.linea, self.columna)
            return
        nuevo_valor = self.expresion.getValor(entorno)
        tipo_real = tipo_expresion
        if tipo_real.esDinamico():
            tipo_real = entorno.obtenerTipo(nuevo_valor)        
        self.dim_lista = self.acceso.dim_lista
        simbolo = self.acceso.expresion.getValor(entorno)
        valor = simbolo ##Tenemos el arreglo de valores
        for dim in self.dim_lista:
            tipo_dim = dim.getTipo(entorno)
            if tipo_dim.esDinamico():
                valor_dim = dim.getValor(entorno)
                tipo_real = entorno.obtenerTipo(valor)
                if tipo_real.esEntero():
                    if isinstance(valor, list): 
                        if valor_dim < len(valor):
                            valor  = valor[valor_dim]                        
                            val  = valor[valor_dim]
                        else:
                            global_utils.registrySemanticError('Acceso','El arreglo tiene un máximo de ' +str(len(valor)) , self.linea, self.columna)                        
                    else:
                        global_utils.registrySemanticError('Acceso','El elemento no es un arreglo ' , self.linea, self.columna)
                        return None
            elif tipo_dim.esEntero():
                valor_dim = dim.getValor(entorno)
                if isinstance(valor, list):                    
                    if valor_dim < len(valor):                                        
                        val  = valor[valor_dim]                                        
                        valor = val
                    else:
                        global_utils.registrySemanticError('Acceso','El arreglo tiene un máximo de ' +str(len(valor)) , self.linea, self.columna)
                        return None
                else:
                    global_utils.registrySemanticError('Acceso','El elemento no es un arreglo ' , self.linea, self.columna)
                    return None
        if valor is not None:
            if isinstance(valor, Simbolo):                
                valor.valor = nuevo_valor


class Estructura(Instruccion):
    def __init__(self, mutable, nombre, atributos, linea, columna):
        self.mutable = mutable 
        self.nombre = nombre 
        self.atributos = atributos
        self.linea = linea
        self.columna = columna

    def graficar(self, padre, grafo):
        id = 'Nodo'+ str(hash(self)) 
        grafo.node(id, 'estructura [Mutable] ' +str(self.mutable))  
        grafo.edge(padre,id)        
        if self.atributos is not None:            
            for i in self.atributos:
                i.graficar(id, grafo)   

    def ejecutar(self, entorno):
        simbolo = EstructuraSimbolo(self.nombre, self.atributos, self.mutable, self.linea, self.columna)
        entorno.insertSimbolo(simbolo)
        