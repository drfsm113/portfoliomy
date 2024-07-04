from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Project, Skill, ContactMessage, AboutMe



admin.site.register(Project)

admin.site.register(Skill)

admin.site.register(ContactMessage)

admin.site.register(AboutMe)