from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_('Required. Must be a valid email address.')
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message=_('Username may contain only letters, numbers and @/./+/-/_ characters.')
            )
        ],
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    )
    first_name = models.CharField(
        _('first name'),
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        _('biography'),
        blank=True,
        max_length=500
    )
    profile_image = models.ImageField(
        _('profile image'),
        upload_to='profiles/',
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        """Returns the user's full name."""
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def followers_count(self):
        """Returns number of followers."""
        return self.followers.count()

    @property
    def following_count(self):
        """Returns number of users being followed."""
        return self.following.count()


class Subscription(models.Model):
    subscriber = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name=_('subscriber')
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name=_('author')
    )
    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
        unique_together = ('subscriber', 'author')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subscriber.username} follows {self.author.username}"

    def clean(self):
        """Validate that user can't subscribe to themselves."""
        if self.subscriber == self.author:
            raise ValidationError(_("User cannot subscribe to themselves."))