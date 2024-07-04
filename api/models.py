from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

def generate_unique_slug(instance, field):
    base_slug = slugify(getattr(instance, field))
    unique_slug = base_slug
    model_class = instance.__class__
    num = 1
    while model_class.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{num}"
        num += 1
    return unique_slug

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects')
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'title')
        super().save(*args, **kwargs)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'name')
        super().save(*args, **kwargs)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_messages')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'name')
        super().save(*args, **kwargs)

class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    resume = models.FileField(upload_to='resumes', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='about_me')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'user')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "About Me"
