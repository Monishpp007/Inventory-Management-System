from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_item, name='add_item'),
    path('purchase/', views.purchase_item, name='purchase_item'),
    path('sale/', views.sell_item, name='sale_item'),
    path('reports/', views.reports, name='reports'),
    path('reports/pdf/', views.pdf_reports, name='pdf_reports'),
]

