from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="Skill level as percentage (0–100)")

    def __str__(self):
        return f"{self.name} - {self.level}%"


class ResumeEntry(models.Model):
    ENTRY_TYPES = [
        ('experience', 'Experience'),
        ('education', 'Education'),
    ]

    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPES)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.organization}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=150,blank=False)
    message = models.TextField(blank=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"