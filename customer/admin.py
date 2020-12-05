from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)


admin.site.register(House)
admin.site.register(WatchList)
admin.site.register(Alert)


class ItemPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_name','item_price','availabilty','item_type',)
admin.site.register(ItemPost,ItemPostAdmin)

class PictureAdmin(admin.ModelAdmin):
    list_display= ('item_post_id','path_addr')
admin.site.register(Picture)

class CarsAdmin(admin.ModelAdmin):
    list_display= ('car_model','mileage','car_description')
admin.site.register(Cars)
