from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class NewsMarket(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

