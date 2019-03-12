from django.shortcuts import render

# Create your views here.
from home.models import Book


def detail(request):
    if request.method == 'GET':
        try:
            book_id = request.GET.get('id')
            if book_id:
                book = Book.objects.get(book_id=book_id)
                return render(request,'detail.html',{'book':book})
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
