from django.contrib import admin
from .models import Project, Skill,ResumeEntry, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ResumeEntry)
admin.site.register(ContactMessage)