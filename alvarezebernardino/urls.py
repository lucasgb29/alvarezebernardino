from django.urls import path
from alvarezebernardino.views import index,servicos

urlpatterns = [
    path('',index, name= 'index'),
    path('servicos/',servicos, name='servicos')
]
