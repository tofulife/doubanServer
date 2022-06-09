
from douban.models import(
    bookModel
)
from rest_framework import serializers





class bookSerializers(serializers.ModelSerializer):
    class Meta:
        model = bookModel
        fields ='__all__'


