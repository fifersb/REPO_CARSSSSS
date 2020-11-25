from django.contrib import admin
from .models import SliderIndex,FotosGaleria,MisionVision,FormInsumo

# Register your models here.
class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields = ['ident']
    list_per_page = 3

class FotosGaleriaAdmin(admin.ModelAdmin):
    list_display = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 3 

admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(FotosGaleria, FotosGaleriaAdmin)
admin.site.register(MisionVision)
admin.site.register(FormInsumo)

