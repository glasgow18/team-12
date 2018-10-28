from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
import requests
# Create your views here.

id = 0
nodes = {0:{"answer":"Where do you live?","key":"hello"}}
'''
@csrf_exempt
def returnAnswer(request):
    return HttpResponse("yo")
    print("yoooooooooooooooooooo3")
    try:

        print (request.body)
        if request.method == 'GET':
            json_data = request.body.decode('utf-8')
            for k,v in nodes:
                if request == v["key"]:
                    answer = v["answer"]
                    return answer
        else:
            print ("lol")
            return HttpResponse("OKi")
    except:
        return HttpResponse("Key characteristics not found")
'''
@csrf_exempt
def returnAnswer(request):
    try:
        #print (request.body)
        if request.method == 'POST':
            json_data = json.loads(request.body.decode('utf-8'))
            for k,v in nodes.items():
                if json_data["key"] == v["key"]:
                    answer = v["answer"]
                    print(answer)
                    return HttpResponse(answer)
            return HttpResponse("New Answer")

        else:
            return HttpResponse("Not POst Sent")
    except:
        return HttpResponse("Key characteristics not found")
    return HttpResponse("Hello, world")
