from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings


from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path

app_name = 'activities'



urlpatterns = [
    path('', views.index, name='index'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('signup/', views.signup, name='signup'),
    path('signup_function/', views.signup_function, name='signup_function'),
    path('login/', views.login, name='login'),
    path('signin_function/', views.signin_function, name='signin_function'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path ('education/', views.education, name='education'),
    path ('delete_item/<str:serialnumber>', views.delete_item, name='delete_item'),
    path('update_table1/<str:id>', views.update_table1, name='update_table1'),
    path('academic_input/', views.academic_input, name='academic_input' )
 
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



