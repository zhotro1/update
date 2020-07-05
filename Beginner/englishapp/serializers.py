from rest_framework import serializers
from .models import EnglishAppModel


class EnglishAppSerializer(serializers.ModelSerializer):
	class Meta:
		model = EnglishAppModel
		fields = ['card_name', 'card_pic', 'card_voice']