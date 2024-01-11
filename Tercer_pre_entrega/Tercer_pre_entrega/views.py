from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Hola, bienvenido a mi pagina")