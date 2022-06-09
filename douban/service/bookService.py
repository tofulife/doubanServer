from douban.models import(
    bookModel,
)

from douban.serializers import bookSerializers

# import douban.serializers

class bookService:
    def show(self):
        book = bookModel.objects.all()
        return book

    


