from django.db import models




class AbstractNameModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(AbstractNameModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True)


class Tag(AbstractNameModel):
    pass


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
    star_choices =(
    (i,'* ' * i) for i in range(1, 6)
    )
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=star_choices, default=1, null=True)

    def __str__(self):
        return self.text