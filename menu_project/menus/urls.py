from django.urls import path

from .views import index, menu


app_name = 'menus'

urlpatterns = [
    path('<int:node_id>/', menu, name='menus'),
    path('', index, name='index')
]
