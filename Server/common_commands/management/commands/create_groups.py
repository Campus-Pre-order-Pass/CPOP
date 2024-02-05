# yourapp/management/commands/create_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from Customer.models import *
from Order.models import *

from helper.auth.creat import creat_permission_tool




class Command(BaseCommand):
    help = 'Create and manage user groups'

    # def handle(self, *args, **options):
    #     # Create or get the desired groups with verbose_name and help_text
    #     whitelist_group = creat_permission_tool.create_or_get_group('WhitelistGroup', '白名單群組', 'This group has whitelist permissions.')
    #     blacklist_group = creat_permission_tool.create_or_get_group('BlacklistGroup', '黑名單群組', 'This group has blacklist permissions.')
        
    #     # customer models

    #     # Assign permissions for Customer model
    #     creat_permission_tool.assign_permissions(whitelist_group, ContentType.objects.get_for_model(Customer))
        
        
    #     # order models =================================================
    #     # Assign permissions for Order model
    #     creat_permission_tool.assign_permissions(whitelist_group, ContentType.objects.get_for_model(Order))
        
    #     # TransactionLog
    #     creat_permission_tool.assign_permissions(whitelist_group, ContentType.objects.get_for_model(TransactionLog))
        

    #     # Assign permissions for CustomerGroupMembership model
    #     self.assign_customergroupmembership_permissions(whitelist_group)

    #     # Output success message
    #     self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully.'))



    # def assign_customergroupmembership_permissions(self, group):
    #     """_summary_

    #     Args:
    #         group (_type_): _description_
    #     """
    #     content_type_customergroupmembership = ContentType.objects.get_for_model(CustomerGroupMembership)

    #     # Add 'view' permission to the group for CustomerGroupMembership model
    #     view_permission_customergroupmembership_codename = 'view_permission'
        
    #     creat_permission_tool.add_permission_to_group(group, content_type_customergroupmembership, view_permission_customergroupmembership_codename, 'view')

    #     # Add 'add' permission to the group for CustomerGroupMembership model
    #     add_permission_customergroupmembership_codename = 'add_permission'

    #     creat_permission_tool.add_permission_to_group(group, content_type_customergroupmembership, add_permission_customergroupmembership_codename, 'add')

    #     # Do not add 'delete' permission to the group for CustomerGroupMembership model


    def handle(self, *args, **options):
        # Get or create the WhitelistGroup
        whitelist_group, created = Group.objects.get_or_create(name='WhitelistGroup')
        blacklist_group  = creat_permission_tool.create_or_get_group('BlacklistGroup', '黑名單群組', 'This group has blacklist permissions.')


        # Define the permission IDs you want to assign to the WhitelistGroup
        permission_ids_to_assign = [81, 82, 83, 84, 130, 131, 133, 85, 87, 88, 89, 90, 91, 92, 126, 127, 128, 129]

        # Assign each permission to the WhitelistGroup
        for permission_id in permission_ids_to_assign:
            try:
                # Get the permission object
                permission = Permission.objects.get(id=permission_id)

                # Add the permission to the group
                whitelist_group.permissions.add(permission)

                self.stdout.write(self.style.SUCCESS(f'Permission "{permission.codename}" added to the group.'))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Permission with ID {permission_id} does not exist. Skipping.'))

        self.stdout.write(self.style.SUCCESS('Permissions assigned successfully to the WhitelistGroup.'))