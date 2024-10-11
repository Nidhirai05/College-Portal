from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Notice,Event,Alumni,Student,Contact,Feedback
# Create your views here.

def home(request):
    # return HttpResponse("<h1> This is home page</h1>")
    #notice_list = Notice.objects.all()   #It will fetch data from Notice table
    notice_list = Notice.objects.order_by('-date')
    feedback_list=Feedback.objects.order_by('-date')[:3]
    # feedback_list=Feedback.objects.filter(rating='⁕⁕⁕⁕⁕').order_by('-date')[:4]
    context={
        "notice_key":notice_list,  #notice1,notice2,notice3
        "feedback_key":feedback_list
    }
    

    return render(request,'college_app/html/index.html',context)  #render is used to display a template
         

def about(request):
    return render(request,'college_app/html/about_us.html')

def feedback(request):
    if "session_key" not in request.session.keys():
        messages.error(request,"Unathorised Access")
        return redirect("login")
    if request.method=="GET":
      return render(request,'college_app/student/feedback.html')
    
    if request.method=="POST":
        u_name=request.POST["user_name"]
        u_email=request.POST["user_email"]
        u_rating=request.POST["rating"]
        u_remark=request.POST["remark"]
        feedback_obj=Feedback(name=u_name,email=u_email,rating=u_rating,remarks=u_remark)
        feedback_obj.save()
        messages.success(request,"Thank you for your feeedback")
        return redirect("feedback")
    

def contact(request):
    if request.method=="GET":
      return render(request,'college_app/html/contact.html')
    
    if request.method=="POST":
        u_name=request.POST["user_name"]
        u_email=request.POST["user_email"]
        u_phone=request.POST["user_phone"]
        u_query=request.POST["user_query"]
        contact_obj=Contact(name=u_name,email=u_email,phone=u_phone,query=u_query)
        contact_obj.save()
        messages.success(request,"Thank you contacting us we will reach you soon!!!")
        return render(request,'college_app/html/contact.html')
    

def login(request):
    if request.method=="GET":
      return render(request,'college_app/html/login.html')
    
    if request.method=="POST":
        s_id=request.POST["id"] #request.POST is a built in dictionary
        s_pass=request.POST["password"]
        print(f"{s_id+s_pass}")
        student_data=Student.objects.filter(id=s_id,password=s_pass)   #LHS=model attribute
        if len(student_data)>0:
            request.session["session_key"]=s_id   #storing value in session dictionary
            student_dict={"student_key":student_data[0]}
            return render(request,'college_app/student/student_home.html',student_dict)

        else:
            messages.error(request,"Invalid Id/password")
            return render(request,'college_app/html/login.html')

def courses(request):
    return render(request,'college_app/html/courses.html')

def facilities(request):
   return render(request,'college_app/html/facilities.html')

def bca(request):
    return render(request,'college_app/html/bca.html')

def mca(request):
    return render(request,'college_app/html/mca.html')

def btech(request):
    return render(request,'college_app/html/btech.html')

def internships(request):
    return render(request,'college_app/html/internships.html')

def event(request):
    event_list = Event.objects.all()
    event_dict = {"event_key":event_list}
    return render(request,'college_app/html/event.html',event_dict)


def alumni(request):
    alumni_list = Alumni.objects.all()
    alumni_dict = {"alumni_key":alumni_list}
    return render(request,'college_app/html/alumni.html',alumni_dict)

def edit_profile(request):
    if "session_key" not in request.session.keys():
        messages.error(request,"Unathorised Access")
        return redirect("login")
    
    if request.method=="GET":
        student_id=request.session["session_key"]  #getting student id from session
        student_object=Student.objects.get(id=student_id)
        student_dict={"student_key":student_object}
        return render(request,'college_app/student/student_edit_profile.html',student_dict)
    
    if request.method=="POST":
        student_id=request.session["session_key"]  #getting student id from session
        student_object=Student.objects.get(id=student_id)
        s_email=request.POST["email"]
        s_phone=request.POST["phone"]
        s_address=request.POST["address"]
        student_object.email=s_email
        student_object.phone=s_phone
        student_object.address=s_address
        student_object.save()
        student_dict={"student_key":student_object}
        return render(request,'college_app/student/student_home.html',student_dict)
    

def logout(request):
    if "session_key" not in request.session.keys():
        messages.error(request,"Unathorised Access")
        return redirect("login")
    del request.session["session_key"]
    return redirect("home")  #logical name of url path(endpoint)
    



# contact page 
# login page
# courses
# facilities
