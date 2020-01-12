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
	NorS = models.CharField(max_length=1,verbose_name='N or S')
	longitude = models.CharField(max_length=128,verbose_name='Longitude')
	EorW = models.CharField(max_length=1,verbose_name='E or W')
	speed = models.CharField(max_length=128,verbose_name='Speed over ground, knots')
	track = models.CharField(max_length=128,verbose_name='Track made good, degrees true')
	date = models.CharField(max_length=128,verbose_name='Date')
	magnetic = models.CharField(max_length=128,verbose_name='Magnetic Variation, degrees')
	EorWm = models.CharField(max_length=1,verbose_name='E or W')
	checksum = models.CharField(max_length=128,verbose_name='Checksum')
	content = models.CharField(max_length=128, verbose_name='Trame content') 

# Example: $INDPT,2.3,0.0*46
class DataDPT(models.Model):

	class Meta:
		verbose_name = 'DPT - Depth of Water data'
		verbose_name_plural = 'DPT - Depth of Water data'
		
	list_display = ('__unicode__', 'DPT - Depth of Water data',)
	
	depth = models.CharField(max_length=128,verbose_name='Depth') 
	offset = models.CharField(max_length=128,verbose_name='Offset') 
	checksum = models.CharField(max_length=128,verbose_name='Checksum')
	content = models.CharField(max_length=128, verbose_name='Trame content')
	
class DataTopo(models.Model):

	class Meta:
		verbose_name = 'Topographic Trame'
		verbose_name_plural = 'Topographic Trames'
		
	list_display = ('__unicode__', 'Topographic Trame',)
	
	latitude = models.CharField(max_length=128,verbose_name='Latitude')
	NorS = models.CharField(max_length=1,verbose_name='N or S')
	longitude = models.CharField(max_length=128,verbose_name='Longitude')
	EorW = models.CharField(max_length=1,verbose_name='E or W')
	depth = models.CharField(max_length=128,verbose_name='Depth') 
	antenna_altitude = models.CharField(max_length=128,verbose_name='Altitude Atenna',default=None, blank=True, null=True)
	antenna_altitude_metric = models.CharField(max_length=1,verbose_name='Altitude Atenna Metric',default=None, blank=True, null=True)
	content = models.CharField(max_length=128, verbose_name='Trame content')
	
	
	
	
	
	
	
	
	
	
	