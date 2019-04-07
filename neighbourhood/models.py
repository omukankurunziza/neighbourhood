from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Admin(models.Model):
    name=models.CharField(max_length = 60,null = True)
    user = models.ForeignKey(User,null=True)

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 60,null = True)
    # image = models.ImageField(upload_to = "images/",null = True)
    admin = models.ForeignKey(Admin,null=True)
    # profile =models.ForeignKey(Profile,null=True)
    Occupants_Count= models.CharField(max_length = 70,null = True)
    # likes = models.IntegerField(default=0)
    location = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    # Admin = models.ForeignKey(Admin,null=True)
    # profile = models.ForeignKey(Profile, null=True) 
    # comments = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    def delete_name(self):
        self.delete()

    def save_name(self):
        self.save()

    def update_location(self,new_location):
        self.name_location = new_location
        self.save()


    @classmethod
    def get_name(cls, id):
        name = cls.objects.get(id=id)
        return name

    @classmethod
    def post_names(cls):
        names = cls.objects.all()
        return names 

    


    class Meta:
        ordering = ['-pub_date']
    
    # @classmethod
    # def search_by_title(cls,search_term):
    #     project = cls.objects.filter(title__icontains = search_term)
    #     return project


	# @classmethod
	# def search_by_n(cls,search_term):
	# 	photos = cls.objects.filter(name__icontains = search_term)
	# 	return photos
class Profile(models.Model):
    username = models.CharField(default='User',max_length=60)
    profile_image = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(default='',blank = True)
    location = models.TextField(default='',blank = True)
    neighbourhood_name = models.TextField(default='',blank = True)
    # contact = models.TextField(default=0,null = True)
    # project = models.IntegerField(default=0)
    user = models.ForeignKey(User,null=True)



    def __str__(self):
        return self.username

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()
    
class User(models.Model):
    # user = models.ForeignKey(User, null= True)
    # project = models.ForeignKey(Project, null= True)
    neighbourhood = models.ForeignKey(Neighbourhood, null= True)
    # project = models.ForeignKey(Project, null= True,related_name='rating')
    name= models.TextField(default='',blank = True)
    email=  models.CharField(default='User',max_length=60)
    # content= models.IntegerField(default=0)
    def __str__(self):
        return self.name


    def delete_name(self):
        self.delete()

    def save_name(self):
        self.save()

class Business(models.Model):
    # user = models.ForeignKey(User, null= True)
    # project = models.ForeignKey(Project, null= True)
    neighbourhood = models.ForeignKey(Neighbourhood, null= True)
    # project = models.ForeignKey(Project, null= True,related_name='rating')
    name= models.TextField(default='',blank = True)
    email=  models.CharField(default='User',max_length=60)
    user = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.name


    def delete_name(self):
        self.delete()

    def save_name(self):
        self.save()