from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from . import serializers
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate, login, logout
from users.models import User
from rest_framework.authtoken.models import Token


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        user = request.user
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.UserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:
            Response(serializer.errors)


class SignUp(APIView):
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")

            if User.objects.filter(username=username):
                return Response(
                    {"fail": "이미 존재하는 이름입니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = User.objects.create(
                username=username,
                name=username,
            )
            user.set_password(password)
            user.save()

            # 사용자에 대한 토큰 생성
            token, created = Token.objects.get_or_create(user=user)

            # 사용자 로그인
            login(request, user)

            return Response(
                {
                    "ok": "회원가입 성공!",
                    "token": token.key,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            print(e)
            return Response(
                {"error": "회원가입 중 오류가 발생했습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # print(request.data)
        # print(username, password)

        if not username or not password:
            raise ParseError
        user = authenticate(
            username=username,
            password=password,
        )

        user = User.objects.filter(username=username).first()
        print(user.check_password(password))

        if user:
            login(request, user)
            print(request.session.session_key)  # 세션 키 출력
            return Response({"ok": "Welcome!"})
        else:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "See you later!"})
