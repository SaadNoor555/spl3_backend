from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth.hashers import make_password
import face_recognition
from .models import *

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        username = form['username']
        password = form['password']
        password = make_password(password)
        img = form['img_dir']
        userimg = face_recognition.load_image_file(img)
        user_encoding = face_recognition.face_encodings(userimg)[0]
        new_user = User.objects.create(username=username, password=password, face=user_encoding, img=img)
        new_user.save()
        return JsonResponse('User saved', safe=False)
    else:
        print('invalid request')
        return JsonResponse('GET request not allowed', safe=False)

def signin(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        username = form['username']
        password = form['password']
        
