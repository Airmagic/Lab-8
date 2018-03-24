from django.db import models
from django.utils import timezone

# creating a class for the blogs
class Post(models.Model):
    # making object blogs for the site
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

            # This is a publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # This gets a text string with the post title
    def __str__(self):
        return self.title
