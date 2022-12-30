from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.core.validators import MaxValueValidator, MinValueValidator
import secrets
# Create your models here.

class User(AbstractUser):
    is_class_agent = models.BooleanField(default=False)
    is_organisor = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    organization = models.ForeignKey("organization", on_delete=models.SET_NULL, null=True, blank=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class homework(models.Model):
    homework = models.CharField(max_length=600)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
    date = models.DateField(null =True)
    choices = [
    ('Initialized', 'Initialized'),
    ('Review', 'Review'),
    ('Completed', 'Completed'),
    ('Re-do', 'Re-do'),
    ('Falied', 'Falied')]
    status = models.CharField(max_length=11, choices=choices, default=1)
    
    class Meta:
        verbose_name_plural = "homework"

class VOW(models.Model):
    Affirmation = models.CharField(max_length=600)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
    date = models.DateField(null =True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.Affirmation}"
    
    class Meta:
        verbose_name_plural = "Affirmation"
    
class classes(models.Model):
    std = models.CharField(max_length=2, null=True)
    sec = models.CharField(max_length=2, null=True)
    
    def __str__(self):
        return f"{self.std},{self.sec}"
    
    class Meta:
        verbose_name_plural = "classes"
        
class customers(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=45, null=True, unique=True)
    phone = models.CharField(max_length=17, null=True, unique=True)
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(15)],null=True)
    agent = models.ForeignKey("Agent",blank=True, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey("organization", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("usercategory", on_delete=models.CASCADE, blank=True, null=True)
    classes = models.ForeignKey("classes", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.name},{self.email},{self.classes}"
    
    class Meta:
        verbose_name_plural = "Customers"

class score(models.Model):
    score = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(15)],null=True)
    date = models.DateField()
    email = models.ForeignKey("customers", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.score},{self.date},{self.email}"
    
    class Meta:
        verbose_name_plural = "score"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey("organization", on_delete=models.SET_NULL,null=True)
    classes = models.ManyToManyField("classes", blank=True)
    def __str__(self):
        return f"{self.user.email}"
    
    class Meta:
        verbose_name_plural = "Agent"

class Reviews(models.Model):
    review = models.CharField(max_length=300)
    date = models.DateField()
    email = models.ForeignKey("customers", on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent",blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.review},{self.date},{self.email}"
    
    class Meta:
        verbose_name_plural = "Reviews"

class Questions(models.Model):
    question1 = models.CharField(max_length=300,blank=True, null=True)
    question2 = models.CharField(max_length=300,blank=True, null=True)
    question3 = models.CharField(max_length=300,blank=True, null=True)
    question4 = models.CharField(max_length=300,blank=True, null=True)
    question5 = models.CharField(max_length=300,blank=True, null=True)
    agent = models.ForeignKey("Agent",blank=True, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.agent}, {self.date}, {self.question1,self.question2,self.question3,self.question4,self.question5}, {self.category}"
    
    class Meta:
        verbose_name_plural = "Questions"


class Answers(models.Model):
    email = models.ForeignKey("customers", on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=300,blank=True, null=True)
    answer2 = models.CharField(max_length=300,blank=True, null=True)
    answer3 = models.CharField(max_length=300,blank=True, null=True)
    answer4 = models.CharField(max_length=300,blank=True, null=True)
    answer5 = models.CharField(max_length=300,blank=True, null=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.Email}, {self.date} ,{self.answer1,self.answer2,self.answer3,self.answer4,self.answer5},"
    
    class Meta:
        verbose_name_plural = "Answers"
        

class organization(models.Model):
    organization = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.organization}"
    
    class Meta:
        verbose_name_plural = "Organization"

class category(models.Model):
    cateogry = models.CharField(max_length=100)
    agent = models.ForeignKey("Agent",blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cateogry}"
    
    class Meta:
        verbose_name_plural = "Category"
        
class usercategory(models.Model):
    cateogry = models.CharField(max_length=100)
    agent = models.ForeignKey("Agent",blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cateogry}"
    
    class Meta:
        verbose_name_plural = "UserCategory"


class feedback(models.Model):
    choices = [
        ("Good", "Good"),
        ("Needs Imporovement", "Needs Imporovement"),
        ("Irrelevant", "Irrelevant")
    ]
    date = models.DateField(null=True, blank=True)
    feedback = models.CharField(max_length=50, choices=choices)
    affirmation = models.ForeignKey("VOW", on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.feedback, self.affirmation}"
    
    class Meta:
        verbose_name_plural = "Feedback"


class API(models.Model):
    Key = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.Key}"
    
    class Meta:
        verbose_name_plural = "API"


class schedule(models.Model):
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    affirmation = models.ForeignKey("VOW", on_delete=models.CASCADE)
    Category = models.ManyToManyField("usercategory")
    user = models.ManyToManyField("customers")
    date = models.DateField(null=True, blank=True)
    no_of_times = models.IntegerField(default=1, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    
    def __str__(self):
        return f"{self.affirmation, self.date}"
    
    class Meta:
        verbose_name_plural = "schedule"

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)