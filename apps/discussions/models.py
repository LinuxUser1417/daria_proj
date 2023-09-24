from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200)


class Discussion(models.Model):
    topic = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class DisLike(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



@receiver(post_save, sender=Like)
def increase_discussion_rating_on_like(sender, instance, **kwargs):
    instance.discussion.rating += 1
    instance.discussion.user.rating += 1
    instance.discussion.save()
    instance.discussion.user.save()

@receiver(post_delete, sender=Like)
def decrease_discussion_rating_on_unlike(sender, instance, **kwargs):
    instance.discussion.rating -= 1
    instance.discussion.user.rating -= 1
    instance.discussion.save()
    instance.discussion.user.save()

@receiver(post_save, sender=DisLike)
def decrease_discussion_rating_on_dislike(sender, instance, **kwargs):
    instance.discussion.rating -= 1
    instance.discussion.user.rating -= 1
    instance.discussion.save()
    instance.discussion.user.save()

@receiver(post_delete, sender=DisLike)
def increase_discussion_rating_on_undislike(sender, instance, **kwargs):
    instance.discussion.rating += 1
    instance.discussion.user.rating += 1
    instance.discussion.save()
    instance.discussion.user.save()
