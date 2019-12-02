from django.contrib import admin
from api.models import Trame
from django.utils.html import format_html



class TrameAdmin(admin.ModelAdmin):
	list_display = ('id', 'content')
	search_fields = ('content',)
	list_filter = ('content',)

	def extendTrame(self, request, queryset):
		for trame in queryset:
			trame.content = trame.content + '-' + 'toto'
			trame.save()
			
		   
	extendTrame.short_description = 'Etendre une trame'

	
	actions = [ extendTrame, ]
	
	
	
admin.site.register(Trame,TrameAdmin)
