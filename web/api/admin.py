from django.contrib import admin
from api.models import Trame

class TrameAdmin(admin.ModelAdmin):
	list_display = ('id', 'content')
	search_fields = ('content',)
	list_filter = ('content',)
	
admin.site.register(Trame,TrameAdmin)
