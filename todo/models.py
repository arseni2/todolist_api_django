from django.db import models

class TodoListModel(models.Model):
    text = models.TextField()
    is_importants = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    editMode = models.BooleanField(default=False)