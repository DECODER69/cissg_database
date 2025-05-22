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
    path('update_other/<str:id>', views.update_other, name='update_other'),
    path('update_vocational/<str:id>', views.update_vocational, name='update_vocational'),
    path('academic_input/', views.academic_input, name='academic_input' ),
    path('vocational_input/', views.vocational_input, name='vocational_input' ),
    path('other_input/', views.other_input, name='other_input' ),
    path('coastguard_input/', views.coastguard_input, name='coastguard_input' ),
    path('cglocal_input/', views.cglocal_input, name='cglocal_input' ),
    path('cgforeign_input/', views.cgforeign_input, name='cgforeign_input' ),
    path('education2/', views.education2, name='education2'),
    path('education3/', views.education3, name='education3'),
    path('education4/', views.education4, name='education4'),
    path('education5/', views.education5, name='education5'),
    path('education6/', views.education6, name='education6'),
    path('education7/', views.education7, name='education7'),
    path('update_coastguard/<str:id>', views.update_coastguard, name='update_coastguard'),
    path('update_cglocal/<str:id>', views.update_cglocal, name='update_cglocal'),
    path('update_cgforeign/<str:id>', views.update_cgforeign, name='update_cgforeign'),
    path('military_input/', views.military_input, name='military_input' ),
    path('mlocal"_input/', views.mlocal_input, name='mlocal_input' ),
    path('mforeign_input/', views.mforeign_input, name='mforeign_input' ),
    path('update_military/<str:id>', views.update_military, name='update_military'),
    path('update_mlocal/<str:id>', views.update_mlocal, name='update_mlocal'),
    path('update_mforeign/<str:id>', views.update_mforeign, name='update_mforeign'),
    
    path('shipboard_input/', views.shipboard_input, name='shipboard_input' ),
    path('collateral_input/', views.collateral_input, name='collateral_input' ),
    path('update_shipboard/<str:id>', views.update_shipboard, name='update_shipboard'),
    path('update_collateral/<str:id>', views.update_collateral, name='update_collateral'),
    
    path('shorebased_input/', views.shorebased_input, name='shorebased_input' ),
    path('collateral2_input/', views.collateral2_input, name='collateral2_input' ),
    path('update_shorebased/<str:id>', views.update_shorebased, name='update_shorebased'),
    path('update_collateral2/<str:id>', views.update_collateral2, name='update_collateral2'),
    
    path('gov_input/', views.gov_input, name='gov_input' ),
    path('nongov_input/', views.nongov_input, name='nongov_input' ),
    path('update_gov/<str:id>', views.update_gov, name='update_gov'),
    path('update_nongov/<str:id>', views.update_nongov, name='update_nongov'),
    
    
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



