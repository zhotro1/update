from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.exceptions import ParseError
from rest_framework import status

# Create your views here.

from simplesocial.models import Persion
from simplesocial.serializers import PersionInfoSerializer

from englishapp.models import EnglishAppModel
from englishapp.serializers import EnglishAppSerializer

class ReadOnly(BasePermission):
	def has_permission(self, request, view):
		return request.method in SAFE_METHODS


class PersionInfoApiView(APIView):
	parser_classes = [MultiPartParser, FormParser]
	authentication_classes= [TokenAuthentication]
	permission_classes = [IsAuthenticated|ReadOnly]

	def get(self,request, format=None):
		queryset = Persion.objects.all()
		serializer = PersionInfoSerializer(instance=queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = PersionInfoSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return(serializer.errors, status.HTTP_400_BAD_REQUEST)

class EnglishAppApiView(APIView):
	parser_classes = [MultiPartParser, FormParser, FileUploadParser]
	authentication_classes= [TokenAuthentication]
	permission_classes = [IsAuthenticated|ReadOnly]

	def get(self,request, format=None):
		queryset = EnglishAppModel.objects.all()
		serializer = EnglishAppSerializer(instance=queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		print('data', request.data)
		serializer = EnglishAppSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return(serializer.errors, status.HTTP_400_BAD_REQUEST)


