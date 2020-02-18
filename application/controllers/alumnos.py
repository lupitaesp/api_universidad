import app 
import web
import csv
import json

render = web.template.render('application/controllers/')

class AlumnosCsv:
    def GET(self):
        try:
            data = web.input()
            if data['action'] == "get" and data['token'] == '1234':

                result=[]
                result.append(matricula) #definir esto
                result.append(nombre)
                result.append(primero)
                result.append(segundo)
                result.append(carrera)
                result['status']='200k'
                return json.dumps(result)

                with open('static/csv/datos.csv','a+', newline='') as csvfile:
                    read = csv.read(csvfile)
                    read.readrow(result)

                result = "matricula,nombre,primero,segundo,carrera\n"
                return result
            else:
                result = [] #crea array vacio
                result.append("No te conozco")
                return result
        except Exception as e:
            result = []
            result.append("Mmmm algo salio mal {}".format(e.args))
            return result