# yourapp/checks.py

from django.core.checks import register, Tags, Error

from django.contrib.auth.models import Group

@register(Tags.models)
def check_whitelist_and_blacklist_groups(app_configs, **kwargs):
    errors = []

    # Check WhitelistGroup
    try:
        whitelist_group = Group.objects.get(name='WhitelistGroup')
    except Group.DoesNotExist:
        errors.append(
            Error(
                "WhitelistGroup is missing",
                hint="Create the 'WhitelistGroup' group.",
                obj=None,
                id='Customer.E001',
            )
        )

    # Check BlacklistGroup
    try:
        blacklist_group = Group.objects.get(name='BlacklistGroup')
    except Group.DoesNotExist:
        errors.append(
            Error(
                "BlacklistGroup is missing",
                hint="Create the 'BlacklistGroup' group.",
                obj=None,
                id='Customer.E002',
            )
        )

    return errors
