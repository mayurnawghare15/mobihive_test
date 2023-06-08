from django.db import models
import firebase_admin
from firebase_admin import firestore
import uuid


class Classroom(models.Model):
    """
    Model representing a classroom.
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the classroom.
        """
        return self.name


class Students(models.Model):
    """
    Model representing a student.
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the student.
        """
        return self.name
