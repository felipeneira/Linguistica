##input: numero entre 1 y 999
##output: string del numero en palabras
def numero_mapu(X):
    mapu_1_10 = ['kiñe','epu','kula','meli','kechu','kayu','regle','pura','aylla','mari']
    ## usamos la cantidad de numeros para determinar la accion
    if len(str(X))==1:
        ## Las unidades poseen solo un numero asi que este simplemente ingresa
        P = X-1
        numero = mapu_1_10[P]
        return numero
    elif len(str(X))==2:
        ##En el caso de tener un numero con decenas calculamos el numero partido
        ##en 10 y utilizamos la funcion int() para eliminar lo que venga despues
        ##del punto
        D = int(X/10)
        ##Para sacar la unidad volvemos a multiplicar nuestra decena por 10
        ##y se lo restamos al numero total, esto nos indica las unidades
        U = X - (D*10)
        ##De esta forma tratamos cada numero por separado y podemos aplicar la 
        ##el mismo metodo que aplicamos a las unidades
        D = mapu_1_10[D-1]
        U = mapu_1_10[U-1]
        ##debido a la forma de los numeros en mapudungun utilizaremos mas if,
        ##esto porque si el numero esta entre el 10 y 20 se suele omitir el kiñe
        ## (kiñe) mari epu -> 12
        if D == "kiñe":
            ##A su vez, si el numero termina con 0 nos entregara al final mari
            ## debido a que la posicion quedara en -1. Para evitar imprimir esto
            ## unicamente imprimiremos la decena y si el numero es diferente de
            ##-1 ("mari") imprimiremos la unidad
            if U == "mari":
                return mapu_1_10[-1]
            if U != "mari":
                return "mari "+ U
        ##En caso de que la decena sea diferente de 1 (esto significa mayor de 19) 
        ##si se adjuntara el numero correspondiente
        else:    
            if U == "mari":
                return D+" mari"
            if U != "mari":
                ##es necesario decir que se utiliza un string que diga "mari"
                ##directamente por terminos de eficiencia, pero tambien es posible
                ##utilizar mapu_1_10[-1] o mapu_1_10[9]. Esto es posible unicamente
                ##debido a la estabilidad del mapudungun
                return D+" mari "+U
    elif len(str(X))==3:
        C= int(X/100)
        D = int((X - (C*100))/10)
        U = X -((C*100)+(D*10))
        C = mapu_1_10[C-1]
        D = mapu_1_10[D-1]
        U = mapu_1_10[U-1]
        ##Debido a que cuando la centena es uno suele anteponerse el kiñe, no es
        ##necesario separar ambos casos con una condicion
        ##Ahora se añade tambien una condicion en caso de que la decena
        ##sea igual a 0 pero existan unidades
        if D == "mari":
            if U == "mari":
                return C+" pataka"
            if U != "mari":
                return C+" pataka " + U
        elif D == "kiñe":
            if U == "mari":
                return C+" pataka "+mapu_1_10[-1]
            if U != "mari":
                return C+" pataka "+"mari "+ U
        else:    
            if U == "mari":
                return C+" pataka "+ D+" mari"
            if U != "mari":
                return C+" pataka "+ D+" mari "+ U
    else:
        print("Fotru anhay!")
        
