from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Movie (models.Model):
    title =models.TextField(max_length=100)
    description= models.TextField(max_length=1000)
    duration = models.IntegerField(blank=True,null=True)
    Director = models.ForeignKey(Director,null=True,on_delete=models.PROTECT)



    def __str__(self):
        return self.title
    
class Review(models.Model):
    text = models.TextField(max_length=210)
    Movie=models.ForeignKey(Movie,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.text