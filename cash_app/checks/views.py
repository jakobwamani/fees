from django.shortcuts import render
from checks.models import *
from checks.forms import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request):
    
    return render(request,"index.html",{})

def register_school(request):
    context = {}
    # add the dictionary during initialization
    form = school_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('/') 
    else:
        context['form'] = form

    return render(request, "school.html",{'form':form})

def view_schools(request):
    school_names = school.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_schools.html", {'school_names':school_names})


def update_schools(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        school_name_record = school.objects.get(id=pk)
        form = school_form(request.POST or None, instance=school_name_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_schools.html",context=context_dict)

def delete_schools(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        school_name_to_delete = school.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        school_name_to_delete.delete()
    
    # return HttpResponseRedirect('/view_raw_material_names/')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_unchecked_slips(request):
    context = {}
    # add the dictionary during initialization
    
    if request.method == 'POST':

        form = unchecked_form(request.POST ,request.FILES) 

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('/') 
    else:
        form = unchecked_form()
    return render(request, "unchecked.html",{'form':form})

def view_unchecked_slips(request):
    un_checked_slips = un_checked.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_unchecked.html", {'un_checked_slips':un_checked_slips})

def update_unchecked_slips(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        slip_record = un_checked.objects.get(id=pk)
        form = unchecked_form(request.POST or None, instance=slip_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_unchecked.html",context=context_dict)
    
def delete_unchecked_slips(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        slip_to_delete = un_checked.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        slip_to_delete.delete()
    
    # return HttpResponseRedirect('/view_raw_material_names/')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))