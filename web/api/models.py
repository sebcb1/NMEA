from django.db import models

class Trame(models.Model):

	class Meta:
		verbose_name = 'Trame'
		verbose_name_plural = 'Trames'
		
	list_display = ('__unicode__', 'Trames',)

	content = models.CharField(max_length=128, verbose_name='Trame content')
	
	def __str__(self):
		return str(self.id)


# Exemple:	$INRMC,163118,A,5040.9561,N,00103.1228,W,4.9,0.0,140608,1.1,W*6D
class DataRMC(models.Model):

	class Meta:
		verbose_name = 'RMC - Recommended Minimum Navigation Information data'
		verbose_name_plural = 'RMC - Recommended Minimum Navigation Information data'
		
	list_display = ('__unicode__', 'RMC - Recommended Minimum Navigation Information data',)
	
	utc = models.TimeField(verbose_name='UTC') 
	status = models.CharField(max_length=1,verbose_name='Status') 
	latitude = models.CharField(max_length=128,verbose_name='Latitude')
	NorS = models.CharField(max_length=1,verbose_name='N or S', null=True)
	longitude = models.CharField(max_length=128,verbose_name='Longitude', null=True)
	EorW = models.CharField(max_length=1,verbose_name='E or W', null=True)
	speed = models.CharField(max_length=128,verbose_name='Speed over ground, knots', null=True)
	track = models.CharField(max_length=128,verbose_name='Track made good, degrees true', null=True)
	date = models.CharField(max_length=128,verbose_name='Date', null=True)
	magnetic = models.CharField(max_length=128,verbose_name='Magnetic Variation, degrees', null=True)
	EorWm = models.CharField(max_length=1,verbose_name='E or W', null=True)
	checksum = models.CharField(max_length=128,verbose_name='Checksum', null=True)
	content = models.CharField(max_length=128, verbose_name='Trame content', null=True) 

# Example: $INDPT,2.3,0.0*46
class DataDPT(models.Model):

	class Meta:
		verbose_name = 'DPT - Depth of Water data'
		verbose_name_plural = 'DPT - Depth of Water data'
		
	list_display = ('__unicode__', 'DPT - Depth of Water data',)
	
	depth = models.CharField(max_length=128,verbose_name='Depth') 
	offset = models.CharField(max_length=128,verbose_name='Offset') 
	checksum = models.IntegerField(verbose_name='Checksum')
	content = models.CharField(max_length=128, verbose_name='Trame content')