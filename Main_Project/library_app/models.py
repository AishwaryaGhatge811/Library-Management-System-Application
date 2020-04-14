from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.TextField()
    book_type = models.TextField()
    book_price = models.IntegerField(default=1)
