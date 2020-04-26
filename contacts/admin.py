from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)

# from campspot.models import campspot

# class ListingAdmin(admin.ModelAdmin):
#   list_display = ('id', 'title', 'email',)
#   list_display_links = ('id', 'title')
#   list_filter = ('contact',)
#   list_editable = ('is_published',)
#   search_fields = ('title', 'description', 'address', 'price')
#   list_per_page = 25

# admin.site.register(contact, contactAdmin)