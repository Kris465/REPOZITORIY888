from django.contrib import admin
from .models import AboutPage, Grade, Course, ContactPage, Student, Notice, Teacher

# Register your models here.
admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Notice)
admin.site.register(Teacher)
