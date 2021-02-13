from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

# Create your models here.
class Article(models.Model):
    pub_date = models.Datefield()
    headline = models.CharField(max_length=200)
    content = models.Textfield()
    author = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
