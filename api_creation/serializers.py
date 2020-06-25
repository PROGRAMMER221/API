from rest_framework import serializers
from .models import student, profile
from django.contrib.auth.models import User


class studentserializer(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = '__all__'

class profileserializer(serializers.ModelSerializer):

    class Meta:
        model = profile
        fields = ('name','pic')


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')
