from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create user roles and assign permissions'

    def handle(self, *args, **kwargs):
        # Create roles
        admin_group, created = Group.objects.get_or_create(name='Admin')
        editor_group, created = Group.objects.get_or_create(name='Editor')
        viewer_group, created = Group.objects.get_or_create(name='Viewer')
        
        # Assign permissions
        view_doc_permission = Permission.objects.get(codename='view_document')
        change_doc_permission = Permission.objects.get(codename='change_document')
        add_doc_permission = Permission.objects.get(codename='add_document')
        delete_doc_permission = Permission.objects.get(codename='delete_document')
        add_user_permission = Permission.objects.get(codename='add_user')
        change_user_permission = Permission.objects.get(codename='change_user')
        
        # Add permissions to groups
        viewer_group.permissions.add(view_doc_permission)
        editor_group.permissions.add(view_doc_permission, change_doc_permission, add_doc_permission)
        admin_group.permissions.add(view_doc_permission, change_doc_permission, add_doc_permission, delete_doc_permission, add_user_permission, change_user_permission)

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))