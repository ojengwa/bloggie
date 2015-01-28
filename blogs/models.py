from django.db import models

# Create your models here.
class Author(models.Model):
  author_name = models.charField(max_length=50)
  date_joined = models.DateTimeField('date joined')
  #"""docstring for Author"""
  # def __init__(self, arg):
  #   super(Author, self).__init__()
  #   self.arg = arg
  #   

class Post(models.Model):
  author = models.ForeignKey(Author)
  text = models.charField(max_length=900)
  likes = models.IntegerField(default=0)
  #"""docstring for Post"""
  # def __init__(self, arg):
  #   super(Post, self).__init__()
  #   self.arg = arg

class Comment(models.Model):
  post = models.ForeignKey(Post)
  comment = models.charField(max_length=900)

  # """docstring for Comment"""
  # def __init__(self, arg):
  #   super(Comment, self).__init__()
  #   self.arg = arg
    
  #   