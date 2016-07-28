from __future__ import unicode_literals
from django.db import models

# -----------------------For Different Colors-----------------------


class Size(models.Model):
    name = models.CharField(max_length=200)
    diplayImage = models.FileField()

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name,
            "image": self.diplayImage.url
        }
        return data


# -----------------------For Different Colors-----------------------


class Color(models.Model):
    name = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name
        }
        return data


# -----------------------For Kinds of Sofa-----------------------

class SofaKind(models.Model):
    name = models.CharField(max_length=255)
    displayImage = models.CharField(max_length=2048, blank=True)
    displayName = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name
        }
        return data


# -----------------------For Arm Types-----------------------

class Arm(models.Model):
    name = models.CharField(max_length=255)
    kindId = models.ForeignKey("SofaKind")
    displayImage = models.CharField(max_length=2048, blank=True)
    displayName = models.CharField(max_length=255, default=None, null=True)
    layer = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name,
            "sofakind": self.kindId.name,
            "layer": self.layer
        }
        return data


# -----------------------For ArmType,Size * Color-----------------------

class ArmVariant(models.Model):
    armId = models.ForeignKey("Arm")
    size = models.CharField(max_length=255)
    color = models.ForeignKey('Color')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField()

    def __str__(self):
        return self.armId.name + "_" + self.size + "_" + self.color.name

    def as_json(self):
        data = {
            "name": self.__str__(),
            "arm": self.armId.name,
            "size": self.size,
            "color": self.color.name,
            "price": str(self.price),
            "image": self.image.url,
        }
        return data


# -----------------------For Leg Types----------------------

class Leg(models.Model):
    name = models.CharField(max_length=255)
    displayImage = models.CharField(max_length=2048, blank=True)
    displayName = models.CharField(max_length=255, default=None, null=True)
    layer = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name,
            "layer": self.layer,
        }
        return data


# -----------------------For LegTypes, Size, Arm, Color----------------------

class LegVariant(models.Model):
    legId = models.ForeignKey("Leg")
    size = models.CharField(max_length=255)
    armId = models.ForeignKey("Arm")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField()

    def __str__(self):
        return self.legId.name + "_" + self.size + "_" + self.armId.name

    def as_json(self):
        data = {
            "name": self.__str__(),
            "leg": self.legId.name,
            "arm": self.armId.name,
            "size": self.size,
            "price": str(self.price),
            "image": self.image.url,
        }
        return data


# -----------------------For Back Types----------------------

class Back(models.Model):
    name = models.CharField(max_length=255)
    displayImage = models.CharField(max_length=2048, blank=True)
    displayName = models.CharField(max_length=255, default=None, null=True)
    layer = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name,
            "layer": self.layer,
        }
        return data


# -----------------------For BackTypes, Size, Arm, Color----------------------

class BackVariant(models.Model):
    backId = models.ForeignKey("Back")
    size = models.CharField(max_length=255)
    armId = models.ForeignKey("Arm")
    color = models.ForeignKey('Color')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField()

    def __str__(self):
        return self.backId.name + "_" + self.size + "_" + self.armId.name + "_" + self.color.name

    def as_json(self):
        data = {
            "name": self.__str__(),
            "back": self.backId.name,
            "arm": self.armId.name,
            "size": self.size,
            "price": str(self.price),
            "image": self.image.url,
            "color": self.color.name
        }
        return data


# -----------------------For Pipe Types----------------------

class Pipe(models.Model):
    name = models.CharField(max_length=255)
    displayImage = models.CharField(max_length=2048, blank=True)
    displayName = models.CharField(max_length=255, default=None, null=True)
    layer = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def as_json(self):
        data = {
            "name": self.name,
            "layer": self.layer,
        }
        return data


# -----------------------For PipeTypes, Size, Arm, Back, Color----------------------

class PipeVariant(models.Model):
    pipeId = models.ForeignKey("Pipe")
    size = models.CharField(max_length=255)
    armId = models.ForeignKey("Arm")
    backId = models.ForeignKey("Back")
    color = models.ForeignKey('Color')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField()

    def __str__(self):
        return self.pipeId.name + "_" + self.size + "_" + self.armId.name + "_" + self.backId.name + "_" + self.color.name

    def as_json(self):
        data = {
            "name": self.__str__(),
            "pipe": self.pipeId.name,
            "size": self.size,
            "arm": self.armId.name,
            "back": self.backId.name,
            "color": self.color.name,
            "price": str(self.price),
            "image": self.image.url
        }
        return data
