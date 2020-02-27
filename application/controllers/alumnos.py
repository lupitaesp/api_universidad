import web
import json
import csv
#render = web.template.render('application/controllers/')   #En esta no se ocupa
class Alumnos:
    def GET(self):
        try:
            datos=web.input()     #Los datos introducidos por el usuario se almacenaran en datos
            if datos['token']=="1234":#Si el usuario ingresa bien el token se declarara lo siguiente
                result=[]           #Un arreglo
                result2={}          #Un diccionario
                if datos['action']=="get":        #Si accion es get va a hacer lo siguiente
                    with open('static/csv/alumnos.csv','r') as csvfile:   #Ruta del archivo csv que va a leer, r es de lectura, csvfile es una variable cualquiera
                        reader = csv.DictReader(csvfile)         #Lector del archivo, DictReader te almacena los datos como en diccionario en este caso en la variable reader
                        for row in reader:              #Lee la primer fila y la manda la arreglo
                            result.append(row)          #Lo manda al arreglo result
                            result2['Version']="0.5.1"
                            result2['status']="200 OK"
                            result2['alumnos']=result      #Result2 en la posicion alumnos, sera lo que va a almacenar en result
                    return json.dumps(result2)          #Va a regresar un json del result2 que es lo que va almacenando el arreglo
                elif datos['action']=="buscar":
                    consulta={}
                    consulta['version']="0.01"
                    consulta['status']="200 ok"
                    #matricula=datos['matricula']
                    result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open('static/csv/alumnos.csv','r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result = []
                        for row in reader:
                            if str(row['matricula'])==datos['matricula']:
                                #resultados={}
                                #resultados['matricula']=str(row['matricula'])
                                #resultados['nombre']=str(row['nombre'])
                                #resultados['primer_apellido']=str(row['primer_apellido'])
                                #resultados['segundo_apellido']=str(row['segundo_apellido'])
                                #resultados['carrera']=str(row['carrera'])
                                result.append(row)
                            #resultados['alumno']=result
                    return json.dumps(result)
                elif datos["action"] == "put":
                    m1 = datos["matricula"]
                    m2 = datos["nombre"]
                    m3 = datos["primer_apellido"]
                    m4 = datos["segundo_apellido"]
                    m5 = datos["carrera"]
                    result = []
                    result.append(m1)
                    result.append(m2)
                    result.append(m3)
                    result.append(m4)
                    result.append(m5)
                    with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                        writer = csv.writer(csvfiles)
                        writer.writerow(result)
                    return("Realizado")
                elif datos['action'] == "actualizar":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        lo = []
                        validator = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                 
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    v1 = datos["matricula"]
                                    v2 = datos["nombre"]
                                    v3 = datos["primer_apellido"]
                                    v4 = datos["segundo_apellido"]
                                    v5 = datos["carrera"]
                                    result.append(v1)
                                    result.append(v2)
                                    result.append(v3)
                                    result.append(v4)
                                    result.append(v5)
                                    lo.append(result)
                            else:
                                fila1 = row['matricula'] 
                                fila2 = row['nombre']
                                fila3 = row['primer_apellido']
                                fila4 = row['segundo_apellido']
                                fila5 = row['carrera']
                                result.append(fila1)
                                result.append(fila2)
                                result.append(fila3)
                                result.append(fila4)
                                result.append(fila5)
                                lo.append(result)
                        with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                            writer = csv.writer(csvfiles)
                            for x in lo:
                                writer.writerow(x)
                        if validator == 0:
                            result.append("No se encontro el dato")
                    return json.dumps("Actualizado")
                elif datos['action'] == "borrar":
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        lo = []
                        validator = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    print("ok")
                            else:
                                line1 = row['matricula'] 
                                line2 = row['nombre']
                                line3 = row['primer_apellido']
                                line4 = row['segundo_apellido']
                                line5 = row['carrera']
                                result.append(line1)
                                result.append(line2)
                                result.append(line3)
                                result.append(line4)
                                result.append(line5)
                                lo.append(result)
                            with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                                writer = csv.writer(csvfiles)
                                writer.writerow(result)
                            if validator == 0:
                                result.append("No existe el valor")
                        return json.dumps("Realizado")
                else:                           #Si accion no es get va a poner comando no encontrado
                    result2={}
                    result2['Version']="0.1.0"
                    result2['status']="Command not found"
                    return json.dumps(result2)
            else:
                result={}
                result['Version']="0.1.0"
                result['status']="Los datos insertados son incorrectos"
                return json.dumps(result)
        except Exception as e:
            result={}
            text= "ups algo paso{}".format(e.args)
            result  ['status'] = text 
            return json.dumps(result)