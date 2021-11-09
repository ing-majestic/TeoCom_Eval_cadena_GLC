# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#funcion para abrir archivo
def abrir_archivo(name):
    #determinamos le directorio donde se encuentra el archivo
    directory = "./"
    #abrimos el archivo y el contenido lo cargamos a una variable
    archivo = open(directory+name)
    #resultado de lectura
    #Si se quiere utilizar en mas d eun proceso el contenido debe volverse a abrir el archivo 8incluyendo print)
    #print(imprime.read())
    return (archivo)

#funcion que lee e imprime el contenido de documento
def leer_documento(name):
    #determinamos le directorio donde se encuentra el archivo
    directory = "./"
    #abrimos el archivo y el contenido lo cargamos a una variable
    archivo = open(directory+name)
    imprime = open(directory + name)
    #resultado de lectura
    #Si se quiere utilizar en mas d eun proceso el contenido debe volverse a abrir el archivo 8incluyendo print)
    print("-----------------------------------------------")
    print("Contenido del documento '" + name + "'")
    print("-----------------------------------------------")
    print(imprime.read())
    print("----------------END DOC-----------------")
    imprime.close()
    return (archivo)

#funcion para abrir archivo y guardar las lineas en una lista
def abrir_archivo_lineas(name):
    #abrimos el archivo y cargamos el contenido a una variable
    archivo = abrir_archivo(name)
    #almacenamos las lineas en lista
    lineas = archivo.readlines()

    #dividir lineas en lista de lineas
    lista_lineas = []
    #limpieza de caracteres especiales por linea
    for linea in lineas:
        linea = linea.split()
        mensaje = linea[0]
        mensaje = mensaje.replace(",","")
        mensaje = mensaje.replace(";", "")
        mensaje = mensaje.replace("(", "")
        mensaje = mensaje.replace(")", "")
        #agrega a una lista los mensajes
        a = list(mensaje)
        lista_lineas.append(a)
    #print("")
    #print("---------lista de lineas depuradas-------")
    #print(lista_lineas)
    print("Obtención de reglas en archivo : "+name+ "... ok!")
    return (lista_lineas)

#funcion que obtiene una cadena a evaluar
def obtener_cadena():
    cadena = []
    print("Ingresa la cade a validar:")
    cadena = input()
    print("Cadena ingresada: "+cadena)
    return (cadena)

def alfabeto(file):
    cadena = []
    alfabeto = []
    reglas = abrir_archivo_lineas(file)
    #creamos la lista del alfabeto que pueden reconocer las reglas
    for regla in reglas:
        #print(len(regla))
        if len(regla) == 4:
            cadena.append(regla[1])
        if len(regla) == 8:
            cadena.append(regla[4])
        elif len(regla) == 10:
            cadena.append(regla[3])
    alfabeto = list(dict.fromkeys(cadena))
    #print("cadena reconocido es:")
    #print(cadena)
    #print("El alfabeto reconocido es:")
    print("Obtención de alfabeto en reglas... ok!")
    #print(alfabeto)
    return (alfabeto)

def indice_cadena(name):
    reglas =abrir_archivo_lineas(name)
    #print(reglas)
    for regla in reglas:
        regla.append(0)
    #print(reglas)
    return reglas

