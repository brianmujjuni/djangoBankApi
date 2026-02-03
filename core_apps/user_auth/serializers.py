from django.contrib.auth import get_user_model
from djoser.serializers import (
    UserCreateSerializer as DjaoserUserCreateSerializer,
)

User = get_user_model()


class UserCreateSerializer(DjaoserUserCreateSerializer):
    class Meta(DjaoserUserCreateSerializer.Meta):
        model = User
        fields = [
            "id_no",
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
            "security_question",
            "security_answer",
        ]
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
