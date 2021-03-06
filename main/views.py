from django.shortcuts import render, redirect

# from django.http import HttpResponse

from django.views import View

from . import models

# Create your views here.

# home view or todo view
class home(View):

    def get(self, request):
        datas = []
        try:
            # get all todo data from database
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
            # passing todo datas to html
            'datas': datas
        })

# todos marked as done view
class done(View):

    def get(self, request):
        datas = []
        try:
            # get all done data from database
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
            # passing done datas to html
            'datas': datas
        })

# create view
class create(View):

    # get method will return add todo 'form'
    def get(self, request):
        return render(request, 'add.html')

    # post method will submit the add todo 'form'
    def post(self, request):
        try:
            # create a todo object
            data1 = models.Todo()

            # get todo title from form
            data1.name = request.POST.get('name')

            # get last date from form
            data1.last_date = request.POST.get('date')
            
            # save todo object
            data1.save()
        except:
            pass
        # after completion of form submission, user will be redirected to home page (todo page)
        return redirect('/')

# mark done button view
class mark_done(View):

    def get(self, request, id):
        try:
            # create todo object with given id
            data1 = models.Todo.objects.get(id=id)

            # create done object
            data2 = models.Done()

            # copy todo object title to done object title
            data2.name = data1.name

            # copy todo object last date to done object last date
            data2.last_date = data1.last_date

            # save done object
            data2.save()

            # delete todo object
            data1.delete()
        except:
            pass
        # redirect user to homepage
        return redirect('/')