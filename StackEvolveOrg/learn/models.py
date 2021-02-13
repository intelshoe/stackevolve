from django.db import models


# Research articles
class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200)
    url_title = models.CharField(max_length=25)
    content = models.TextField()
    tag = models.CharField(max_length=20)
    author = models.CharField(max_length=35)

    def __str__(self):
        return self.headline
