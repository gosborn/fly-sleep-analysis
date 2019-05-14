from django.db import models

# Create your models here.
class Experiment(models.Model):
    date_performed = models.DateField()
    run_number = models.IntegerField()
    person = models.CharField(max_length=256)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Board(models.Model):
    LARGE = 'Large'
    SMALL = 'Small'

    BOARD_TYPES = (
        (LARGE, 'Large'),
        (SMALL, 'Small'),
    )

    number = models.IntegerField()
    type = models.CharField(max_length=5, choices=BOARD_TYPES, default=SMALL)
    monitor_file = models.FileField(upload_to='monitor_file')
    experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Genotype(models.Model):
    name = models.CharField(max_length=256)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class BoardPosition(models.Model):
    FEMALE = 'Female'
    MALE = 'Male'

    GENDER_TYPES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    position = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_TYPES, default=FEMALE)
    collection_start = models.DateField()
    collection_end = models.DateField()

    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    genotype = models.ForeignKey('Genotype', null=True, blank=True, on_delete=models.SET_NULL)
