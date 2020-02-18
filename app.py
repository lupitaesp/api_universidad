import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/alumnos_csv/?', 'application.controllers.alumnos_csv.AlumnosCsv'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug = True
    app.run()