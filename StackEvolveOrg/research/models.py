from django.db import models

# name of person who submitted article
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

# Research articles
class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(200)
    url_title = models.CharField(25)
    content = models.TextField()
    tag = models.CharField(20)
    author = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
