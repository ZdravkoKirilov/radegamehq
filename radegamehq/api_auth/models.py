from django.db import models
from django.core.mail import send_mail


class AppUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_authenticated = models.BooleanField(default=False)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    class Meta:
        pass

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return '{}'.format(self.email)


