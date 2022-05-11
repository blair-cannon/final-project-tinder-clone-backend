from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations, models
import django.db.models.deletion
import logging


logger = logging.getLogger(__name__)

role_permissions = {
    'Dog Owners': (
        'Can view message',
        'Can delete message',
        'Can add message',
        'Can change message',
        'Can view conversation',
        'Can delete conversation',
        'Can add conversation',
        'Can change conversation',
        'Can view location',
        'Can delete location',
        'Can add location',
        'Can change location',
        'Can view park',
        'Can delete park',
        'Can add park',
        'Can change park',
        'Can view breed',
        'Can delete breed',
        'Can add breed',
        'Can change breed',
        'Can view gender',
        'Can delete gender',
        'Can add gender',
        'Can change gender',
        'Can view socialization',
        'Can delete socialization',
        'Can add socialization',
        'Can change socialization',
        'Can view aggression',
        'Can delete aggression',
        'Can add aggression',
        'Can change aggression',
        'Can view tag',
        'Can delete tag',
        'Can add tag',
        'Can change tag',
        'Can view size',
        'Can delete size',
        'Can add size',
        'Can change size',
        'Can view user',
        'Can delete user',
        'Can add user',
        'Can change user',
        'Can view dog',
        'Can delete dog',
        'Can add dog',
        'Can change dog',
        'Can view image',
        'Can delete image',
        'Can add image',
        'Can change image',
        'Can view connection',
        'Can delete connection',
        'Can add connection',
        'Can change connection',
        'Can view comment',
        'Can delete comment',
        'Can add comment',
        'Can change comment',
    ),
}


# See https://code.djangoproject.com/ticket/23422
def add_role_permissions(apps, schema_editor):
    emit_post_migrate_signal(2, False, 'default')

    for r in role_permissions:
        role, created = Group.objects.get_or_create(name=r)
        for p in role_permissions[r]:
            perm, created2 = Permission.objects.get_or_create(name=p)
            role.permissions.add(perm)
        role.save()


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '__latest__'),
        ('auth', '__latest__'),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_role_permissions),
    ]

# Users don't have perms to start unless superuser
# Signals => post_save() runs before completely saving object
# Custom migrations - use of __latest__
# Groups can have permissions and be attached to Users, User can also have single perms
# SITE_ID
# Permissions model
# Using shell to debug
# migrations.RunPython for seeding a DB maybe.
# Only is_staff can use Django admin. Could add is_staff as Boolean field and default to true
# get_or_create()
