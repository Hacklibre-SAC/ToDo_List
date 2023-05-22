from django.db import models

class Todo(models.Model):
    TodoName = models.CharField("Nombre de tarea", max_length=500)
    Status = models.BooleanField("Estado", default=False)

    def __str__(self):
        return f"{self.TodoName} > {self.Status}"
    