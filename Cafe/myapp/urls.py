from django.urls import path
from .views import *

urlpatterns = [
			path('', index, name = "index"),
			path('about/', about, name = "about"),
			path('products/', products, name = "products"),
			path('store/', store, name = "store"),

			path('register/', registerUser, name = "register"),
			path('login/', loginUser, name = "login"),
			path('logout/', logoutUser, name = "logout"),
			path('order_det/', OderDetails, name = "order_det"),
			path('contact/',  contact, name = "contact")

]