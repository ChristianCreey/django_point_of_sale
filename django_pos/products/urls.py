from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    # List categories
    path('categories', views.CategoriesListView, name='categories_list'),
    # Add category
    path('categories/add', views.CategoriesAddView, name='categories_add'),
]
