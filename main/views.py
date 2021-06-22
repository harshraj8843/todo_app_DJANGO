from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.views import View

from . import models

# Create your views here.

# home view or todo view
class home(View):

    def get(self, request):
        datas = []
        try:
            data1 = models.Todo.objects.all().order_by('last_date')
            for data in data1:
                datas.append({
                    'id': data.id,
                    'name': data.name,
                    'last_date': data.last_date
                })
        except:
            pass
        return render(request, 'todo.html', {
            'datas': datas
        })

# todos marked as done view
class done(View):

    def get(self, request):
        datas = []
        try:
            data1 = models.Done.objects.all().order_by('-deleted_at')
            for data in data1:
                datas.append({
                    'name': data.name,
                    'last_date': data.last_date,
                    'deleted_at': data.deleted_at
                })
        except:
            pass
        return render(request, 'done.html', {
            'datas': datas
        })

# create view
class create(View):

    # get method will return form
    def get(self, request):
        return render(request, 'add.html')

    # post method will submit the form
    def post(self, request):
        try:
            data1 = models.Todo()
            data1.name = request.POST.get('name')
            data1.last_date = request.POST.get('date')
            data1.save()
        except:
            pass
        return redirect('/')

# mark done button view
class mark_done(View):

    def get(self, request, id):
        try:
            data1 = models.Todo.objects.get(id=id)

            #copying data1 data to data2
            data2 = models.Done()
            data2.name = data1.name
            data2.last_date = data1.last_date
            data2.save()

            # deleting todo
            data1.delete()
        except:
            pass
        return redirect('/')