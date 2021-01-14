from django.db import models
from plays.models import Play
from users.models import CustomUser
# Create your models here.



class Review(models.Model):
    play = models.ForeignKey(Play,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.play);
