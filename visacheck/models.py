from django.db import models

# Create your models here.
class Visa(models.Model):
    card_holder = models.CharField(max_length=120)
    cc_no = models.IntegerField()
    expiry_date=models.IntegerField()
    csv=models.IntegerField()


    def __str__(self):
        return self.card_holder
