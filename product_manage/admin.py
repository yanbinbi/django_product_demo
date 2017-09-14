from django.contrib import admin
from product_manage.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Address)
