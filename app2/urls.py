from django.urls import path
from .import views

urlpatterns =[
    path('reg',views.registration,name='register'),
    path('log',views.logins,name='log'),
    # path('product',views.product_details,name='product'),
    path('list',views.product_list,name='list'),
    path('shop',views.shop_view,name='shop'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('cart/<int:i>',views.addToCart,name='cart'),
    path('remove',views.deletecart,name='remove'),
    path('rmv/<int:j>',views.remove,name='rmv'),
    path('userlogout',views.userlogout,name='userlogout'),
    # path('address',views.address,name='address'),
    path('payment',views.payment,name='payment'),
    path('increase/<int:k>',views.increase_qty,name='increase'),
    path('decrease/<int:l>',views.decrease_qty,name='decrease'),
    path('address',views.save_address,name='address')
]