from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

def status(request):
    return HttpResponse('It\'s OK')