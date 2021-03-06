from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.login.serializers.users import UserSerializer


class UserSignupViewset(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=("post",), detail=False, url_path="sign-up")
    def sign_up(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=serializer.validated_data)
        token = serializer.get_token()
        token["username"] = serializer.validated_data["username"]
        return Response(token, status=status.HTTP_201_CREATED)
