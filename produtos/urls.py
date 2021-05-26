from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form-produto', views.create_produto, name='create_produto'),
    path('form-produto', views.update_produto, name='update_produto'),
    path('categorias', views.categorias, name='categorias'),
       

]