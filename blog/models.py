# blog/models.py

from django.db import models
from django.core.validators import MinLengthValidator
from datetime import date

# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# Tag Model
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=300, default="No excerpt provided")
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(default=date.today)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title

# ✅ FIXED: Comment Model defined properly outside Post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField(max_length=120,null=True)
    user_email = models.EmailField(null=True)
    text = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post.title}"
