from django.db import models
from django.utils import timezone
from django.urls import reverse
from slugify import slugify
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    # column =
    # tag =
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)  # 建立索引

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)  # 用中文slug覆盖原版
        super(Article, self).save(*args, **kargs)

    def get_absolute_url(self):  # 获取文章url
        return reverse('article:article_detail', args=[self.id, self.slug])

# Create your models here.
