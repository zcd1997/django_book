from django.shortcuts import render

# Create your views here.
from home.models import Category, Book


def category(request):
    if request.method == 'GET':
        try:
            categorys = Category.objects.all()
            cate_id = request.GET.get('cate')
            if cate_id:
                books = Book.objects.filter(cate_id=cate_id)
                return render(request, 'search_category.html', {'categorys':categorys, 'books':books})
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')