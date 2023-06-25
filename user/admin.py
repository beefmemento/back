from django.contrib import admin
from .models import Defaultuser, Subject, User_to_subject
# Register your models here.

admin.site.register(Defaultuser)
admin.site.register(Subject)

admin.site.register(User_to_subject)