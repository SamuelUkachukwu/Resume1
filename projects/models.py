from django.db import models
from cloudinary.models import CloudinaryField
from multiselectfield import MultiSelectField


LANG_CHOICE = (
    ('html', 'HTML-5'),
    ('css', 'CSS-3'),
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('django', 'Django'),
    ('flask', 'Flask'),
    ('bootstrap', 'Bootstrap')
    )


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True,)
    languages = MultiSelectField(choices=LANG_CHOICE)
    project_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=550, blank=True)
    github_link = models.CharField(max_length=200)
    host_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    github = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    profession = models.TextField(max_length=400)
    skills = models.TextField(max_length=400)
    engage_me = models.TextField(max_length=400)
    about_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name