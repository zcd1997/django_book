from django.shortcuts import render

# Create your views here.
from home.models import Book, Category, Chapter


def chapter(request):
    if request.method == 'GET':
        try:
            book_id = request.GET.get('book_id')
            if book_id:
                book = Book.objects.get(book_id=book_id)
                chapters =  Chapter.objects.filter(book_id=book_id)
                return render(request, 'chapter.html', {'book':book,'chapters':chapters})
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')