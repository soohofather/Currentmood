from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        validators=[MinLengthValidator(5)], max_length=16, unique=True
    )
    last_name = models.CharField(validators=[MinLengthValidator(1)], max_length=20)
    first_name = models.CharField(validators=[MinLengthValidator(1)], max_length=20)
    address = models.CharField(max_length=50)
    user_img = ProcessedImageField(
        upload_to="user_img/",
        blank=True,
        processors=[ResizeToFill(400, 400)],
        format="JPEG",
        options={"quality": 100},
        null=True,
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    profile_music_id = models.CharField(max_length=30, default=None, null=True)
    profile_music_title = models.CharField(max_length=50, default=None, null=True)
    profile_music_channel = models.CharField(max_length=30, default=None, null=True)

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

    