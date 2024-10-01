import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import UserProfile
#1
@receiver(post_save, sender=UserProfile)
def profile_saved_sync(sender, instance, **kwargs):
    print(f"Signal started for {instance.username}")
    time.sleep(5)  # Simulate a long process
    print(f"Signal finished for {instance.username}")

#2
@receiver(post_save, sender=UserProfile)
def profile_saved_thread(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")


#3
@receiver(post_save, sender=UserProfile)
def profile_saved_transaction(sender, instance, **kwargs):
    print(f"Signal triggered for {instance.username}")
    if instance.username == "rollback_test":
        raise Exception("Triggering rollback")
