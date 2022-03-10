from django.db import models

class Project(models.Model):
	title =  models.CharField(max_length=100)
	discription =  models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/', height_field='url_height', width_field='url_width')  #'portfolio/images/'
	url = models.URLField(blank=True)
	url_height = '100'
	url_width = '100'


	def __str__(self):
		return self.title