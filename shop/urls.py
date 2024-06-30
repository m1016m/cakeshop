
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('order/', views.order, name='order'),
#     path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
#     path('order_history/', views.order_history, name='order_history'),
#     path('order_increase/<int:order_id>/', views.order_increase, name='order_increase'),
#     path('order_decrease/<int:order_id>/', views.order_decrease, name='order_decrease'),
#     path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),
#     path('order_confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('order/', views.order, name='order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_increase/<int:order_id>/', views.order_increase, name='order_increase'),
    path('order_decrease/<int:order_id>/', views.order_decrease, name='order_decrease'),
    path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('order_confirm/<int:order_id>/', views.order_confirm, name='order_confirm'),
    path('add_item_to_order/<int:order_id>/', views.add_item_to_order, name='add_item_to_order'),
]
