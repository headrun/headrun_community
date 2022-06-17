from django.contrib.auth.models import User
from django.db import models

from base.models import BaseActiveOrderedModel

# Create your models here.

POST_CHOICES = (
    ("STORY", "STORY"),
    ("POST", "POST"),
)
FILE_CHOICES = (
    ("Photo", "Photo"),
    ("Video", "Video"),
    ("Text", "Text"),
)
REACTION_CHOICES = (
    ("LIKE", "LIKE"),
    ("DISLIKE", "DISLIKE")
)


# Posts,Story models
class Posts(BaseActiveOrderedModel):
    post_type = models.CharField(max_length=30, choices=POST_CHOICES)
    posted_username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="createdby")
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, null=True)
    tags = models.CharField(max_length=50, null=True)
    links = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.description


# post's file type
class FileType(BaseActiveOrderedModel):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name="postid")
    file_type = models.CharField(max_length=20, choices=FILE_CHOICES, default="Photo")
    post_file = models.FileField(upload_to='static/', null=True, verbose_name="post_images")

    def __str__(self):
        return self.post
    class Meta(BaseActiveOrderedModel.Meta):
        pass


# comments for the post&story
class Comments(BaseActiveOrderedModel):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comment_by")
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name="post_id")
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment
    
    class Meta(BaseActiveOrderedModel.Meta):
        pass


# reactions on post,story
class Reactions(BaseActiveOrderedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="liked_by")
    reacted_to = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name="likedpost")
    reaction = models.CharField(max_length=500, choices=REACTION_CHOICES, default="LIKE")

    def __str__(self):
        return self.reaction
    
    class Meta(BaseActiveOrderedModel.Meta):
        pass
