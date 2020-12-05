from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.http import HttpResponse

# Temp trial line of code

# Account is related to auth user model when ever user created account id also created
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20,null=True)
    is_verified = models.BooleanField(null=True)
    email = models.EmailField(max_length=50,unique=True,null=True)
    if(User.objects.exists):
        def __str__(self):
            return self.user
    
@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()


# This model contain item posted by system information
class ItemPost(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     item_name = models.CharField(max_length=200)
     item_price = models.IntegerField()
     availabilty = models.BooleanField(null=True)
     item_type = models.CharField(
         max_length=200,
         blank=True,
         null=True,
         choices=[
             ('car','Car'),
             ('house','House'),

         ],
     )
     def __str__(self):
         return self.title


#This picture class is related ItemPost model as far as their is a post their will be picture
class Picture(models.Model):
    item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
    path_addr = models.CharField(max_length=200)
    def __str__(self):
        return self.path_addr

# Car model is used for if a post is type of car this model get used
class Cars(models.Model):
     item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE,blank=True,null=True)
     car_model = models.CharField(max_length=200)
     mileage = models.CharField(max_length=200) 
     car_description = models.CharField(max_length=1000,null=True,blank=True)
     transmission = models.CharField(
         max_length=200,
         null=True,blank=True,
         choices=[
             ('manual','Manual'),
             ('automatic','Automatic'),
         ]
     )
     manu_year = models.DateField(null=True,blank=True)
     engine_type = models.CharField(
         max_length=200,
         null=True,blank=True,
         choices=[
             ('diesel',"Diesel"),
             ('benzine', 'Benzine')
    
         ]
     )
     car_condition = models.CharField(
         max_length=200,
        #  null=True,blank=True,
         choices=[
             ('new','New'),
             ('sl_used','Slightly Used'),
             ('used','Used')
         ]
     )
     drive_type = models.CharField(
         max_length=200,
         null=True,blank=True,
         choices=[
            ('two_wheel','2 Wheel Drive'),
            ('four_wheel','4 Wheel Drive'),
         ],
     )
     car_color = models.CharField(
         max_length=200,
        #  null=True,
        #  blank=True,
         choices=[
            ('old','It\'s own color'),
            ('New','Color renewed'),
         ],
    )
    # def __str__(self):
    #     return self.item_post_id



# House model is used for if a post is type of house this model get used
class House(models.Model):
     item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
     area = models.FloatField(max_length=200,null=True,blank=True)
     bank_loan = models.CharField(
         max_length=200,null=True,blank=True,
         choices=[
             ('free','Free'),
             ('depted','Depted')
         ]
    )
     bed_unit = models.IntegerField(null=True,blank=True)
     house_description = models.CharField(max_length=1000,null=True,blank=True)

     def __str__(self):
         return self.item_post_id

# Watchlist model
class WatchList(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
     


# Alert model
class Alert(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     item_type = models.CharField(
         max_length=200,
         choices=[
             ('car','Car'),
             ('house','House'),

         ]
     )


# Rating model
class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rated_user_id = models.IntegerField(blank=True,null=True)
    score = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(1),
                                ]
                                )

    def __str__(self):
        return str(self.pk)