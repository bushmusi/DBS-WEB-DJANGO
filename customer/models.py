from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=200)
    is_verified = models.BooleanField()
@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()

class ItemPost(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     item_name = models.CharField(max_length=200)
     item_price = models.IntegerField()
     item_type = models.CharField(
         max_length=200,
         choices=[
             ('car','Car'),
             ('house','House'),

         ],
     )

class Picture(models.Model):
    item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
    path_addr = models.CharField(max_length=200)

class Cars(models.Model):
     item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
     car_model = models.CharField(max_length=200)
     transmission = models.CharField(
         max_length=200,
         choices=[
             ('manual','Manual'),
             ('automatic','Automatic'),
         ]
     )
     manu_year = models.DateField()
     engine_type = models.CharField(
         max_length=200,
         choices=[
             ('diesel',"Diesel"),
             ('benzine', 'Benzine')
    
         ]
     )
     car_condition = models.CharField(
         max_length=200,
         choices=[
             ('new','New'),
             ('sl_used','Slightly Used'),
             ('used','Used')
         ]
     )
     drive_type = models.CharField(
         max_length=200,
        choices=[
            ('two_wheel','2 Wheel Drive'),
            ('four_wheel','4 Wheel Drive'),
        ],
     )
     car_color = models.CharField(max_length=200)
     mileage = models.CharField(max_length=200)
     description = models.CharField(max_length=1000)

class House(models.Model):
     item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
     area = models.FloatField(max_length=200)
     bank_loan = models.CharField(max_length=200)
     bed_unit = models.IntegerField()
class WatchList(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)


class Alert(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     item_type = models.CharField(
         max_length=200,
         choices=[
             ('car','Car'),
             ('house','House'),

         ]
     )