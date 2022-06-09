from django.http import HttpResponse
from douban import views

def hello(request):
    return HttpResponse('test呀')


def tt():
    return HttpResponse(views.bookView.infun())