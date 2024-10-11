from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Consultancy
def registration(request):
    if request.method=="GET":
        return render(request,'college_app/consultancy/consultancy_registration.html')
    
    if request.method=="POST":
        id=request.POST["cid"]
        password=request.POST["password"]
        name=request.POST["cname"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        area=request.POST["area"]
        address=request.POST["address"]
        cobj=Consultancy(id=id,password=password,cname=name,email=email,phone=phone,work_area=area,address=address)
        cobj.save()
        messages.success(request,"Registration done successfully. Now,You can do login!!👍")
        return redirect("c_registration")
    

def c_login(request):
    if request.method=="GET":
      return render(request,'college_app/consultancy/c_login.html')
    
    if request.method=="POST":
        c_id=request.POST["id"] #request.POST is a built in dictionary
        c_pass=request.POST["password"]
        consultancy_data=Consultancy.objects.filter(id=c_id,password=c_pass)   #LHS=model attribute
        if len(consultancy_data)>0:
            request.session["session_key"]=c_id   #storing value in session dictionary
            consultancy_dict={"consultancy_key":consultancy_data[0]}
            return render(request,'college_app/consultancy/c_home.html',consultancy_dict)

        else:
            messages.error(request,"Invalid Id/password")
            return render(request,'college_app/consultancy/c_login.html')
        

def consultancy_edit_profile(request):
    if request.method=="GET":
        consultancy_id=request.session["session_key"]  #getting student id from session
        consultancy_object=Consultancy.objects.get(id=consultancy_id)
        consultancy_dict={"consultancy_key":consultancy_object}
        return render(request,'college_app/consultancy/consultancy_edit_profile.html',consultancy_dict)
    
    if request.method=="POST":
        consultancy_id=request.session["session_key"]  #getting student id from session
        consultancy_object=Consultancy.objects.get(id=consultancy_id)
        c_email=request.POST["email"]
        c_phone=request.POST["phone"]
        c_address=request.POST["address"]
        consultancy_object.email=c_email
        consultancy_object.phone=c_phone
        consultancy_object.address=c_address
        consultancy_object.save()
        consultancy_dict={"consultancy_key":consultancy_object}
        return render(request,'college_app/consultancy/c_home.html',consultancy_dict)

def c_logout(request):
    del request.session["session_key"]
    return redirect("c_login")  #logical name of url path(endpoint)