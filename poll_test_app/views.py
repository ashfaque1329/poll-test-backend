from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from poll_test_app.models import *
from poll_test_app.serializers import *


# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def poll_list(request, format=None):
    """
    List all polls.
    """
    if request.method == 'GET':
        poll = Poll.objects.all()
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def poll_detail(request, id, format=None):
    """
    Retrieve, create or delete a poll.
    """
    try:
        poll = Poll.objects.get(id=id)
    except poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        poll = Poll.objects.get(id=id)
        data = JSONParser().parse(request)
        options_id = data['options'][0]['id']
        options_votes = data['options'][0]['votes']
        option = Option.objects.get(id=options_id, poll_id=id)
        option.votes = option.votes+options_votes
        option.save()
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        poll.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def option_list(request, format=None):
    """
    List all options.
    """
    if request.method == 'GET':
        option = Option.objects.all()
        serializer = OptionSerializer(option, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def option_detail(request, slug_option, format=None):
    """
    Retrieve,update or delete an option.
    """
    try:
        option = Option.objects.get(slug_option=slug_option)
    except option.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OptionSerializer(option, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        option.delete()
        return Response(status=204)
