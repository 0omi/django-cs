from django.contrib import admin
from .models import Photo

# Register your models here.

admin.site.site_header = "KITTEN CROCHET" # Adjustments to the control panel
admin.site.site_title = "KITTEN CROCHET"  

admin.site.register(Photo)
