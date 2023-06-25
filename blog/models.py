from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    professor = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    score = models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='attachments/')

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    subjects = models.ManyToManyField(Subject)
    uploaded_posts = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name='uploader')
    downloaded_posts = models.ManyToManyField(Post, related_name='downloaders')

    def __str__(self):
        return self.name

