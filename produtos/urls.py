from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form-produto', views.create_produto, name='create_produto'),
    path('form-produto', views.update_produto, name='update_produto'),
    path('categorias', views.categorias, name='categorias'),
    path('form-categorias', views.create_categorias, name='create_categorias'),
    path('form-categorias', views.update_categorias, name='update_categorias'),   

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)