from django.db import models
from django.db import connection
import json
import osgeo
from django.contrib.gis.db import models
from django.contrib.gis.gdal import DataSource

class Gggg(models.Model):
    id_0 = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    farm_name = models.CharField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    fld_id = models.IntegerField(blank=True, null=True)
    flp_id = models.IntegerField(blank=True, null=True)
    f_id = models.IntegerField(blank=True, null=True)
    tlu = models.CharField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    geojson = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.geojson

    class Meta:
        db_table = 'gggg'


from django.db import models

# Create your models here.
