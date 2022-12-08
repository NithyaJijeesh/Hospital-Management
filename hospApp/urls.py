
from django.urls import path
from . import views
#from django.contrib.auth import views 

urlpatterns = [

    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('user_home',views.user_home,name='user_home'),

    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('add_dept',views.add_dept,name='add_dept'),
    path('show_dept',views.show_dept,name='show_dept'),
    path('del_dept/<pk>',views.del_dept,name='del_dept'),

    path('add_qual',views.add_qual,name='add_qual'),
    path('show_qual',views.show_qual,name='show_qual'),
    path('del_qual/<pk>',views.del_qual,name='del_qual'),

    path('add_room',views.add_room,name='add_room'),
    path('show_room',views.show_room,name='show_room'),
    path('del_room/<pk>',views.del_room,name='del_room'),

    path('add_test',views.add_test,name='add_test'),
    path('show_test',views.show_test,name='show_test'),
    path('del_test/<pk>',views.del_test,name='del_test'),

    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('show_doctor',views.show_doctor,name='show_doctor'),
    path('edit_doctor/<pk>',views.edit_doctor,name='edit_doctor'),
    path('del_doctor/<pk>',views.del_doctor,name='del_doctor'),

    path('add_inpatient',views.add_inpatient,name='add_inpatient'),
    path('edit_inpatient/<pk>',views.edit_inpatient,name='edit_inpatient'),
    path('show_inpatient',views.show_inpatient,name='show_inpatient'),
    path('del_inpatient/<pk>',views.del_inpatient,name='del_inpatient'),

    path('add_outpatient',views.add_outpatient,name='add_outpatient'),
    path('edit_outpatient/<pk>',views.edit_outpatient,name='edit_outpatient'),
    path('show_outpatient',views.show_outpatient,name='show_outpatient'),
    path('del_outpatient/<pk>',views.del_outpatient,name='del_outpatient'),

    path('add_pathology',views.add_pathology,name="add_pathology"),
    path('show_pathology',views.show_pathology,name="show_pathology"),
    path('del_pathology/<pk>',views.del_pathology,name='del_pathology'),

    path('add_ipbill',views.add_ipbill,name='add_ipbill'),
    path('add_opbill',views.add_opbill,name='add_opbill'),
    path('show_bill',views.show_bill,name='show_bill'),
    path('del_ipbill/<pk>',views.del_ipbill,name='del_ipbill'),
    path('del_opbill/<pk>',views.del_opbill,name='del_opbill'),

    path('profile',views.profile,name="profile"),
    path('edit_profile/<pk>',views.edit_profile,name='edit_profile'),
    path('show_patient',views.show_patient,name = 'show_patient'),
    path('add_prescription',views.add_prescription,name = 'add_prescription'),
    path('show_details/<pk>',views.show_details,name = 'show_details'),

    #patient signup
    path('signup',views.signup,name = 'signup'),
    path('patient_home',views.patient_home,name = 'patient_home'),
    path('view_doctor',views.view_doctor,name = 'view_doctor'),
    path('book_appointment/<pk>',views.book_appointment,name = 'book_appointment'),
    path('pat_profile',views.pat_profile,name="pat_profile"),
    path('edit_pat_profile/<pk>',views.edit_pat_profile,name='edit_pat_profile'),


    #... appointment ...

    path('patient_appointment',views.patient_appointment,name = 'patient_appointment'),
    path('cancel_appointment/<pk>',views.cancel_appointment,name = 'cancel_appointment'),

    path('add_appointment', views.add_appointment,name = 'add_appointment'),
    path('view_appointment',views.view_appointment,name = 'view_appointment'),
    path('del_appointment/<pk>',views.del_appointment,name = 'del_appointment'),


    path('admin_appointment',views.admin_appointment,name='admin_appointment'),
    path('admin_view_appointment',views.admin_view_appointment,name='admin_view_appointment'),
    path('admin_approve_appointment',views.admin_approve_appointment,name='admin_approve_appointment'),
    path('approve_appointment/<pk>',views.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<pk>',views.reject_appointment,name='reject_appointment')
    # ....password change....
    #path('change_password',views.change_password,name = 'change_password'),



]