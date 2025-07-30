from django.contrib import admin
from service.models import homepro,mens,womens,Cart,Checkout,Order

# Register your models here.
    
# class serhome(admin.ModelAdmin):
#     list_display=('name','image','price','descriptions')

class sermen(admin.ModelAdmin):
    list_display=('mname','mimage','mprice','mdescriptions')

class serwomen(admin.ModelAdmin):
    list_display=('wname','wimage','wprice','wdescriptions')

class scart(admin.ModelAdmin):
    list_display=()

class scheckout(admin.ModelAdmin):
    list_display=()

class sorder(admin.ModelAdmin):
    list_display = ('product_name', 'host', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')

# admin.site.register(homepro)
admin.site.register(mens)
admin.site.register(womens)
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(Order)