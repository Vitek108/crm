from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


# SIGNAL:
def post_user_crated_signal(sender, instance, created, **kwargs): # instance = prvek modelu, který byl uložen,
    # created = říká, zda byla instance nově vytvořena či ne (true/false)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_crated_signal, sender=User) # connect bere jméno volané funkce a sender = model, který posílá událost