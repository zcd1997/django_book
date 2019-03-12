from django.shortcuts import render

# Create your views here.
from home.models import Book


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        books = Book.objects.filter(book_title__contains=keyword).order_by('book_id')
        return render(request, 'search_result.html', {'books': books})
    else:
        return render(request, 'error.html')
