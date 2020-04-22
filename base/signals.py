from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import Profile




@receiver(post_save,sender=User)
def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #instance here is the objects of the User models whenever the new user registers and logs in
                                                #i check whether this user is new or not if yes i want Profile models to create an object whose user is equal to the new user
        print('Profile created')

# post_save.connect(create_profile,sender=User)



@receiver(post_save,sender=User)
def update_profile(sender,instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile Updated')

# post_save.connect(update_profile,sender=User)