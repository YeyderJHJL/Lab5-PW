from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # name: para enlace <a href="{% url 'index' %}">Home</a>.
    path('books/', views.BookListView.as_view(), name="books"),
]