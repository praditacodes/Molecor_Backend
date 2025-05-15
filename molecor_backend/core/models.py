from django.db import models
from django.utils.text import slugify

class CaseStudy(models.Model):
    CATEGORY_CHOICES = [
        ('TOM_PVC-O', 'TOM PVC-O Pipes'),
        ('FITTINGS', 'Fittings'),
        ('VALVES', 'Valves'),
    ]
    
    WATER_APPLICATION_CHOICES = [
        ('POTABLE', 'Potable water supply'),
        ('IRRIGATION', 'Irrigation'),
        ('INDUSTRIAL', 'Industrial'),
        ('WASTEWATER', 'Wastewater'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank for auto-generation
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='TOM_PVC-O')
    water_application = models.CharField(max_length=50, choices=WATER_APPLICATION_CHOICES, default='POTABLE')
    year = models.PositiveIntegerField(null=True, blank=True)
    region = models.CharField(max_length=100, blank=True)
    constructor = models.CharField(max_length=100, blank=True)
    promoter = models.CharField(max_length=100, blank=True)
    total_length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    specifications = models.JSONField(default=list, blank=True)
    content = models.TextField(blank=True)
    value = models.CharField(max_length=100, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    testimonial = models.TextField(blank=True)
    testimonial_author = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class CaseStudyImage(models.Model):
    case_study = models.ForeignKey(CaseStudy, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='case_studies/')
    caption = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.case_study.title}"

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')
    issued_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# class Certificate(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='certificates/')
#     issued_date = models.DateField()
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.title

# class CaseStudy(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date = models.DateField()
#     image = models.ImageField(upload_to='case_studies/', blank=True)

#     def __str__(self):
#         return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)

    summary = models.TextField()
    image = models.ImageField(upload_to='news/')
    published_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
