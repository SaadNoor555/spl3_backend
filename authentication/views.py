from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import make_password
import face_recognition
from .models import *
from passlib.handlers.django import django_pbkdf2_sha256

# Create your views here.
def signup(request):
    print('yo')
    if request.method == 'POST':
        form = json.loads(request.body)
        print(form)
        username = form['username']
        password = form['password']
        password = make_password(password)
        img = form['img_dir']
        userimg = face_recognition.load_image_file(img)
        user_encoding = face_recognition.face_encodings(userimg)[0]
        # cur_user = User.objects.get(username=username)
        # if cur_user!=None:
        #     return JsonResponse('Username Exists', safe=False)
        new_user = User.objects.create(username=username, password=password, face=user_encoding, img=img)
        new_user.save()
        return JsonResponse('User saved', safe=False)
    else:
        print('invalid request')
        return JsonResponse('Only POST request allowed', safe=False)

def signin(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        username = form['username']
        password = form['password']
        cur_user = User.objects.get(username=username)
        if cur_user!=None and django_pbkdf2_sha256.verify(password, cur_user.password):
            return JsonResponse('Successfully Logged In', safe=False)
        else:
            return JsonResponse('no such credentials', safe=False)
    else:
        return JsonResponse('Only POST request allowed', safe=False)
