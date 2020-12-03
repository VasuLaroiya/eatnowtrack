from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import date




class Post(models.Model):
    content = models.TextField(max_length=1000)
    servings_meat = models.IntegerField(default=0)
    servings_dairy = models.IntegerField(default=0)
    servings_grains = models.IntegerField(default=0)
    servings_vegetables = models.IntegerField(default=0)
    servings_fruit = models.IntegerField(default=0)
    minutes_aerobic_exercise = models.IntegerField(default=0)
    minutes_weightlifting_exercise = models.IntegerField(default=0)
    image_post = models.ImageField(default='default.png', upload_to='post_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)



    def __str__(self):
        return self.content[:5]

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img_post = Image.open(self.image_post.path)
        if img_post.height > 600 or img_post.width > 600:
            output_size = (600, 600)
            img_post.thumbnail(output_size)
            img_post.save(self.image_post.path)



class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)


class Preference(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")
