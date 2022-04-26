from django.urls import path, include

from sole_market import views

urlpatterns = [
    path('list-products/', views.ProductsLists.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view()),
    path('list-categories/', views.CategoryLists.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view()),
]