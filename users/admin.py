from django.contrib import admin
from .models import Passport, Person, Post, UserProfile, Student, Course


admin.site.register(Passport)
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Course)
