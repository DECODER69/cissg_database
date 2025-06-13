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
    path('logout_view/', views.logout_view, name='logout_view'),
    path('signup/', views.signup, name='signup'),
    path('signup_function/', views.signup_function, name='signup_function'),
    path('login/', views.login, name='login'),
    path('signin_function/', views.signin_function, name='signin_function'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_input/', views.dashboard_input, name='dashboard_input'),
    path('dashboard_input_update/<str:id>', views.dashboard_input_update, name='dashboard_input_update'),
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
    path('education8/', views.education8, name='education8'),
    path('education9/', views.education9, name='education9'),
    path('education10/', views.education10, name='education10'),
    path('education11/', views.education11, name='education11'),
    path('update_coastguard/<str:id>', views.update_coastguard, name='update_coastguard'),
    path('update_cglocal/<str:id>', views.update_cglocal, name='update_cglocal'),
    path('update_cgforeign/<str:id>', views.update_cgforeign, name='update_cgforeign'),
    path('military_input/', views.military_input, name='military_input' ),
    path('appointment_input/', views.appointment_input, name='appointment_input'),
    path('appointment_update/<str:id>', views.appointment_update, name='appointment_update'),
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
    
    
    path('award_input/', views.award_input, name='award_input' ),
    path('commendation_input/', views.commendation_input, name='commendation_input' ),
    path('appreciation_input/', views.appreciation_input, name='appreciation_input' ),
    path('plaque_input/', views.plaque_input, name='plaque_input' ),
    path('update_award/<str:id>', views.update_award, name='update_award'),
    path('update_commendation/<str:id>', views.update_commendation, name='update_commendation'),
    path('update_appreciation/<str:id>', views.update_appreciation, name='update_appreciation'),
    path('update_plaque/<str:id>', views.update_plaque, name='update_plaque'),
    
    path('maward_input/', views.maward_input, name='maward_input' ),
    path('mcommendation_input/', views.mcommendation_input, name='mcommendation_input' ),
    path('mappreciation_input/', views.mappreciation_input, name='mappreciation_input' ),
    path('mplaque_input/', views.mplaque_input, name='mplaque_input' ),
    path('update_maward/<str:id>', views.update_maward, name='update_maward'),
    path('update_mcommendation/<str:id>', views.update_mcommendation, name='update_mcommendation'),
    path('update_mappreciation/<str:id>', views.update_mappreciation, name='update_mappreciation'),
    path('update_mplaque/<str:id>', views.update_mplaque, name='update_mplaque'),
    
  
    path('ccommendation_input/', views.ccommendation_input, name='ccommendation_input' ),
    path('cappreciation_input/', views.cappreciation_input, name='cappreciation_input' ),
    path('cplaque_input/', views.cplaque_input, name='cplaque_input' ),
    path('update_ccommendation/<str:id>', views.update_ccommendation, name='update_ccommendation'),
    path('update_cappreciation/<str:id>', views.update_cappreciation, name='update_cappreciation'),
    path('update_cplaque/<str:id>', views.update_cplaque, name='update_cplaque'),
    
    path('upload_image/', views.upload_image, name='upload_image'),
    
    path('career_input/', views.career_input, name='career_input' ),
    path('dependents_input/', views.dependents_input, name='dependents_input'),
    path('triple/', views.triple, name='triple'),
    
    
    
    # ADMINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



