from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.exceptions import ParseError
from rest_framework import status

from simplesocial.models import Persion
from simplesocial.serializers import PersionInfoSerializer

from englishapp.models import EnglishAppModel, EnglishGameScoreModel
from englishapp.serializers import EnglishAppSerializer, EnglishGameScoreSerializer
from rest_framework.authtoken.models import Token

from .permistions import IsAdminOrReadOnly, IsOwnerOrReadOnly

import random


class PersionInfoApiView(APIView):
	parser_classes = [MultiPartParser, FormParser, JSONParser]
	authentication_classes= [TokenAuthentication]
	permission_classes = [IsAdminOrReadOnly]

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
	parser_classes = [MultiPartParser, FormParser, FileUploadParser,JSONParser]
	authentication_classes= [TokenAuthentication]
	permission_classes = [IsAdminOrReadOnly]

	def get(self, request, format=None):
		queryset = EnglishAppModel.objects.all().order_by("?")[:6]
		serializer = EnglishAppSerializer(instance=queryset, many=True)
		context = {}
		context["cards"] = serializer.data
		context['nana'] = random.choice(context['cards'])['card_name']

		if request.user.is_authenticated:
			score = EnglishGameScoreModel.objects.get_or_create(user=request.user)[0]
			score.get_new_seesion()
			private_key = score.gen_detected_key()
			context['score'] = score.score
			context['private_key'] = private_key
		
		return Response(context, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = EnglishAppSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return(serializer.errors, status.HTTP_400_BAD_REQUEST)


class EnglishGameScoreApiView(APIView):
	parser_classes = [MultiPartParser, FormParser, FileUploadParser, JSONParser]
	authentication_classes= [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def post(self,request, format=None):
		user = request.user
		score = EnglishGameScoreModel.objects.get_or_create(user=user)[0]
		serializer = EnglishGameScoreSerializer(instance =score, data = request.data)
		if serializer.is_valid():
			check = score.check_valid_key(request.data.get('detected_key', 'invalidkey'))
			if check:
				score.answer = request.data.get('answer', 'invalidanswer')
				score.save()
				return Response("success updated data", status.HTTP_201_CREATED)
			else:
				return Response(status = status.HTTP_304_NOT_MODIFIED)
		return(serializer.errors, status.HTTP_400_BAD_REQUEST)



