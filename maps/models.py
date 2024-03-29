from django.db import models
from django.utils import timezone

class Map(models.Model):
	author			= models.ForeignKey('auth.User')
	title			= models.CharField(max_length=500)
	question		= models.TextField()
	description		= models.TextField()
	created_date	= models.DateTimeField(default=timezone.now)
	published_date	= models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class MapContent(models.Model):
    map             = models.ForeignKey(Map, on_delete = models.CASCADE)
    content         = models.TextField()
    created_date    = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.map)