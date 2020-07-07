from rest_framework import serializers
from .models import EnglishAppModel, EnglishGameScoreModel


class EnglishAppSerializer(serializers.ModelSerializer):
	class Meta:
		model = EnglishAppModel
		fields = ['card_name', 'card_pic', 'card_voice']


class EnglishGameScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = EnglishGameScoreModel
		fields = ['answer', 'detected_key']



