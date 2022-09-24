from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from checks import views

urlpatterns = [
    path('',views.index,name='index'),
    path('school/',views.register_school,name='reg_school'),
    path('view_schools/',views.view_schools,name='see_schools'),
    path('update_schools/',views.update_schools,name='update_schools'),
    path('delete_schools/',views.delete_schools,name='remove_school'),
    path('status/',views.define_status,name='set_status'),
    path('view_status/',views.view_status,name='see_status'),
    path('update_status/',views.update_status,name='change_status'),
    path('delete_status/',views.delete_status,name='remove_status'),
    path('slips/',views.get_slips,name='get_slips'),
    path('view_slips/',views.view_slips,name='see_slips'),
    path('update_slip/',views.update_slips,name='update_slips'),
    path('delete_slip/',views.delete_slip,name='remove_slip'),
    
]