from django.contrib import admin
from .models import Notice,Contact,Feedback,Event,Alumni,Student,Consultancy


class Feedback_Admin(admin.ModelAdmin):
    list_display=['name','email','rating','remarks','date']
    list_filter=('rating','name') #Feedback model attributes
    #search_fields=('city')

class Alumni_Admin(admin.ModelAdmin):
    list_display=['name','course','completion_year','email','phone'] #Alumni model attributes
    list_filter=('completion_year','course')

class Student_Admin(admin.ModelAdmin):
    list_display=['name','course','email','phone'] #Alumni model attributes
    search_fields=('course',)


class Contact_Admin(admin.ModelAdmin):
    list_display=['name','email','phone','query']

# class Event_Admin(admin.ModelAdmin):
#     list_display=['event_name','event_venue','event_organizer']

# class Consultancy_Admin(admin.ModelAdmin):
#     list_display=['cname','email','phone','workarea']


# Register your models here.
admin.site.register(Notice)
admin.site.register(Contact,Contact_Admin)
admin.site.register(Feedback,Feedback_Admin)
admin.site.register(Event)
admin.site.register(Alumni,Alumni_Admin)
admin.site.register(Student,Student_Admin)
admin.site.register(Consultancy)

admin.site.site_header="College Admin Dashboard"
admin.site.site_title="College App"
admin.site.index_title="Spread the joy of learning"



