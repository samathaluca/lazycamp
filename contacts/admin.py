from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'campspot', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'campspot')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
# admin.site.register(Contact)







# Register your models here.


# from campspot.models import campspot

# class ListingAdmin(admin.ModelAdmin):
#   list_display = ('id', 'title', 'email',)
#   list_display_links = ('id', 'title')
#   list_filter = ('contact',)
#   list_editable = ('is_published',)
#   search_fields = ('title', 'description', 'address', 'price')
#   list_per_page = 25

# admin.site.register(contact, contactAdmin)