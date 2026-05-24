from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView



@login_required
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


class Create (LoginRequiredMixin, generic.CreateView):
    model = models.Book
    template_name = 'create.html'
    fields = '__all__'
    success_url = '/cataloge'

class Details (LoginRequiredMixin, generic.DeleteView):
    model = models.Book
    template_name = 'details.html'
    context_object_name = 'book'

class Regiser (generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'

class ChangePass (PasswordChangeView):
    template_name = 'registration/change_pass.html'
    success_url = '/accounts/login'