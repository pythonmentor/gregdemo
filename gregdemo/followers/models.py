from django.db import models
from django.conf import settings


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        verbose_name_plural = "users follow"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'followed_user'], name='unique_friendship'
            )
        ]

    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"
