from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=20)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    characteristics = models.ManyToManyField(to="characteristics.Characteristic")

    group = models.ForeignKey(
        to="groups.Group", on_delete=models.CASCADE, related_name="animals"
    )