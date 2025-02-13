from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola mundo")
HttpResponse("<html><body><h1>Hola mundo</h1></body></html>")