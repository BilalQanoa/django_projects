
from django.shortcuts import render, redirect
from car.models import Car

def lists (request):
    lists = Car.objects.all().order_by('-id')
    context = {
        'lists': lists
    }
    return render(request, 'lists.html', context)

def add (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        Car.objects.create(name=name, year=year)
        return redirect('lists')
    return render(request, 'add.html')

def delete (request):
    if request.method == 'POST':
        try:
            id = request.POST.get('car_id')
            Car.objects.get(id=id).delete()
            return redirect('lists')
        except:
            return redirect('lists')
    
    return render(request, 'delete.html')


