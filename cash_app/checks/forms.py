from checks.models import school
from datetimewidget.widgets import DateTimeWidget
import datetime
from checks.models import *
from django import forms
import datetime
from django.utils import timezone

school_query = school.objects.all()

class school_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	school_name = forms.CharField(max_length=100)
		
	class Meta:
		model = school
		fields = ["date","time","school_name"]

class unchecked_form(forms.ModelForm):
    
	school_name = forms.ModelChoiceField(queryset = school_query)
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	photo = forms.ImageField()
	
	class Meta:
		model = un_checked
		fields = ["date","time","school_name","photo"]