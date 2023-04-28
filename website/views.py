from django.shortcuts import render
from .forms import *
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.contrib.auth import logout,login as auth_login
from .forms import *
import django.contrib.auth as auth1
from .decorators import *
from django.http import JsonResponse

# Create your views here.

from functools import wraps
from django.http import HttpResponseRedirect

def shop_check(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        print("I am decorato================================")
        shop_data=Shop.objects.filter(s_info__email=request.user.email)
        print(shop_data)
        if shop_data:
            return function(request, *args, **kwargs)
        else:
             return redirect('shop_profile_complete')

  return wrap
def home(request):
    return render(request,'home.html')
def logout(request):
    # Log out the user.
    auth1.logout(request)
    # Return to homepage.
    return redirect('login')

def login(request):   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            print(user,"--------------------------,")
            form = auth_login(request, user)

            messages.success(request, f' wecome {username} !!')
            if user.is_shop:
                return redirect('shop_home')
            elif user.is_customer:
                return redirect('home')


        else:
            messages.info(request, f'account done not exit plz sign in')
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})



def register_normal( request):
    if request.method =='POST':
            form =CustomUserCreationForm(request.POST)
            if form.is_valid():
                print("form is va;id")
                user=form.save(commit =False)
                user.email =user.email.lower()
                user.username=user.email
                user.active =True
                user.is_customer=True
                user.save()
    
                messages.success(request,"Account Registered Successfully")
                return redirect('home')
            else:
                messages.success(request,"Invalid Input")
                return redirect('register_normal')

    form=CustomUserCreationForm()
    return render(request,'register_normal.html',{'form':form})


def register_shop( request):
    if request.method =='POST':
            form =CustomUserCreationForm(request.POST)
            if form.is_valid():
                print("form is va;id")
                user=form.save(commit =False)
                user.email =user.email.lower()
                user.username=user.email
                user.active =True
                user.is_shop=True
                user.save()
                messages.success(request,"Account Registered Successfully")
                return redirect('home')
            else:
                messages.success(request,"Invalid Input")
                return redirect('register_normal')

    form=CustomUserCreationForm()
    return render(request,'register_shop.html',{'form':form})
#================================================================Custom User Function =========================================================#

def shop_list(request):

    result=Shop.objects.all()
    tvbrands=TvBrands.objects.all()
    if request.method=='POST':
            location = request.POST['location']
            print("Location",location)
            tvbrands12 = request.POST['tvbrands']
            print(tvbrands)
            result=ShopBrands.objects.all()
            if location is not None :
                 result=result.filter(tv_shop__s_city=location)
            print("=\========================resitl location",result)
            if tvbrands12 is not None and tvbrands12!='Select Tv Brand':
                 
                 result=result.filter(tv_brand=tvbrands)
            print("=\========================resitl tvbrands",result)
            tvbrands11=TvBrands.objects.all()
            return render(request,'customer/service1.html',{'shop':result,'tvbrands':tvbrands11})
    return render(request,'customer/service.html',{'shop':result,'tvbrands':tvbrands})

def shop_detail(request,id):
    shop=Shop.objects.get(s_info__id=id)
    shop_brand=ShopBrands.objects.filter(tv_shop__s_info__id=id)
    print(shop_brand)
    shop_service=ShopService.objects.filter(service_shop__s_info__id=id)
    return render(request,'customer/shop_detail.html',{'shop':shop,'shop_brand':shop_brand,'shop_service':shop_service})

    
#===============================================================SHOP Functions ==========================================================#

def shop_profile_complete(request):
    email=request.user
    shop=Shop.objects.filter(s_info__email=email)
    if not shop:
        if request.method=='POST':
            form=ShopProfileCompleteForm(request.POST,request.FILES)
            tv=request.POST.getlist('tvbrands')
            service=request.POST.getlist('tvservices')
            info=CustomUser.objects.get(email=request.user)
            print("I am outer form")
            if form.is_valid():
                print('i am in inner form')
                profile_form=form.save(commit=False)
                print(profile_form.s_image)
                profile_form.s_info=info
                profile_form.save()
                print("here is tv ")
                print(tv)
                for i in tv:
                    print("shop tv",i)
                    obj=ShopBrands(tv_brand=i,tv_shop=profile_form)
                    obj.save()
                for i in service:
                    obj1=ShopService(service_shop=profile_form,service_category=i)
                    obj1.save()
                    return redirect('shop_home')
    else:
        print("hi there is problwm")
        return redirect('shop_home')

            
    tv_brands=TvBrands.objects.all()
    tv_service=TVServices.objects.all()
    form=ShopProfileCompleteForm()
    return render(request,'shop/shop_profile_complete.html',{'form':form,'tv_brands':tv_brands,'tv_service':tv_service})


@shop_check
def shop_home(request):
    shop=Shop.objects.get(s_info__email=request.user)
    form=editShopProfileComplete(instance=shop)

    return render(request,'shop/shop_home.html',{'form':form,'shop':shop})

@shop_check
def shop_edit_profile(request):
    shop=Shop.objects.get(s_info__email=request.user)
    form=ShopProfileCompleteForm(instance=shop)
    return render(request,'shop/edit_profile.html',{'form':form})


def filter_shop(request):
          print("Hey I am in function")
          data = {}
          if request.GET.get('location', None) is not None:
                    location = request.GET.get('location')
                    serv=Shop.objects.filter(s_city=location)
                    print("=====================",serv)
                    subject_data=[]
                    for i in serv:
                        subject_data.append(i.s_name)
                        data['result'] = True
                        data['message'] = "Note posted successfully"
                        data['subject_data']=subject_data
                        ...
                    if request.is_ajax():
                        return JsonResponse(data)
                    else:
                        return JsonResponse(data)