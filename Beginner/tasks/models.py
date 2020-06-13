from django.db import models
from django.forms import ModelForm
from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()

PRIORITIES = (
        ('adanger', 'Ưu tiên cao'),
        ('bwarning', 'Ưu tiên vừa'),
        ('csuccess', 'Ưu tiên thấp')
    )

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
                    max_length=30,
                    choices=PRIORITIES,
                    default=PRIORITIES[0][0]
                )
    complete = models.IntegerField(default=0)

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'date_of_creation', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Bạn đang cần làm gì hôm nay?"}),
            'description': forms.Textarea(attrs={'placeholder': "Mô tả công việc này ..", 'cols': 80, 'rows': 3}),
        }

