from django.contrib import admin
from .models import Parent, Child, IceCream, IceCreamKiosk

class ParentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country', 'has_children']
    list_filter = ['country', 'has_children']
    search_fields = ['first_name', 'last_name', 'city']

admin.site.register(Parent, ParentAdmin)
admin.site.register(Child)
admin.site.register(IceCream)
admin.site.register(IceCreamKiosk)
