from django.db import models

class Trame(models.Model):

	class Meta:
		verbose_name = 'Trame'
		verbose_name_plural = 'Trames'
		
	list_display = ('__unicode__', 'Trames',)

	content = models.CharField(max_length=128, verbose_name='Contenu de la trame')
	commentaire = models.CharField(max_length=128, verbose_name='Commentaire')
	
	def __str__(self):
		return str(self.id)

