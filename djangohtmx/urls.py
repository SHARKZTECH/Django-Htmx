"""djangohtmx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/', create_book, name='create-book'),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    path('htmx/book/<pk>/update/', update_book, name="update-book"),
    path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    
    path('htmx/books/',books,name="books"),

]
