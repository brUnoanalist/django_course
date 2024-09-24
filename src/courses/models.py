from django.db import models

# Create your models here.
class AccessRequirement(models.TextChoices):
    ANYONE = "any","Any"
    EMAIL_REQUIRED= "email_required","Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub","Published"
    COMING_SOON= "soon","Coming Soon"
    DRAFT = "draft", "Draft"
class Course(models.Model):
    title = models.CharField(max_length=255)  # Título del curso
    description = models.TextField()  # Descripción detallada
    #publish_date = models.DateField()  # Fecha de publicación
    #image = models.ImageField(upload_to='course_images/', blank=True, null=True)  # Imagen del curso
    access = models.CharField(max_length=50, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED) # Si el curso es de acceso público o no
    status = models.CharField(max_length=50, choices=PublishStatus.choices, default=PublishStatus.DRAFT)  # Estado del curso

    @property
    def is_published(self):
       return self.status == PublishStatus.PUBLISHED
       