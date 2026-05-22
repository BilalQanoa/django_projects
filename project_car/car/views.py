
from django.shortcuts import render, redirect
from car.models import Car
from django.views import generic

# CBV:
class Lists (generic.ListView):
    template_name= 'lists.html'
    model = Car
    queryset = Car.objects.all().order_by('-id')
    context_object_name = 'lists'

    
class Delete (generic.View):
    def get(self, request):
        return render(request, 'delete.html')

    def post(self, request):
        try:
            car_id = request.POST.get('car_id')
            Car.objects.get(id=car_id).delete()
        except:
            pass
        return redirect('lists')

class Add (generic.CreateView):
    model = Car
    template_name = 'add.html'
    success_url = '/'
    fields = '__all__'



# FBV:
# def lists (request):
#     lists = Car.objects.all().order_by('-id')
#     context = {
#         'lists': lists
#     }
#     return render(request, 'lists.html', context)


# def add (request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         year = request.POST.get('year')
#         Car.objects.create(name=name, year=year)
#         return redirect('lists')
#     return render(request, 'add.html')


# def delete (request):
#     if request.method == 'POST':
#         try:
#             id = request.POST.get('car_id')
#             Car.objects.get(id=id).delete()
#             return redirect('lists')
#         except:
#             return redirect('lists')
    
#     return render(request, 'delete.html')


