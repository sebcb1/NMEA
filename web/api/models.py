from django.db import models


# https://medium.com/@hakibenita/how-to-add-custom-action-buttons-to-django-admin-8d266f5b0d41

class Trame(models.Model):

	class Meta:
		verbose_name = 'Trame'
		verbose_name_plural = 'Trames'
		
	list_display = ('__unicode__', 'Trames',)

	content = models.CharField(max_length=128, verbose_name='Contenu de la trame')
	
	def __str__(self):
		return str(self.id)
