# from django.http import HttpResponse
from rest_framework import viewsets
from douban.serializers import bookSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from douban.service import(
    bookService,
)



class bookView(viewsets.ModelViewSet):
    @api_view(['GET', 'POST'])
    def show(self):
        res = bookService().show()
        serializer = bookSerializers(res, many=True)
        return Response(serializer.data)

        