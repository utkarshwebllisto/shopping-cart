from django.db import models

# Create your models here.
class Friend(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Belonging(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Borrowed(models.Model):
	what = models.ForeignKey(Friend, on_delete=models.CASCADE, blank=True, null=True)
	to_who = models.ForeignKey(Belonging, on_delete=models.CASCADE, blank=True, null=True)
	when = models.DateTimeField(auto_now_add=True)
	returned = models.DateTimeField(blank=True, null=True)



