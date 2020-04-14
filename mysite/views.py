from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Главная страница</h2><p><a href="/contacts">Страница контакты</a></p><h3>Hello World!</h3>')

def status(request):
    return HttpResponse('It\'s OK')

def contacts(request):
    return HttpResponse('<h2>Страница контакты</h2><p><a href="/">Главная страница</a></p><p>Email: test@test.test</p><p>Phone: +7 (123) 456-78-99</p>')