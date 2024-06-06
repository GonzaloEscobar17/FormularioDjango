from django.http import HttpResponse
import datetime


def comparar(request):
    edad = 8
    if edad >= 18:
        return HttpResponse("Eres mayor de edad :)")
    else:
        return HttpResponse("Eres menor de edad :(")
    
def title(request):
    titulo ="""
            <html>
            <body>
                <h1>Visual Studio</h1>
            </body>
            </html>
            """
    return HttpResponse(titulo)

def dameFecha(request):
    fechaActual = datetime.datetime.now()

    titulo ="""
            <html>
            <body>
                <h3>Fecha y hora actuales %s</h3>
            </body>
            </html>
            """ % fechaActual
    return HttpResponse(titulo)

def calculaEdad(request, edad, agno):
    periodo = agno - 2024
    edadFutura = edad + periodo
    documento ="""
                <html>
                <body>
                    <h2>En el año %s tendras %s años</h2>
                </body>
                </html>
                """%(agno, edadFutura)
    return HttpResponse(documento)