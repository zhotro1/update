from rest_framework import serializers
from .models import Persion

class PersionSerilizer(serializers.ModelSerializer):
	persion_img = serializers.SerializerMethodField()
	def get_persion_img(self, obj):
		return self.context['request'].build_absolute_uri(obj.persion_img.url)

	class Meta:
		model = Persion
		fields = ['persion_img', 'persion_name']

	def create(self, validated_data):
		return Persion.objects.create(**validated_data)