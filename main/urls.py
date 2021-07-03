from django.urls import path

from . import views
urlpatterns = [

    # todo path
    path('', views.home.as_view(), name='home'),

    # done path
    path('done/', views.done.as_view(), name='done'),

    # create new todo path
    path('create/', views.create.as_view(), name='create'),

    # 'id' is the 'id' of todo data, which will be deleted
    path('mark_done/<int:id>/', views.mark_done.as_view(), name='mark_done'),

]
