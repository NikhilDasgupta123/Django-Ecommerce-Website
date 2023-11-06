from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils.html import format_html

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_type = models.CharField(max_length=25)
    product_description = models.TextField()
    affiliate_url = models.SlugField(blank=True, null=True)
    product_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product_name
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Vote(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    comfort=models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    durability=models.IntegerField(default=0)