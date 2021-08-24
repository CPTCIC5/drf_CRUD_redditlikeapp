from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    published_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering= ['-published_on']

class Vote(models.Model):
    voted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_by=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.voted_by)


