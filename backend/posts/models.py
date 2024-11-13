from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.FloatField(default=0)
    number = models.IntegerField(default=0)
    solve_url = models.TextField(default="")
    body_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Posts: {self.title}"
