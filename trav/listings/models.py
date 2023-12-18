from django.db import models

# Create your models here.

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField(default=None)
    price = models.IntegerField(default=0)
    bed = models.IntegerField(default=1)
    bath = models.IntegerField(default=1)
    sqft = models.IntegerField()

    def __str__(self):
        return self.street

    class Meta:
        db_table = 'listings'
    

"""

 id |   street    |    city     |  zip  | price  | bed | bath | sqft 
----+-------------+-------------+-------+--------+-----+------+------
  1 | Walnut St.  | Glenview    | 92012 | 425000 |   3 |    3 | 3250
  2 | Pecan Dr.   | Allenville  | 92123 | 300000 |   3 |    2 | 2590
  3 | Spruce Ave. | Springfield | 91918 | 500000 |   4 |    2 | 3700

"""
