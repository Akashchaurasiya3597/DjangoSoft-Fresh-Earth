
from django.urls import path
from DjangoSoftApp import views

urlpatterns = [
    path('',views.index_View,name='index'),
    path('index/',views.index_View,name='index'),
    path('about_us/',views.about_us_View,name='about_us'),
    path('shop_Vegetable/', views.Shop_Vegetable_View, name='shop_Vegetable'),
    path('shop_Fruit/', views.Shop_Fruit_View, name='shop_Fruit'),
    path('vegetablesDetail/<pk>',views.vegetables_detail_View,name='vegetablesDetail'),
    path('Popularity_vegetable/',views.Popularity_vegetable_view,name='Popularity_vegetable'),
    path('High_Low_vegetable/',views.High_Low_vegetable_view,name='High_Low_vegetable'),
    path('Low_High_vegetable/',views.Low_High_vegetable_view,name='Low_High_vegetable'),
    path('BestSelling_vegetable/',views.BestSelling_vegetable_view,name='BestSelling_vegetable'),
    path('Popularity_fruit/',views.Popularity_fruit_view,name='Popularity_fruit'),
    path('High_Low_fruit/',views.High_Low_fruit_view,name='High_Low_fruit'),
    path('Low_High_fruit/',views.Low_High_fruit_view,name='Low_High_fruit'),
    path('BestSelling_fruit/',views.BestSelling_fruit_view,name='BestSelling_fruit'),
    path('fruitsDetail/<pk>',views.fruits_detail_View,name='fruitsDetail'),
    path('milksDetail/<pk>', views.milks_detail_View, name='milksDetail'),
    path('WishList/',views.Wish_list_View,name='WishList'),
    path('cart/',views.Cart_view,name='cart'),
    path('Checkout/',views.Checkout_view,name='Checkout'),
    path('MyAccount/', views.My_account_View, name='MyAccount'),
    path('contact/',views.Contact_View,name='contact'),
    path('feedback/',views.Feedback_View,name='feedback'),
    path('gallery/',views.Gallery_View,name='gallery'),

]

