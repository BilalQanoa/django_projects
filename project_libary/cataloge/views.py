from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
def index (request):
    num_books = models.Book.objects.all().count()
    num_books_instance = models.BookInstance.objects.all().count()
    num_books_avaliable = models.BookInstance.objects.filter(statue__exact='a').count()

    context = {
        'num_books' : num_books,
        'num_books_instance' : num_books_instance,
        'num_books_avaliable' : num_books_avaliable,
    }
    return render(request, 'index.html', context)


class Create (generic.CreateView):
    model = models.Book
    template_name = 'create.html'
    fields = '__all__'
    success_url = '/cataloge'

class Details (generic.DeleteView):
    model = models.Book
    template_name = 'details.html'
    context_object_name = 'book'

    
