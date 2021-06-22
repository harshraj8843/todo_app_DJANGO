from django.urls import path

from . import views
urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('done/', views.done.as_view(), name='done'),
    path('create/', views.create.as_view(), name='create'),

    # 'id' is the 'id' of todo data, which will be deleted
    path('mark_done/<int:id>/', views.mark_done.as_view(), name='mark_done'),

]
