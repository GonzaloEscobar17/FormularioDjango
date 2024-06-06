# Importa HttpResponse para enviar respuestas HTTP y Template, Context para manejar plantillas
from django.http import HttpResponse
from django.template import Template, Context

# Define la vista `formulario` que manejará la solicitud HTTP
def formulario(request):
    try:
        # Intenta abrir el archivo HTML de la plantilla en modo lectura
        with open("C:/Users/gonza/Desktop/Repaso_python/django/plantillas/index.html", 'r') as doc_externo:
            # Lee el contenido del archivo y crea un objeto Template
            plt = Template(doc_externo.read())
    except FileNotFoundError:
        # Si el archivo no se encuentra, devuelve una respuesta HTTP 404
        return HttpResponse("Archivo de plantilla no encontrado.", status=404)
    
    # Crea un contexto vacío (puedes agregar variables aquí si es necesario)
    ctx = Context({})
    # Renderiza la plantilla con el contexto y guarda el resultado en `formularioFinal`
    formularioFinal = plt.render(ctx)
    # Devuelve una respuesta HTTP con el contenido de la plantilla renderizada
    return HttpResponse(formularioFinal)
