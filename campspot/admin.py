from django.contrib import admin
from campspot.models import campme



class campspotAdmin(admin.ModelAdmin):

  spot_display = ('id', 'title', 'price',)
  spot_display_links = ('id', 'title')
  spot_editable = ('price',)
  search_fields = ('title', 'price')
  spot_per_page = 25

admin.site.register(campme)

