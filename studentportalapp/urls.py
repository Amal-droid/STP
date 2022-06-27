from django.urls import path
from studentportalapp.views import book_list,book_create,book

urlpatterns=[
    path('',book_create),
    path('list/',book_list),
    path('<int:pk>',book)
    ]