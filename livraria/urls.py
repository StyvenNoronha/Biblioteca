from django.contrib import admin
from django.urls import path
from livraria.views import home,sobre,logout_user,create_user,deleteBook,create_book,update_book
urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('logout/', logout_user, name='logout'),
    path('create/', create_user, name="create"),
    path('createBook/', create_book, name="createBook"),
    path('delete/<int:id>/', deleteBook, name="delete"),
    path('update/<int:id>/', update_book, name="update"),
]