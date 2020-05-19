from django.contrib import admin
from.models import Header
from .models import headerbox
from .models import Before_Footer_Upcoming_Events,contact,contacttest,contactlast

# Register your models here.
admin.site.register(Header)
admin.site.register(headerbox)
admin.site.register(Before_Footer_Upcoming_Events)
admin.site.register(contact)
admin.site.register(contacttest)
admin.site.register(contactlast)