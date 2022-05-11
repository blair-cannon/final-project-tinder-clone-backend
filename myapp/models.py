from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from django.conf import settings
from django.dispatch import receiver


# Referecned model classes:

class Location(models.Model):
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.city
    
class Park(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Gender(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label

class Socialization(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Aggression(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Tag(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Size(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

# Models with foriegn keys

class User(AbstractUser):
    second_parent = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        g = Group.objects.get(name='Dog Owners') 
        g.user_set.add(instance)

class Dog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    age = models.CharField(max_length=300)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    about_me = models.CharField(max_length=2000, blank=True, null=True)
    favorite_park = models.ForeignKey(Park, on_delete=models.CASCADE, blank=True, null=True)
    socialization = models.ForeignKey(Socialization, on_delete=models.CASCADE)
    aggression = models.ForeignKey(Aggression, on_delete=models.CASCADE)
    is_fixed = models.BooleanField()
    has_bitten = models.BooleanField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='myapp/dog-images/')
    caption = models.CharField(max_length=2000, blank=True, null=True)
    is_profile_pic = models.BooleanField(default=True)

class Connection(models.Model):
    dog_initializer = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='initializer')
    dog_target = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='target')
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

class Conversation(models.Model):
    dog_creator = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='creator')
    dog_other = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='other')
    subject = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    dog_sent = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='sent')
    dog_received = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='received')
    content = models.CharField(max_length=3000, blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    testimony = models.CharField(max_length=3000, blank=True, null=True)