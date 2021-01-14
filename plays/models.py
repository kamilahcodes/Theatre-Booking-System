from django.db import models


# Create your models here.
class Play(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(default = 'abc', unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField()
    genre = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "plays/{slug}/".format(slug=self.slug)



class Viewing(models.Model):
    play_name = models.ForeignKey(Play, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return "plays/seat/{pk}".format(pk=self.pk)

class Seat(models.Model):
    bands = [('A', 'A'), ('B', 'B'), ('C', 'C')]

    number = models.CharField(max_length =100, default = '0')
    viewing = models.ForeignKey(Viewing, null=True, on_delete=models.CASCADE)
    seat_band = models.CharField(choices=bands, default=None, null=True, max_length =100,)
    price = models.DecimalField( decimal_places=2, max_digits=20)
    vacant = models.BooleanField(default=True)

    def __str__(self):
        return str(self.number)
