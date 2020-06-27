from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

from .serializers import PersionSerilizer
from .models import Persion
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser

class ReadOnly(BasePermission):
	def has_permission(self, request, view):
		return request.method in SAFE_METHODS

class PersionListView(APIView):
	parser_classes = (FormParser, MultiPartParser)
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated|ReadOnly,)

	def get(self, request, format=None):
		"""
        curl -X GET \
          -H 'Authorization: Token {header_token_key}' \
          http://127.0.0.1:8000/api/whois/persions/
        """
		persions = Persion.objects.all()
		serializer = PersionSerilizer(persions, many=True, context={"request": request})
		return Response(data=serializer.data, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		"""
		curl -X POST -S \
		  -H 'Accept: application/json' \
		  -H 'Content-Type: multipart/form-data' \
		  -H 'Authorization: Token {header_token_key}' \
		  -F "selection={selection_code/url_code}" \
		  -F "name={candidate name}" \
		  -F "about={about}" \
		  -F "photo=@/path/to/your_photo.jpg;type=image/jpg" \
		  http://localhost:8000/api/v1/candidates
		"""
		serializer = PersionSerilizer(data=request.data, context={"request": request})
		if serializer.is_valid():
			serializer.save(
				persion_name = request.data.get('persion_name'),
				persion_img = request.data.get('persion_img')
			)
			print(serializer.data['persion_img'])
			serializer.data['persion_img'] = request.build_absolute_uri(serializer.data['persion_img'])
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


