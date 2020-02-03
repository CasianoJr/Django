from django.db import models
from django.shortcuts import reverse


class Todo(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse("todo_delete", kwargs={"pk": self.pk})

    def get_completed_url(self):
        return reverse("todo_mark_completed", kwargs={"pk": self.pk})

    def make_incomplete_url(self):
        return reverse("todo_mark_incomplete", kwargs={"pk": self.pk})
