from django.db import models

# Create your models here.
class Book(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    value = models.FloatField()


    def __str__(self):
        return(f'Titulo: {self.title} - R$ {self.value}')
