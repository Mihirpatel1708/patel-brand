"""
URL configuration for patel_brand project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from patel_brand import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('men/',views.men),
    path('women/',views.women),
    path('cart/',views.cart_view,name='cart'),
    # path('contact-us/',views.contact),
    path('about-us/',views.about),
    path('register/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout',views.logout_,name='logout'),
    path('profile_/',views.profile,name='profile'),
    path('addtocart/<int:id>/<str:category>',views.addtocart,name='addtocart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('increase_quantity/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('checkout',views.checkout_,name='checkout_'),
    path('order/',views.order,name='order'),
    path('trackord/',views.trackorder,name='trackorder'),
    # path('search/',views.search,name='search'), 
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

