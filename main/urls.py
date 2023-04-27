
from django.urls import path
from . import views
from django.conf.urls import url
from main.views import *
app_name="main"

urlpatterns = [
        path("",homepage.as_view(),name="homepage"),
        path("register_as_company/",register_as_company.as_view(), name="register_as_company"), 
        path("register_as_normal/", register_as_normal.as_view(), name="register_as_normal"), 
        path("login/",login_request.as_view(), name="login"),
        path("logout/", logout_request.as_view(), name="logout"), 
        path("company_profile/",company_profile.as_view(),name="company"),
        path("student_profile/",student_profile.as_view(),name="student"),
        path("profile/edit_company/",edit_company_profile.as_view(),name="edit_company_profile"),
        path("profile/edit_student/",edit_student_profile.as_view(),name="edit_student_profile"),
        path("change-password/",change_password.as_view(),name="change_password"),

        path("post_service/", post_service.as_view(), name='post_a_job'),
        path("edit_internship/<int:pk>/",views.edit_this_internship,name="edit_this_internship"),
        path("delete_internship/<int:pk>/", views.delete_internship, name = "delete_internship"),
        path('service_posted/', service_posted.as_view(), name='internship_list'),

        
        path("all_services/",all_services.as_view(),name="all_jobs"),
   
        path("service_detail/<int:internship_id>/",views.service_detail,name="service_detail"),
        path("filter_shop/",views.filter_shop,name="filter_shop"),
        
        url(r'^$', views.homepage, name='homepage'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                views.activate, name='activate'),

]
