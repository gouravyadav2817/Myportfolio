from django.shortcuts import render,redirect 
from django.urls import reverse
# Render the full single-page portfolio site
from .models import Project, Skill, ResumeEntry, ContactMessage # Make sure Skill is imported
from .forms import ContactForm
from django.contrib import messages
from datetime import datetime
def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    resume_entries = ResumeEntry.objects.all().order_by('-start_date')  # Optional: Chronological sorting
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out! Your message was sent successfully. I’ll get back to you as soon as possible.")
            return redirect(reverse('index') + "#contact")  # or wherever your home view is named
           
    context = {
        'name': "Gourav Yadav",
        'title': "Full-Stack Developer | Python Django Enthusiast | Data Analytics",
        'projects': projects,
        'skills': skills,
        'resume_entries': resume_entries,
        'form': form,
        'year':datetime.now().year
    }
    return render(request, 'portfolio/index.html', context)