def buscar_regla_en_reglas(cadena,reglas,lista_reglas):
    reglas_perdidas = reglas
    reglas_fuente = lista_reglas
    cadena = cadena
    reglas_aceptacion = []
    print(reglas_fuente)
    print(reglas_perdidas)
    for letra in cadena:
        for elemento in reglas_perdidas:
            if len(elemento) == 4:
                thislist = [elemento[0],elemento[1],elemento[2],letra]
            if len(elemento) == 8:
                thislist = [elemento[1],elemento[2],elemento[3],letra]
            #print(thislist)
            for regla in reglas_fuente:
                #if len(regla) == 4:
                #    vsList = [regla[0],regla[1],regla[2],regla[-1]]
                #    if(set(thislist) == set(vsList)):
                #        #print("List are equal")
                #        #print(regla)
                #        elemento[-1]= 1
                #        break
                if len(regla) == 5:
                    vsList = [regla[0],regla[1],regla[2],letra]
                    if(set(thislist) == set(vsList)):
                        #print("List are equal")
                        #print(regla)
                        elemento[-1] = 1
                        break
                if len(regla) == 8:
                    vsList = [regla[1],regla[2],regla[3]]
                    if(set(thislist) == set(vsList)):
                        #print("List are equal")
                        #print(regla)
                        elemento[-1] = 1
                        break
                if len(regla) == 11:
                    vsList = [regla[0],regla[1],regla[2],regla[3]]
                    if(set(thislist) == set(vsList)):
                        #print("List are equal")
                        #print(regla)
                        regla_acep = [regla[3],regla[4],regla[5],regla[6],regla[7],regla[8],regla[9], regla[10]]
                        print(regla_acep)
                        reglas_aceptacion.append(regla_acep)
                        reglas_perdidas.append(regla_acep)
                        elemento[-1] = 1
                        break
    print(reglas_perdidas)




