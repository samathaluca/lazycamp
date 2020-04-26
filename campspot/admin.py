from django.contrib import admin
from campspot.models import campme

admin.site.register(campme)

# class campspotAdmin(admin.ModelAdmin):

#   list_display = ('id', 'title', 'price',)
#   list_display_links = ('id', 'title')
#   list_editable = ('price',)
#   search_fields = ('title', 'price')
#   list_per_page = 25

