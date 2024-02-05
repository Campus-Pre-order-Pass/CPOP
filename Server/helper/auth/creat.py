from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class CreatPermission(BaseCommand):
    def create_or_get_group(self, name, verbose_name, help_text):
        """creat or get

        Args:
            name (_type_): _description_
            verbose_name (_type_): _description_
            help_text (_type_): _description_

        Returns:
            _type_: _description_
        """
        # group, created = Group.objects.get_or_create(name=name, defaults={'verbose_name': verbose_name, 'help_text': help_text})
        group, created = Group.objects.get_or_create(name=name)
        return group
    
    def assign_permissions(self, group, content_type):
        """base rule

        Args:
            group (_type_): _description_
            content_type (_type_): _description_
        """
        permissions = [
            ('view_permission', 'view'),
            ('change_permission', 'change'),
            ('delete_permission', 'delete'),
            # Add more permissions as needed
        ]

        for codename, action in permissions:
            if group.name != 'BlacklistGroup':
                self.add_permission_to_group(group, content_type, codename, action)
                
    def add_permission_to_group(self, group, content_type, codename, action):
        """add

        Args:
            group (_type_): _description_
            content_type (_type_): _description_
            codename (_type_): _description_
            action (_type_): _description_
        """
        permission_codename = f'{action}_permission'
        
        try:
            permission = Permission.objects.get(content_type=content_type, codename=permission_codename)
            group.permissions.add(permission)
        except Permission.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Permission "{permission_codename}" does not exist. Not adding to the group.'))










# export permissions tool class
creat_permission_tool = CreatPermission()