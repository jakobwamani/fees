from django.shortcuts import render
from checks.models import *
from checks.forms import *
import snoop
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

def define_status(request):
    context = {}
    # add the dictionary during initialization
    
    if request.method == 'POST':

        form = status_form(request.POST ,request.FILES) 

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('/') 
    else:
        form = status_form()

    return render(request, "status.html",{'form':form})

def view_status(request):
    modes = status.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_status.html", {'modes':modes})

def update_status(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        status_record = status.objects.get(id=pk)
        form = status_form(request.POST or None, instance=status_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_status.html",context=context_dict)

def delete_status(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        status_to_delete = status.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        status_to_delete.delete()
    
    # return HttpResponseRedirect('/view_raw_material_names/')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def get_slips(request):
    context = {}
    # add the dictionary during initialization
    
    if request.method == 'POST':

        form = slip_form(request.POST ,request.FILES) 

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('/') 
    else:
        form = slip_form()
        
    return render(request, "slips.html",{'form':form})

def view_slips(request):
    slips = slip.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_slips.html", {'slips':slips})

def update_slips(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        slip_record = slip.objects.get(id=pk)
        form = slip_form(request.POST or None, instance=slip_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_slip.html",context=context_dict)
    
def delete_slip(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        slip_to_delete = slip.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        slip_to_delete.delete()
    
    # return HttpResponseRedirect('/view_raw_material_names/')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

