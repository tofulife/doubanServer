# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class bookModel(models.Model):
    bid = models.CharField(db_column='bId', primary_key=True, max_length=20)  # Field name made lowercase.
    btitle = models.CharField(db_column='bTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bscore = models.CharField(db_column='bScore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bdate = models.CharField(db_column='bDate', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'



