from django.contrib import admin
from api.models import Trame
from django.utils.html import format_html



class TrameAdmin(admin.ModelAdmin):
	list_display = ('id', 'content', 'commentaire','commentTrame')
	search_fields = ('content',)
	list_filter = ('content',)

	def extendTrame(self, request, queryset):
		for trame in queryset:
			trame.content = trame.content + '-' + 'toto'
			trame.save()
			
		   
	extendTrame.short_description = 'Etendre une trame'

	
	actions = [ extendTrame, ]
	
	def commentTrame(self, obj):
		return format_html( '<a class="button" href="/trames/comment">Commenter</a>','')
		
	commentTrame.short_description = 'Actions'	 
	commentTrame.allows_tags = True
	
admin.site.register(Trame,TrameAdmin)
