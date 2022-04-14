from django.urls import path

import dinamicform.views as views

app_name = 'dinamicform'

urlpatterns = [
    path('', views.index, name='index'),
    path('done/', views.done, name='done'),
    path('done/clear_bd/', views.clear_bd, name='clear_bd'),
]
