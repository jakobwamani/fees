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
    path('unchecked/',views.get_unchecked_slips,name='get_unchecked'),
    path('view_unchecked/',views.view_unchecked_slips,name='see_unchecked_slips'),
    path('update_unchecked/',views.update_unchecked_slips,name='update_new_slips'),
    path('delete_unchecked/',views.delete_unchecked_slips,name='remove_slip'),
]