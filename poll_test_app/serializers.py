from django.contrib.auth.models import *
from poll_test_app.models import *
from rest_framework import serializers


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'option_text', 'votes')


class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'options')

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        print("options_data", options_data)
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(poll=poll, **option_data)
        return poll

    '''def update(self, instance, validated_data):
        options_data = validated_data.pop('options')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(poll=poll, **option_data)
        return poll'''
