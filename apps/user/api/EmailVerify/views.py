from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.user.models import VerifyEmail, User

from .serializer import EmailVerifySerializer


class EmailVerifyGenericView(GenericAPIView):
    serializer_class = EmailVerifySerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')
        verify = VerifyEmail.objects.filter(email=email, code=code).first()
        if verify:
            user = User.objects.filter(email=email).first()
            user.is_verified = True
            user.save()
            return Response({
                'status': True,
                'message': 'Email is verified!'
            }, status=status.HTTP_200_OK)
        return Response({'message': 'Email or code is invalid!'}, status=status.HTTP_400_BAD_REQUEST)
