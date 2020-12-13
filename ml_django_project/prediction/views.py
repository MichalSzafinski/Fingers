from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.conf import settings

from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

from prediction.Fingers.predict import *


def home_view(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('/login_error/')
    return render(request, "index.html")


@csrf_exempt
def upload_photo_view(request):
    if request.method == 'POST':
        upload = Upload.objects.create(
            user='',
            image='',
        )
        output = predict(upload.get_path())
        upload.prediction = str(output[0])
        upload.chance = str(output[1])
        upload.save()
    return JsonResponse({'prediciton': upload.prediction, 'szanse': upload.chance})


class UploadView(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
