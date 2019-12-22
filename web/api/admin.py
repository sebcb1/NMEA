from django.contrib import admin
from api.models import Trame, DataDPT, DataRMC
from django.utils.html import format_html
import re
import csv
from django.http import HttpResponse
from django.urls import path
from django.http import HttpResponseRedirect


class TrameAdmin(admin.ModelAdmin):
	change_list_template = "admin/change_list_trames.html"
	list_display = ('id', 'content')
	search_fields = ('content',)
	list_filter = ('content',)
	
	# Example: $INDPT,2.3,0.0*46
	DPTre = re.compile('^\$INDPT,(\d+\.\d+),(\d+\.\d+)\*(.+)$')
	
	# Exemple:	$INRMC,163118,A,5040.9561,N,00103.1228,W,4.9,0.0,140608,1.1,W*6D
	RMCre = re.compile('^\$INRMC,([0-9]+),([VA]),(\d+\.\d+),([NS]),(\d+\.\d+),([EW]),(\d+\.\d+),(\d+\.\d+),([0-9]+),(\d+\.\d+),([EW])\*(.+)')

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('deleteAllTrames/', self.deleteAllTrames),
			path('sendAllDPT/', self.sendAllDPT),
			path('sendAllRMC/', self.sendAllRMC),
			path('exportAllTrames/', self.exportAllTrames),
		]
		return my_urls + urls
		
	def deleteAllTrames(self, request):
		for trame in Trame.objects.all():
			trame.delete()
		self.message_user(request, "All trames were deleted")
		return HttpResponseRedirect("../")		  
		
	def sendAllDPT(self, request):
		i=0
		for trame in Trame.objects.all():
			if self.DPTre.match(trame.content):
				data = self.DPTre.search(trame.content)
				t = DataDPT ( depth=data.group(1), offset=data.group(2), checksum=data.group(3), content=trame.content )
				t.save()
				i = i + 1
		if i > 0:
			self.message_user(request, str(i)+' DPT Trames were sent')
		else:
			self.message_user(request, 'No DPT Trame found')	
		return HttpResponseRedirect("../")
	
	def sendAllRMC(self, request):
		i=0
		dre = re.compile('^([0-9]?[0-9])([0-9][0-9])([0-9][0-9])$')
		for trame in Trame.objects.all():
			if self.RMCre.match(trame.content):
				data = self.RMCre.search(trame.content)
				date = dre.search(data.group(1))
				t = DataRMC (	utc=date.group(1)+':'+date.group(2)+':'+date.group(3), 
								status=data.group(2), 
								latitude=data.group(3), 
								NorS=data.group(4), 
								longitude=data.group(5), 
								EorW=data.group(6), 
								speed=data.group(7), 
								track=data.group(8), 
								date=data.group(9), 
								magnetic=data.group(10), 
								EorWm=data.group(11), 
								checksum=data.group(12), 
								content=trame.content )
				t.save()
				i = i + 1
		if i > 0:
			self.message_user(request, str(i)+' RMC Trames were sent')	
		else:
			self.message_user(request, 'No RMC Trame found')	
		return HttpResponseRedirect("../")


	def exportAllTrames(self, request):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for trame in Trame.objects.all():
			row = writer.writerow([getattr(trame, field) for field in field_names])
		return response


	def sendDPT(self, request, queryset):
		i=0
		for trame in queryset:
			if self.DPTre.match(trame.content):
				data = self.DPTre.search(trame.content)
				t = DataDPT ( depth=data.group(1), offset=data.group(2), checksum=data.group(3), content=trame.content )
				t.save()
				i = i + 1
		if i > 0:
			self.message_user(request, 'DPT Trames sent')
		else:
			self.message_user(request, 'No DPT Trame found')
	sendDPT.short_description = 'Send DPT trames selected'

	def sendRMC(self, request, queryset):
		i=0
		dre = re.compile('^([0-9]?[0-9])([0-9][0-9])([0-9][0-9])$')
		for trame in queryset:
			if self.RMCre.match(trame.content):
				data = self.RMCre.search(trame.content)
				date = dre.search(data.group(1))
				t = DataRMC (	utc=date.group(1)+':'+date.group(2)+':'+date.group(3), 
								status=data.group(2), 
								latitude=data.group(3), 
								NorS=data.group(4), 
								longitude=data.group(5), 
								EorW=data.group(6), 
								speed=data.group(7), 
								track=data.group(8), 
								date=data.group(9), 
								magnetic=data.group(10), 
								EorWm=data.group(11), 
								checksum=data.group(12), 
								content=trame.content )
				t.save()
				i = i + 1
		if i > 0:
			self.message_user(request, str(i)+' RMC Trames were sent')	
		else:
			self.message_user(request, 'No RMC Trame found')	
	sendRMC.short_description = 'Send RMC trames selected'
	
	def exportTrames(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for trame in queryset:
			row = writer.writerow([getattr(trame, field) for field in field_names])
		return response
	exportTrames.short_description = 'Export trames selected to csv file'
		
	actions = [ sendDPT,sendRMC,exportTrames ]
	
class DataDPTAdmin(admin.ModelAdmin):
	change_list_template = "admin/change_list_DPT.html"
	list_display = ('id', 'depth','offset','checksum','content')
	search_fields = ('content',)
	list_filter = ('content',)

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('deleteAllDPT/', self.deleteAllDPT),
			path('exportAllDPT/', self.exportAllDPT),
		]
		return my_urls + urls
		
	def deleteAllDPT(self, request):
		for data in DataDPT.objects.all():
			data.delete()
		self.message_user(request, "All DPT data were deleted")
		return HttpResponseRedirect("../")		  
		
	def exportAllDPT(self, request):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for data in DataDPT.objects.all():
			row = writer.writerow([getattr(data, field) for field in field_names])
		return response	

	def exportData(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for data in queryset:
			row = writer.writerow([getattr(data, field) for field in field_names])
		return response
	exportData.short_description = 'Export DPT data selected to csv file'
		
	actions = [ exportData ]

class DataRMCAdmin(admin.ModelAdmin):
	change_list_template = "admin/change_list_RMC.html"
	list_display = ('id', 'utc','status','latitude','NorS','longitude','EorW','speed','track','date','magnetic','EorWm','checksum','content')
	search_fields = ('content',)
	list_filter = ('content',)

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('deleteAllRMC/', self.deleteAllRMC),
			path('exportAllRMC/', self.exportAllRMC),
		]
		return my_urls + urls
		
	def deleteAllRMC(self, request):
		for data in DataRMC.objects.all():
			data.delete()
		self.message_user(request, "All RMC data were deleted")
		return HttpResponseRedirect("../")		  
		
	def exportAllRMC(self, request):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for data in DataRMC.objects.all():
			row = writer.writerow([getattr(data, field) for field in field_names])
		return response	

	def exportData(self, request, queryset):
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)
		writer.writerow(field_names)
		for data in queryset:
			row = writer.writerow([getattr(data, field) for field in field_names])
		return response
	exportData.short_description = 'Export RMC data selected to csv file'
		
	actions = [ exportData ]
		
admin.site.register(Trame,TrameAdmin)
admin.site.register(DataDPT,DataDPTAdmin)
admin.site.register(DataRMC,DataRMCAdmin)
