"""pragati URL Configuration

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
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
      
      path('',views.home,name='home' ),
      path('login/',views.login,name='login' ),
      path('logout/',views.logout,name='logout' ),
      path('register_normal/',views.register_normal,name='register_normal' ),
      path('register_shop/',views.register_shop,name='register_shop' ),
      path('shop_profile_complete/',views.shop_profile_complete,name='shop_profile_complete' ),
      path('shop_home/',views.shop_home,name='shop_home' ),
      path('shop_list/',views.shop_list,name='shop_list' ),
      path('shop_detail/<int:id>',views.shop_detail,name='shop_detail' ),
      path('shop_edit_profile/',views.shop_edit_profile,name='shop_edit_profile' ),
      path('filter_shop/',views.filter_shop,name='filter_shop' ),

      

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
