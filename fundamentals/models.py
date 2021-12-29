from django.db import models


# Zone Model
class Zone(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    sub_district = models.CharField(max_length=50, null=False, blank=False)
    division = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'zones'
