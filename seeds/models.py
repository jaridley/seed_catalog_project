from django.db import models


class Seeds(models.Model):
    seed_name = models.CharField(max_length=50)
    seed_variety = models.CharField(max_length=50)
    seed_type = models.CharField(max_length=50)
    seed_planting_zone = models.CharField(max_length=4)
    germination_period = models.CharField(max_length=4)
    days_to_harvest = models.CharField(max_length=4)
    plant_spacing = models.CharField(max_length=4)
    row_spacing = models.CharField(max_length=4)
    plant_depth = models.CharField(max_length=4)
    sun_requirements = models.CharField(max_length=4)
    water_requirements = models.CharField(max_length=4)

    def __str__(self):
        return self.seed_name
