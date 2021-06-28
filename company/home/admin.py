from django.contrib import admin
from .models import Product
from .models import Employee
from .models import Employment
from .models import Slider
from .models import Massage

# Register your models here.
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Employment)
admin.site.register(Slider)
admin.site.register(Massage)
