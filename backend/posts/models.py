from django.db import models
import random

# Create your models here.


class Section(models.Model):

    title = models.CharField(max_length=100, default="PHYS 161", unique=True)

    def __str__(self):
        return f"Section: {self.title}"


class Topic(models.Model):
    title = models.CharField(max_length=100)
    SET_NUMBERS = [(1, 1), (2, 2), (3, 3), (4, 4)]
    set_number = models.IntegerField(choices=SET_NUMBERS)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, default=random.randint(0, 10000)
    )

    def __str__(self):
        return f"Topic: {self.title}, Set: {self.set_number}"


class Post(models.Model):

    body = models.TextField()
    answer = models.FloatField(default=0)
    number = models.IntegerField(default=0)
    solve_url = models.TextField(default="")
    body_url = models.URLField(null=True, blank=True)
    # problem_set = models.ForeignKey(ProblemSet, on_delete=models.SET_NULL)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, default=random.randint(0, 10000)
    )

    def __str__(self):
        return f"Problem title: {self.topic.title}, Number: P{self.number}"
