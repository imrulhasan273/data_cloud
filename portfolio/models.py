from django.db import models

class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin_link = models.URLField(null=True, blank=True)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    research_gate_link = models.URLField(null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class Summary(models.Model):
    content = models.TextField()

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_image = models.ImageField(upload_to='company_images/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    institution_image = models.ImageField(upload_to='institution_images/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Publication(models.Model):
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    publication_date = models.DateField()
    link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

class ProblemSolving(models.Model):
    platform = models.CharField(max_length=100)
    profile_link = models.URLField()
    problems_solved = models.IntegerField()
    site_image = models.ImageField(upload_to='site_images/')

class Certification(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    organization_image = models.ImageField(upload_to='organization_images/', null=True, blank=True)
    date_obtained = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

class Reference(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    relation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SkillsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SkillsSubcategory(models.Model):
    category = models.ForeignKey(SkillsCategory, on_delete=models.CASCADE, related_name='subcategories')
    value = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skill_icons/', null=True, blank=True)

    def __str__(self):
        return self.value

# py -3.10 manage.py makemigrations
# py -3.10 manage.py migrate




