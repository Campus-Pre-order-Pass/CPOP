from django.dispatch import receiver
from django.db.models.signals import post_save 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from Customer.models import *

@receiver(post_save, sender=Customer)
def create_or_update_customer(sender, instance, created, **kwargs):
    """when created cumtomer add `WhitelistGroup` to  group 

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
        created (_type_): _description_
    """
    if created:
        # 如果是新建立的 Customer 實例
        whitelist_group = Group.objects.get(name='WhitelistGroup')
        CustomerGroupMembership.objects.create(uid=instance.uid, group=whitelist_group)