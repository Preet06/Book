from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Book
# Create your views here.


def home_page(request):
    if request.method == 'GET':
        data = Book.objects.all()
        Language = request.GET.get('Language')
        Genre = request.GET.get('Genre')
        print(Language)

        if Language!='' and Language is not None:
            data=data.filter(Language=Language)

        if Genre!='' and Genre is not None:
            data=data.filter(Genre=Genre)    


        stu = {
       "data": data
           }
        return render(request, 'home.html',stu)
    else:
        data = Book.objects.all()
        stu = {
       "data": data
           }
        return render(request, 'home.html',stu)



class BookCreateView(CreateView):
    model = Book
    template_name = 'add.html'
    fields = ['Book_Name', 'Author', 'Genre','Language']
