from django.urls import path
from . import views,consultancy_views

urlpatterns=[
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("feedback/",views.feedback,name="feedback"),
    path("login/",views.login,name="login"),
    path("contact/",views.contact,name="contact"),
    path("courses/",views.courses,name="courses"),
    path("facilities/",views.facilities,name="facilities"),
    path("bca/",views.bca,name="bca"),
    path("mca/",views.mca,name="mca"),
    path("btech/",views.btech,name="btech"),
    path("internships/",views.internships,name="internships"),
    path("event/",views.event,name="event"),
    path("alumni/",views.alumni,name="alumni"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("logout/",views.logout,name="logout"),
    path("c_registration/",consultancy_views.registration,name="c_registration"),
    path("c_login/",consultancy_views.c_login,name="c_login"),
    path("consultancy_edit_profile/",consultancy_views.consultancy_edit_profile,name="consultancy_edit_profile"),
    path("c_logout/",consultancy_views.c_logout,name="c_logout"),
    
]