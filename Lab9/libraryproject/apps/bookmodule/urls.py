from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"), 
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links),
    path('html5/text/formatting', views.formatting),
    path('html5/listing', views.listing),
    path('html5/tables', views.tables),
    path('search', views.search, name='books.search'),
    path('lab8/task7', views.lab8_task7, name='books.lab8_task7'),
    path('lab9/task1', views.lab9_task1, name='books.lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='books.lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='books.lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='books.lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='books.lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='books.lab9_task6')
    ] 




