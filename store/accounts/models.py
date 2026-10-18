from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    man = 1
    woman = 2

    status_choice = (
        (man, "Male"),
        (woman, "Female"),
    )

    status = models.IntegerField(choices=status_choice)

    profileImage = models.ImageField(
        upload_to="profileImage/",
        verbose_name="Photo",
        blank=True,
        null=True
    )

    credit = models.IntegerField(default=0)

    class Meta:
        verbose_name = "user"
        db_table = "UserProfile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.user.username}'s Profile"