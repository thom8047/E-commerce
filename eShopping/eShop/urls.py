from django.urls import path
from . import views

#from .views import PageView


urlpatterns = [
    #path(r'admin/', admin.site.urls),
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    # Need to have user urls as well
    #path('users/login/', views.store, name="store"),
]