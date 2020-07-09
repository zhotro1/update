from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import random, string, datetime

def get_to_day_min():
	return datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp()



def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


class EnglishAppModel(models.Model):
	card_name = models.CharField(max_length=100, unique=True, blank=False)
	card_pic = models.ImageField(null=False, blank=False)
	card_voice = models.FileField(null=False, blank=False)

	def __str__(self):
		return self.card_name


class EnglishGameScoreModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='englishscore')
	score = models.IntegerField(default=0)
	answer = models.CharField(max_length=100, blank=True)
	time_update_score = models.FloatField(default=0)
	detected_key = models.CharField(editable=False, blank=True, max_length=100)
	time_update_key = models.FloatField(default=0)
	detected_d = models.PositiveSmallIntegerField(default=0)
	detected_s = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return '{}: {}'.format(self.user.username, self.score)

	def gen_detected_key(self):
		self.answer = ''
		self.detected_key = get_random_alphaNumeric_string()
		self.time_update_key = datetime.datetime.now().timestamp()
		self.detected_d = 0
		self.detected_s = 0
		self.save()
		return self.detected_key

	def get_new_seesion(self):
		if self.time_update_score < get_to_day_min():
			self.score = 0
			self.save()

	def check_valid_key(self, key):
		now = datetime.datetime.now().timestamp()
		if ((now - self.time_update_key) < 31) and (self.detected_key == key):
			return True
		else:
			return False

	def save(self, *args, **kwargs):
		if (self.answer == 'dung') and (self.detected_d == 0):
			self.score += 30
			self.detected_d += 1
			self.time_update_score = datetime.datetime.now().timestamp()
		elif (self.answer == 'sai') and (self.detected_s < 5):
			self.score -= 20
			self.detected_s += 1
			self.time_update_score = datetime.datetime.now().timestamp()
		super().save(*args, **kwargs)










