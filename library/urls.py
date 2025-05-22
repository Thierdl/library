from django.urls import path
from .views import add_category, add_book, list_book


urlpatterns = [
    path('category/add/', add_category, name="add_category"),


    path('category/book/add/', add_book, name="add_book"),
    #path('category/book/delete/<int:book_id>/', delete_book, name="delete_book"),
    #path('category/book/update/<int:book_id>/', update_book, name="update_book"),
    path('category/book/list/<int:book_id>/', list_book, name="list_book"),

]