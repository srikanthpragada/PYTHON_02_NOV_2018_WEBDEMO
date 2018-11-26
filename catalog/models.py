from django.db import models


# Create your models here.

class Course:
    def __init__(self, name, faculty, topics):
        self.name = name
        self.faculty = faculty
        self.topics = topics
