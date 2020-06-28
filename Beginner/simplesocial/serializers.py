from rest_framework import serializers
from simplesocial.models import Persion


class PersionInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persion
		fields = ['persion_img', 'persion_name']