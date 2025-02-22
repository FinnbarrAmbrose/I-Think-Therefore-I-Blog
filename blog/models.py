from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))

def get_default_user():
    return User.objects.get(username='defaultuser')

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    field_2 = models.CharField(max_length=100, default="Hello, world!")
    field_3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments" )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", default=get_default_user)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    challenge = models.SlugField(default='a_slug')
    challenge = models.FloatField(default=3.0)
   

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.event_name