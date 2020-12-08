from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.http import HttpResponse
from django.core.exceptions import ValidationError

# Temp trial line of code
class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

# Account is related to auth user model when ever user created account id also created
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20,null=True)
    user_type = models.CharField(
        max_length=20,
        null=True,
        default= 'customer',
        choices=[
             ('broker','Broker'),
             ('company','Company'),

        ],
    )
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
     item_name = models.CharField(max_length=200)
     item_price = models.IntegerField()
     availabilty = models.BooleanField(null=True)
     serviceType = models.CharField(
         max_length=200,
         blank=True,
         null=True,
         choices=[
             ('rent','Rent'),
             ('sell','Sell'),

         ],
     )
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
         return self.item_name


# This picture class is related ItemPost model as far as their is a post their will be picture
# updated by biniam

def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id)


def validate_image(image):
    file_size = image.file.size
    limit_kb = 5
    if file_size > limit_kb * 5000:
        raise ValidationError("Max size of file is %s KB" % limit_kb)


class Picture(models.Model):
    item_post_id = models.ForeignKey(ItemPost, on_delete=models.CASCADE)
    path_addr = models.ImageField( upload_to="images/")


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
    def __str__(self):
        return self.car_model



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
    # 0.56468787870
    bed_unit = models.IntegerField(null=True,blank=True)
    house_description = models.CharField(max_length=1000,null=True,blank=True)
    lat = models.FloatField(max_length=30,null=True,blank=True)
    longt = models.FloatField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.bank_loan

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