#función que buscara los elementos d ela cadena ingresada y guardara las reglas que aceptan la cadena propuesta
def evaluar_cadena (archivo_reglas):
    reglas_aceptación = []
    nueva_cadena = []
    abc = []
    reglas = []
    cadena = []
    reglas = indice_cadena(archivo_reglas)
    abc = alfabeto(archivo_reglas)
    #obtener cadena a evaluar
    cadena = [obtener_cadena()]

    #primer evaluación si coincide el alfabeto con las reglas a aplicar
    abc_cadena = list(dict.fromkeys(cadena[0]))
    for letra in abc_cadena:
        try:
            abc.index(letra)
        except ValueError:
            print("Ooops la cadena no corresponde al alfabeto del archivo de reglas!")

    # se comienza a evaluar caracter por caracter de la cadena y se crea la lista de reglas de aceptación
    # se agrega la regla S a la lista de reglas de aceptación
    #print(reglas)
    for regla in reglas:
        if len(regla) == 4:
                index = ["Def: S"]
                reglas_aceptación.append(index)
                reglas_aceptación.append(regla)
    #print(reglas_aceptación)
    # se obtiene la primer regla de aceptación S y se desagrega

    #a = reglas_aceptación[0][0]
    #b = reglas_aceptación[0][1]
    #c = reglas_aceptación[0][2]

    # se obtiene la primer letra de cadena
    for letra in cadena[0]:
        letra_cadena = letra
        if nueva_cadena != cadena:
            #se busca una regla que cumpla con el estado S y la primer letra de cadena
            for regla_ac in reglas_aceptación:

                    #print(regla_ac)
                    #evalua si la regla ya se ha leido, para su evaluación en en siclo pasado lo determina el valor ultimo d ecada regla (0 o 1)
                    #if regla_ac[-1] == 0:

                        if len(regla_ac) == 4 and regla_ac[-1] == 0:

                            a = regla_ac[0]
                            b = regla_ac[1]
                            c = regla_ac[2]

                            for regla in reglas:
                                #print(len(regla))
                                if len(regla) == 11 and regla[-1] == 0:
                                    # print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[3]


                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        #print("se encontro coincidencia con regla de aceptación len 4 vs regla len 11")

                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text+regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_a.extend(
                                            [regla[3], regla[4], regla[5], regla[6], regla[7], regla[8], regla[9], 0])
                                        nueva_cadena.append(regla[3])
                                        reglas_aceptación.append(regla_a)
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)


                                if len(regla) == 8 and regla[-1] == 0:
                                    # print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[3]


                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        #print("se encontro coincidencia con regla de longitud 8 vs regla aceptacion len 4")
                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_a.extend(
                                            [regla[3], regla[4], regla[5], regla[6], 0])
                                        nueva_cadena.append(regla[3])
                                        reglas_aceptación.append(regla_a)
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)


                                if len(regla) == 4 and regla[-1] == 0:
                                    # print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[1]


                                    #if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                    if a1 == a and a2 == b and a3 == c :
                                        #print("se encontro coincidencia con regla de aceptación len 4 vs regla len 4")
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)

                        elif len(regla_ac) == 5 and regla_ac[-1] == 0:
                            a = regla_ac[1]
                            b = regla_ac[2]
                            c = regla_ac[3]
                            #letra =regla_ac[0]
                            #print("se encontro coincidencia con regla de aceptación len 5 ")
                            #print(regla_ac)
                            #print(letra_cadena)

                            for regla in reglas:
                                if len(regla) == 11 and regla[-1] == 0:
                                    #print("regla de aceptación encontrada de longitud 5 vs una regla de lon 11")
                                    #print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    #letra_b = regla[3]



                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        #print("se encontro coincidencia con regla de aceptación lon 5 vs regla longitud 11")
                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_a.extend(
                                            [regla[3], regla[4], regla[5], regla[6], regla[7], regla[8], regla[9], 0])
                                        nueva_cadena.append(regla[3])
                                        reglas_aceptación.append(regla_a)
                                        # print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)


                                #print(regla)
                                if len(regla) == 8 and regla[-1] == 0:
                                #if len(regla) == 8:
                                    #print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[3]
                                    #print(letra_cadena)

                                    #print("se encontro coincidencia con regla de aceptación len 5 vs regla len 8")
                                    #print("1. Regla de aceptación buscada: ")
                                    #print(regla_ac)
                                    #print("2. Elementos que deben coincidir: ")
                                    #print(regla_buscada)
                                    #print("3. Regla con la que se compara")
                                    #print(regla)
                                    #print(letra_cadena)

                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        #print("se encontro coincidencia con regla de aceptación len 8 vs regla len 8")

                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_b = []
                                        regla_b.extend(
                                            [regla[4], regla[5], regla[6], 1])
                                        nueva_cadena.append(regla[5])
                                        reglas_aceptación.append(regla_b)
                                        regla_a.extend(
                                            [regla[3],regla_ac[1],regla_ac[2],regla_ac[3],0])
                                        reglas_aceptación.append(regla_a)
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)


                                if len(regla) == 4 and regla[-1] == 0:
                                    # print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[1]


                                    #if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                    if a1 == a and a2 == b and a3 == c :
                                        #print("se encontro coincidencia con regla de aceptación len 4 vs regla len 4")
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)

                        elif len(regla_ac) == 6 and regla_ac[-1] == 0:
                            a = regla_ac[1]
                            b = regla_ac[2]
                            c = regla_ac[3]


                            for regla in reglas:
                                #print(len(regla))
                                if len(regla) == 11 and regla[-1] == 0:
                                    # print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[3]
                                    #print("regla aceptación len 6 vs regla 11")
                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_a.extend(
                                            [regla[3], regla[4], regla[5], regla[6], regla[7], regla[8], regla[9], 0])
                                        nueva_cadena.append(regla[3])
                                        reglas_aceptación.append(regla_a)
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)

                        elif len(regla_ac) == 8 and regla_ac[-1] == 0:
                            a = regla_ac[1]
                            b = regla_ac[2]
                            c = regla_ac[3]


                            for regla in reglas:
                                if len(regla) == 11 and regla[-1] == 0:
                                    #print("regla de aceptación encontrada de longitud 8 vs una regla de lon 11")
                                    #print(regla_ac)
                                    #regla_buscada = [a, b, c]
                                    #print("Regla de aceptación buscada: ")
                                    #print(regla_buscada)
                                    #print(regla)

                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[3]
                                    #print(letra_cadena)


                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        #print("se encontro coincidencia con regla de aceptación lon 8 vs longitud 11")
                                        #print(regla_ac)
                                        #print(regla)
                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_a.extend(
                                            [regla[3], regla[4], regla[5], regla[6], regla[7], regla[8], regla[9], 0])
                                        nueva_cadena.append(regla[3])
                                        reglas_aceptación.append(regla_a)
                                        # print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)



                                if len(regla) == 8 and regla[-1] == 0:
                                    # print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    letra_b = regla[3]
                                    regla_buscada = [a, b, c]
                                    #print("Regla de aceptación buscada: ")
                                    #print(regla_buscada)
                                    #print(regla)
                                    #print(letra_cadena)

                                    if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                        #print("se encontro coincidencia con regla de aceptación len 8 vs regla len 8")

                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_b = []
                                        regla_b.extend(
                                            [regla[4], regla[5], regla[6], 1])
                                        nueva_cadena.append(regla[5])
                                        reglas_aceptación.append(regla_b)
                                        regla_a.extend(
                                            [regla[5],regla_ac[1],regla_ac[2],regla_ac[3],0])
                                        reglas_aceptación.append(regla_a)
                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)

                                if len(regla) == 5 and regla[-1] == 0:
                                    #print(regla)
                                    a1 = regla[0]
                                    a2 = regla[1]
                                    a3 = regla[2]
                                    regla_buscada = [a, b, c]

                                    #letra_b = regla[1]


                                    #if a1 == a and a2 == b and a3 == c and letra_cadena == letra_b:
                                    if a1 == a and a2 == b and a3 == c :
                                        #print("se encontro coincidencia con regla de aceptación len 8 vs regla len 5")
                                        #print("1. Regla de aceptación buscada: ")
                                        #print(regla_ac)
                                        #print("2. Elementos que deben coincidir: ")
                                        #print(regla_buscada)
                                        #print("3. Regla con la que se compara")
                                        #print(regla)

                                        regla_a = []
                                        text = ["Der:"]
                                        nueva_lista = text + regla_ac
                                        index = "".join([str(_) for _ in nueva_lista])
                                        reglas_aceptación.extend([index])
                                        regla_b = []
                                        regla_b.extend(
                                            [regla[0], regla[1], regla[2], 1])
                                        nueva_cadena.append(regla[3])
                                        reglas_aceptación.append(regla_b)
                                        regla_a.extend(
                                            [regla_ac[0],regla_ac[4],regla_ac[5],regla_ac[6],0])
                                        reglas_aceptación.append(regla_a)
                                        #print("4. regla que se agrega a cola:")
                                        #print(regla_b)


                                        #print(regla_a)
                                        regla_ac[-1] = 1
                                        regla[-1] = 1
                                        #print(reglas_aceptación)




    print("reglas de aceptación encontradas: ")
    print(len(reglas_aceptación))
    for regla in reglas_aceptación:
        index = reglas_aceptación.index(regla)
        print(str(index)+" "+str(regla))
    print("cadena formada por diferentes derivaciones segun al evaluación ")
    print(nueva_cadena)


def evalua_2():
    doc = "gram.cfg"
    reglas =  abrir_archivo_lineas(doc)
    reglas_indice = indice_cadena(doc)
    cadena_resultado = []
    cadena = list(input("Ingresa cadena: "))
    i = 0


    if ['1'] in reglas:
        index = reglas.index(['1'])
        cadena_resultado.append(reglas[index+1])
        reglas_indice[index+1][3] = 1
        print(cadena_resultado)
        regla_S = reglas[index+1]

        while i < len(cadena):
            #regla_S.append(cadena[i])
            print(regla_S)
            if regla_S in reglas:
                print("se encontro esta coincidencia: ")
                i = 0
            else:
                i += 1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doc = "gram.cfg"
    #leer_documento(doc)
    #abrir_archivo_lineas(doc)
    #cadena = reconoce_cadena()
    #obtener_cadena(cadena,doc)
    #alfabeto(doc)
    #indice_cadena(doc)
    evaluar_cadena(doc)
    #regla_aceptacion = [['f','L','h',0]]
    #reglas = indice_cadena(doc)
    #buscar_regla_en_reglas("cbb",regla_aceptacion,reglas)
    #evalua_2()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
