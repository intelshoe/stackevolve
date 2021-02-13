from django.db import models

# name of person who submitted article
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

# Research articles
class Article(models.Model):
    pub_date = models.Datefield()
    headline = models.CharField(max_length=200)
    # not safe
    url_title = models.Textfield(max_legnth=25)
    content = models.Textfield()
    tags = models.Textfield()
    author = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
