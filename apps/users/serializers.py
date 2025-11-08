from rest_framework import serializers
from django.contrib.auth.models import User, Group

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Editor', 'Editor'),
    ('Viewer', 'Viewer'),
]
class UserRoleSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    role = serializers.ChoiceField(choices=ROLE_CHOICES, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role', 'group']
        extra_kwargs = {'password': {'write_only': True}}

    def get_group(self, obj):
        group = obj.groups.first()
        return group.name if group else None

    def create(self, validated_data):
        role_name = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # Assign to group
        group = Group.objects.get(name=role_name)
        user.groups.add(group)
        return user

    def update(self, instance, validated_data):
        role_name = validated_data.get('role')
        if not role_name:
            raise serializers.ValidationError({"role": "This field is required."})
        try:
            group = Group.objects.get(name=role_name)
        except Group.DoesNotExist:
            raise serializers.ValidationError({"role": f"Group '{role_name}' does not exist."})
        # Remove from existing groups
        instance.groups.clear()
        # Add to new group
        group = Group.objects.get(name=role_name)
        instance.groups.add(group)
        return instance
