import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Logica import users
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def index(request):
    #body_unicode = request.body.decode('utf-8')
    #body = json.loads(body_unicode)
    #nick_name = body['nick_name']
    #fullname = body['fullname']
    nick_name = request.POST.get('nick_name')
    fullname = request.POST.get('fullname')
    try:
        user = users.create_user(nick_name=nick_name, fullname=fullname)
        response = {
        "status": "sucessfull",
        "code": 200,
        "data": "good ending"
        }
    except Exception as err:
        response = {
        "status": "error",
        "code": 500,
        "data": "bad ending()"
        }
    return JsonResponse(response)
