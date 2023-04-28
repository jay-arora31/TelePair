from django.shortcuts import render,get_object_or_404,redirect
from .models import *

def shop_profile_check(function):
    print("Heyyyyyyyyyyyyyyyyyyyyyyyyyy")
    def wrap(request, *args, **kwargs):
        shop_data=Shop.objects.filter(s_info__email=request.user.email)
        if shop_data is None:
            print(request.user,"dewiudfqiwudnon")
            print(request.META)
            return redirect('shop_profile_complete')
        else:
            return function(request, *args, **kwargs)
        
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap