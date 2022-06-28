# from django.urls import path
# from studentportalapp.views import book_list,book_create,book

# urlpatterns=[
#     path('',book_create),
#     path('list/',book_list),
#     path('<int:pk>',book)
#     ]

from django.urls import path
from studentportalapp.views import BookCreate, BookList,BookDetails
urlpatterns=[
    path('list/',BookList.as_view()),
    path('',BookCreate.as_view()),
    path('<int:pk>',BookDetails.as_view()) 
    ]